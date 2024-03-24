#!/usr/bin/env python3
"""
to change school topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    to update many rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
