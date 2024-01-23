#!/usr/bin/env python3
"""
List all documents in a collection
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection

    parameters:
    - mongo_collection
    return:
    - returns a list of documents in mongo_collection
    """
    return mongo_collection.find()
