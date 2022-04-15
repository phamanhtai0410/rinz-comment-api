# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from marshmallow import Schema, fields, EXCLUDE, INCLUDE

from lib.schema.req import BaseReq


# Create Comment

class CreateCommentSchemaReq(BaseReq):
    class Meta:
        unknown = INCLUDE
        ordered = True

    type = fields.String(required=True, blank=False)
    item_id = fields.String(required=True, blank=False)
    parent_id = fields.String(required=False, default='')
    content = fields.String(required=True, blank=False)


class CreateCommentRes(Schema):
    class Meta:
        unknown = EXCLUDE
        ordered = True

    result = fields.String(required=True, allow_none=False)



