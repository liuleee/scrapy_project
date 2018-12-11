# -*- coding:utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem

#创建一个爬虫类
class itcastSpider(scrapy.Spider):

    name = 'itcast'
    #允许爬虫作用的范围
    allow_domains = ['http://www.itcast.cn/']
    #爬虫起始url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#']

    def parse(self, response):
        #通过scrapy自带的xpath匹配出所有来时的根节点列表集合
        teacher_list = response.xpath('//div[@class="li_txt"]')
        #所有老师的列表集合

        #通过根节点集合遍历每项
        for each in teacher_list:
            item = MyspiderItem()
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            teacher_list.append(item)
            yield item










