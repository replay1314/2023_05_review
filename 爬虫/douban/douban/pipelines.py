# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanPipeline:
    def process_item(self, item, spider):
        return item


class MySQLPipline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        print('爬虫开始')
        self.conn = pymysql.connect(user='root', password='123456', host='localhost', database='douban')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            sql = f'insert into movies values("{item["title"]}","{item["author"]}","{item["year"]}","{item["score"]}","{item["country"]}","{item["type"]}")'
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.conn.close()
