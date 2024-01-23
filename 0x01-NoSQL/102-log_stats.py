#!/usr/bin/env python3
"""
MongoDB nginx log stats
"""
from pymongo import MongoClient


def nginx_log_stats(nginx_logs):
    """
    Displays nginx log stats

    Arguments:
    - None

    Return:
    - void
    """
    print("{} logs".format(nginx_logs.count_documents({})))
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_logs.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))

    status_checks_count = len(list(
        nginx_logs.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def top_ten_ips(nginx_logs):
    """
    Displays nginx log stat about the top 10 most appearing HTTP IPs

    Arguments:
    - nginx_logs

    Return:
    - void
    """
    print("IPs:")
    top_logs = nginx_logs.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for log in top_logs:
        ip = log['_id']
        log_count = request_log['totalRequests']
        print('\t{}: {}'.format(ip, log_count))


def run():
    """
    Runs the above methods

    Arguments:
    - None

    Return:
    - void
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_log_stats(client.logs.nginx)
    top_ten_ips(client.logs.nginx)


if __name__ == '__main__':
    run()
