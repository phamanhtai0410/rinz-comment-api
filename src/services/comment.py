# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import src.workers.comment as comment_worker


class CommentService(object):

    @staticmethod
    def save_comment(cls, _comment_body: dict):
        comment_worker.save_comment.delay(_comment_body)
        return {
            'result': 'Create new comment successfully !'
        }
