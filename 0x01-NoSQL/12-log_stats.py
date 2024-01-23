#!/usr/bin/env python3
"""
MangoDB nginx log stats
"""

from pymongo import MongoClient


def nginx_log_stats():
    """
    Displays stats about Nginx logs stored in MongoDB
    """
    with MongoClient('mongodb://127.0.0.1:27017') as client:
        logs_collection = client.logs.nginx

        total_count = logs_collection.count_documents({})
        get_count = logs_collection.count_documents({"method": "GET"})
        post_count = logs_collection.count_documents({"method": "POST"})
        put_count = logs_collection.count_documents({"method": "PUT"})
        patch_count = logs_collection.count_documents({"method": "PATCH"})
        delete_count = logs_collection.count_documents({"method": "DELETE"})

        path_query = {"method": "GET", "path": "/status"}
        path_count = logs_collection.count_documents(path_query)

        print("{} logs".format(total_count))
        print("Methods:")
        print("\tmethod GET: {}".format(get_count))
        print("\tmethod POST: {}".format(post_count))
        print("\tmethod PUT: {}".format(put_count))
        print("\tmethod PATCH: {}".format(patch_count))
        print("\tmethod DELETE: {}".format(delete_count))
        print("{} status check".format(path_count))


if __name__ == "__main__":
    nginx_log_stats()
