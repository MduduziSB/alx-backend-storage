#!/usr/bin/env python3
"""
Python scripts that updates all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name

    Arguments:
    - mango_collection (database)
    - name (string)
    - topics (list)

    Return:
    - void
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
