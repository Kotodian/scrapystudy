# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        # print(type(response))
        #selectorList
        duanzidivs=response.xpath("//div[@id='content-left']/div")
        #print(type(contentleft))
        for duanzidiv in duanzidivs:
            #selector
            author=duanzidiv.xpath(".//h2/text()").get().strip()
            content=duanzidiv.xpath(".//div[@class='content']//text()").getall()
            content="".join(content).strip()
            print(content)
            pass