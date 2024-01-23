#!/usr/bin/env python3
"""
Python script that generates school list having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Generates the list of school having a specific topic

    Arguments:
    - mongo_collection
    - topic

    Return:
    - returns a list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
