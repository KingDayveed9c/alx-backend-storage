#!/usr/bin/env python3
"""
Task 10 change school topics
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
