#!/usr/bin/env python3
"""
MangoDB nginx log stats
"""

from pymongo import MongoClient


def nginx_log_stats():
    """
    Displays nginx log stats

    Arguments:
    - None

    Return:
    - void
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    nginx_coll = db['nginx']

    # Get the total number of logs
    total_logs = nginx_coll.count_documents({})

    # Get the count for each HTTP method
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    method_counts = {}
    for method in http_methods:
        method_counts[method] = nginx_coll.count_documents({"method": method})

    check_count = nginx_coll.count_documents({"method": "GET",
                                             "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in http_methods:
        print(f"    method {method}: {method_counts[method]}")
    print(f"{check_count} status check")

    client.close()


if __name__ == "__main__":
    nginx_log_stats()
