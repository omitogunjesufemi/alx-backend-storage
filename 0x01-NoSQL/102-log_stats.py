#!/usr/bin/env python3
"""
Write a Python script that provides some stats about Nginx logs
stored in MongoDB:

    Database: logs
    Collection: nginx
    Display (same as the example):
        first line: x logs where x is the number of documents
in this collection
        second line: Methods:
        5 lines with the number of documents with the method =
["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
(see example below - warning: it’s a tabulation
before each line)
        one line with the number of documents with:
            method=GET
            path=/status
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    total_count = nginx_collection.count_documents({})
    get_count = nginx_collection.count_documents({"method": "GET"})
    post_count = nginx_collection.count_documents({"method": "POST"})
    put_count = nginx_collection.count_documents({"method": "PUT"})
    patch_count = nginx_collection.count_documents({"method": "PATCH"})
    delete_count = nginx_collection.count_documents({"method": "DELETE"})

    status_count = nginx_collection.count_documents({"method": "GET",
                                                     "path": "/status"})

    print(f"{total_count} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_count}")
    print(f"\tmethod POST: {post_count}")
    print(f"\tmethod PUT: {put_count}")
    print(f"\tmethod PATCH: {patch_count}")
    print(f"\tmethod DELETE: {delete_count}")
    print(f"{status_count} status check")

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(logs_collection.aggregate(pipeline))
    for ip in top_ips:
        print("\t{}: {}".format(ip['_id'], ip['count']))
