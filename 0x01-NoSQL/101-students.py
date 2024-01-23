#!/usr/bin/env python3
"""
Python scripts that lists students sorted by avarage score
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    Arguments:
    - mongo_collection (database):

    Return:
    - list of studentd sorted by avarage score
    """
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
