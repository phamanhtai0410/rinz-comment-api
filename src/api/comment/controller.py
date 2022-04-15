# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask import request

import lib
from lib.logger import Logger
from src.schemas.comment import CreateCommentSchemaReq, CreateCommentRes
from bson.objectid import ObjectId
from src.exceptions.comment import ErrorCommentException
from src.services.comment import CommentService
from src.constants import AppConstants
from lib.util import dt_utcnow


def is_valid_comment_length(content: str):
    """
        Check if comment's length (number of words) does not exceed the maximum limit
        This does not count spaces, newline characters
    """
    no_words = len(content.split())
    return no_words <= AppConstants.CONTENT_MAX_WORDS


@lib.handle_res(login=True, req_schema=CreateCommentSchemaReq, res_schema=CreateCommentRes)
def create_new_comment(body, params, *args, **kwargs):
    Logger.debug(msg="*** Create new comment", args=[body, kwargs['wallet']])

    if not ObjectId.is_valid(body.item_id):
        raise ErrorCommentException(message='invalid_item_id')

    if not ObjectId.is_valid(body.parent_id):
        raise ErrorCommentException(message='invalid_parent_id')

    if not is_valid_comment_length(body.content):
        raise ErrorCommentException(message='invalid_comment_length')

    _comment = {
        'type': body.type,
        'item_id': body.item_id,
        'parent_id': body.parent_id,
        'content': body.content,
        'public_address': kwargs['wallet']['user_id'],
        'status': True,
        'created_time': dt_utcnow(),
        'updated_time': dt_utcnow()
    }

    return CommentService.save_comment(_comment)

