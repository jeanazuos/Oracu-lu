# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class MongoDBPipeline(object):

    def __init__(self):

        mongo_collection = 'deal-of-day'
        mongo_uri = '127.0.0.1'
        mongo_db = 'luiza-deal'
        mongo_port = 27017
        mongo_username = 'admin'
        mongo_password = 'admin123'

        self.conn = MongoClient(
            mongo_uri,
            mongo_port,
            username = mongo_username,
            password = mongo_password
        )

        db = self.conn['luiza-deal']
        self.mycol = db[mongo_collection]


    #insert to db
    def set_data(self, item):
        self.mycol.insert(dict(item))

#criar o desconnect do banco

    def process_item(self, item, spider):
        self.set_data(item)
        return item
