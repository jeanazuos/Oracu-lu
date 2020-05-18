# -*- coding: utf-8 -*-

from pymongo import MongoClient
import os

class MongoDBPipeline(object):

    mongo_collection_name = os.environ.get('MONGO_COLLECTION')
    mongo_uri = os.environ.get('MONGO_URI')
    mongo_db = os.environ.get('MONGO_DATABASE')
    mongo_port = int(os.environ.get('MONGO_PORT'))
    mongo_user = os.environ.get('MONGO_USER')
    mongo_pass = os.environ.get('MONGO_PASS')

    def __init__(self):
        pass

    def open_spider(self, spider):
        self.client = MongoClient(
            self.mongo_uri,
            self.mongo_port,
            username = self.mongo_user,
            password = self.mongo_pass
        )
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.set_data(item)
        return item
  
    def set_data(self, item):
        self.db[self.mongo_collection_name].insert(dict(item))