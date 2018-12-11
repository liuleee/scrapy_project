# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TentcentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionName = scrapy.Field()
    positionLink = scrapy.Field()
    positionType = scrapy.Field()
    peopleNum = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()
#
# #将数据交给管道处理
# yield item
# #将请求重新发送给调度器如队列，出队列，交给下载器下载
# yield scrapy.Request(url,callback=self.parse)

