# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Questions:
# 1. How to create multiple collections in a database?
# Solution: Create another class pipeline to handle another table
# Reference: https://stackoverflow.com/questions/19653963/use-different-collections-in-mongodb-depending-on-item-type
# 2. How to only store unique quotes? Prevent duplicate entries upon multiple runs


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class TutorialPipeline:
    def __init__(self):
        # Initialize Connection to localhost at port 27107
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        # Create db called myquotes
        db = self.conn['myquotes']
        # Create table or collection
        self.collection = db['quotes_tb']

    def process_item(self, item, spider):
        # Store item to table
        self.collection.insert(dict(item))
        return item
