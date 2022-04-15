# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from lib.decorators.http import make_response
from lib.enums.http import StatusInt
from src.enums.http import ErrorCode


class ErrorCommentException(Exception):
    def __init__(self, message='error_comment_exception', *args: object) -> None:
        super().__init__(*args)
        self.response = make_response(
            error_code=ErrorCode.ErrorComment,
            msg=message
        ), StatusInt.Bad

    pass
