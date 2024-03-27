#!/usr/bin/env python3
"""Module contains a func that list topic of schools"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    return mongo_collection.find({"topics": topic})
