# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class MongoDBPipeline(object):
    collection_name = 'deal-of-day'
    def __init__(self):

        mongo_collection = 'deal-of-day'
        mongo_uri = '127.0.0.1'
        mongo_db = 'luiza-deal'
        mongo_port = 27017
        mongo_username = 'admin'
        mongo_password = 'admin123'

    def open_spider(self, spider):
        self.client = MongoClient(
            '127.0.0.1',
            27017,
            username = 'admin',
            password = 'admin123'
        )
        self.db = self.client['luiza-deal']
    


    #insert to db
    def set_data(self, item):
        self.db[self.collection_name].insert(dict(item))
        # self.mycol.insert(dict(item))

#criar o desconnect do banco

    def process_item(self, item, spider):
        self.set_data(item)
        return item
