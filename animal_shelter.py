#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:56:25 2021

@author: 0953859_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""
    
    def __init__(self, username, password):
        #Initializing the MongoClient. This helps to
        #access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:43314/AAC' % (username, password))
        self.database = self.client['AAC']
        
        
#Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            #try to insert data, return true if done, return false if not
            try:
                self.database.animals.insert(data) #data should be dictionary
                return True
            except:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
#Create method to implement the R in CRUD
    def read(self, criteria=None):
        #if criteria is not None then this query will find and return all rows which match the criteria
        if criteria is not None:
            data = self.database.animals.find(criteria)
        else:
            raise Exception("Nothing to read, because criteria parameter is empty")
        return data
    def readAll(self, criteria=None):
        #query for retrieving all data from db
        try:
            data = self.database.animals.find(criteria, {"_id":False})
        except:
            raise Exception("Unsuccessful Retrieval")
        return data
#Create method to implement U in CRUD.
    def update(self, query, updated):
        #if either query or updated parameters are empty, throw error
        if query and updated is not None:
            try: 
                updated_data = self.database.animals.update(query, updated)
            except:
                raise Exception("Update unsuccessful")
        else:
            raise Exception("Nothing to update, because query and or update parameter is empty")
        return dumps(updated_data)
#Create method to implement the D in CRUD.
    def delete(self, criteria):
        #check if there is criteria to delete, otherwise raise exception
        if criteria is not None:
            #try to delete, raise exception if unsuccessful
            try:
                result = self.database.animals.remove(criteria) #data should be dictionary
            except:
                raise Exception("Delete unsuccessful")
        else:
            raise Exception("Nothing to delete, because criteria is empty")
        return dumps(result)