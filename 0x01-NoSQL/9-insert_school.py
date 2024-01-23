#!/usr/bin/env python3
"""
Python scripts that inserts a document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the collection based on kwargs
    Arguments:
    - variable arguments
    Return:
    - returns a new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
