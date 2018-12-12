# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ItcastPipeline(object):
    #__init__作为类的初始化方法，可选
    def __init__(self):
        self.filename = open("cz.json", "wb+")

    #用来处理item数据，必写
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False)+"\n"
        self.filename.write(jsontext.encode("utf-8"))
        return item
    #类的结束方法，可选
    def close_spider(self,spider):
        self.filename.close()
