#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:45:23 2020

@author: ulhaqi12
"""

import scrapy

from Example.items import MovieItem

class ThirdSpider(scrapy.Spider):
    name = 'ThirdSpider'
    allowed_domains = ["imdb.com"]
    start_urls = ['https://www.imdb.com/chart/top/']
    
    def parse(self, response):
         links = response.xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td[2]/a/@href').extract()
         i=1;
         for link in links:
             abs_url = response.urljoin(link)
             url_next = '//*[@id="main"]/div/span/div/div/div[2]/table/tbody/tr['+str(i)+']/td[3]/strong/text()'
             rating = response.xpath(url_next).extract()
             if(i<=len(links)):
                 i+=1
                 yield scrapy.Request(abs_url,callback=self.parse_indetail,meta = {'rating' : rating})
                
    def parse_indetail(self, response):
        item = MovieItem()
        item['title'] = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/h1/text()').extract()
        item['directors'] = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[2]/a/text()').extract()
        item['writers'] = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[3]/text()').extract()
        item['stars'] = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[4]/text()').extract()
        item['popularity'] = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[3]/div[5]/div[2]/div[2]/span/text()[1]').extract()
        
        return item
    