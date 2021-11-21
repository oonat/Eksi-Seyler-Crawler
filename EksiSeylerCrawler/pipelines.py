# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class EksiseylercrawlerPipeline:
    def process_item(self, item, spider):
        return item


from .models import session, Entry, create_tables

class DatabasePipeline(object):
    def __init__(self):
        create_tables()
    
    def process_item(self, item, spider):
        entry = Entry(**item)
        try:
            session.add(entry)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item