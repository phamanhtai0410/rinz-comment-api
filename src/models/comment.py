# -*- coding: utf-8 -*-

# File: session.py

"""
   Description:
        -
        - Comment database model for RINZ-IO
"""
from lib.model import BaseMG
from pymodm import fields


class Comment(BaseMG):
    class Meta:
        collection_name = 'comment'
        final = True
        ignore_unknown_fields = True

    _id = fields.ObjectIdField(primary_key=True)
    type = fields.CharField(default='', blank=False)
    item_id = fields.CharField(default='', blank=False)
    parent_id = fields.CharField(blank=True)
    content = fields.CharField(blank=False)
    public_address = fields.CharField(blank=False)
    no_children = fields.IntegerField(default=0)
    status = fields.BooleanField(default=True)
