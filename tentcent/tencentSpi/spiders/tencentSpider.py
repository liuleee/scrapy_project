# -*- coding: utf-8 -*-
import scrapy
from tencentSpi.items import TentcentItem



class TencentspiderSpider(scrapy.Spider):
    name = "tencentSpider"
    allowed_domains = ["tencent.com"]

    url = "https://hr.tencent.com/position.php?&start="
    offset = 0

    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | tr[@class='odd']"):
            #初始化模型对象
            item = TentcentItem()

            item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['positionLink'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            item['workLocation'] = each.xpath("./td[4]/a/text()").extract()[0]
            item['publishTime'] = each.xpath("./td[5]/a/text()").extract()[0]

            # 数据交给item进行保存
            yield item

        if self.offset < 1680:
            self.offset += 10
        else:
            raise ("结束工作")
        # 请求交给request请求
        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接新的url，并请用回调函数parse
        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)






