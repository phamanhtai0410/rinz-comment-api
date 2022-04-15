# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask import Blueprint

from .controller import create_new_comment

rest_comment = Blueprint('rest_comment', __name__, url_prefix='')
rest_comment.add_url_rule('add', methods=['POST'], view_func=create_new_comment)
