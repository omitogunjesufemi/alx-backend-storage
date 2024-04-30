#!/usr/bin/env python3
"""
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
