# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain="https://www.qiushibaike.com"

    def parse(self, response):
        # print(type(response))
        # selectorList
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        # print(type(contentleft))
        for duanzidiv in duanzidivs:
            # selector
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            content = duanzidiv.xpath(".//div[@class='content']//text()").getall()
            content = "".join(content).strip()
            duanzi = QsbkItem(author=author, content=content)
            yield duanzi

        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain+next_url,callback=self.parse)
