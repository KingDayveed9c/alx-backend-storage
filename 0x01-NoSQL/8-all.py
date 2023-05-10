#!/usr/bin/env python3
"""
This is a module that has a utility function that lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    list all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
