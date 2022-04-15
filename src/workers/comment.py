# -*- coding: utf-8 -*-

# File: comment.py

"""
   Description:
        -
        -
"""
from lib.decorators import handle_exception
from src.task import worker
from src.models.comment import Comment
from bson import ObjectId
from sentry_sdk import capture_exception
import traceback
from src.constants import AppConstants
from src.helpers.comment import send_message_socket


@worker.task(name='worker.save_comment', rate_limit='20/s')
@handle_exception()
def save_comment(_comment_body: dict):
    try:
        Comment.insert(_comment_body)

        if _comment_body['parent_id']:
            Comment.objects.raw({'_id': ObjectId(_comment_body['parent_id'])}).update({'$inc': {'no_children': 1}})
        send_socket_message_task.delay(
            AppConstants.NEW_COMMENT,
            _comment_body['type'],
            _comment_body['public_address'],
            _comment_body['item_id'],
            _comment_body.to_dict()
        )
    except Exception as e:
        capture_exception(e)
        traceback.print_exc()

    return 'Update Comment success'


@worker.task(name='worker.send_to_socket_task', rate_limit='20/s')
@handle_exception()
def send_socket_message_task(message_type, item_type, public_address, item_id, _payload):
    _payload_dict = {
        **_payload,
        'public_address': public_address,
    }
    send_message_socket(message_type, item_type, public_address, item_id, _payload_dict)
    return 'Send message socket task finished successfully'
