# -*- coding: utf-8 -*-

from pymongo import Connection

class DBInterface:
    """Class managing inputs and outputs of lol_db."""
    
    def __init__(self):
        self.connection = Connection()

        self.db = self.connection['lol_stats_db']
        self.collection = self.db['items']

    def insertItem(self, item):
        self.collection.insert(item)
        
    def displayCollection(self):
        l = list(self.collection.find())
        print(l)
        print l[0]["name"]
        
    def getCollection(self):
        return list(self.collection.find())
    
