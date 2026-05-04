#!/usr/bin/env python3
""" Lists all documents in a collection """

def list_all(mongo_collection):
    """ Return list of all documents or empty list """
    return list(mongo_collection.find())
