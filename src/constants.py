# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""


class AppConstants(object):
    # Maximum number of words in a comment's content
    CONTENT_MAX_WORDS = 1000
    # Socket message types
    NEW_COMMENT = 'NEW_COMMENT'
    # Socket message contents
    SOCKET_MESSAGE_CONTENT = {
        NEW_COMMENT: {
            'title': {
                'vn': '{user_name} vừa bình luận bài đăng của bạn',
                'en': '{user_name} has just commented on your post',
            },
            'description': {
                'vn': '{user_name} vừa bình luận bài đăng của bạn',
                'en': '{user_name} has just commented on your post',
            }
        },
    }
