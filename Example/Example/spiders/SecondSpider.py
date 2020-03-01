#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 22:28:52 2020

@author: ulhaqi12
"""

import scrapy

from Example.items import NewItem

class SecondSpider(scrapy.Spider):
     name = "SecondSpider"
     allowed_domains = ['www.instagram.com']
     start_urls = ['https://www.instagram.com/explore/tags/fashion/']
     
     def parse(self,response):
         item = NewItem()
         item['main_headline'] = response.xpath('//span/text()').extract()
         item['headline'] = response.xpath('//title/text()').extract()
         item['url'] = response.url
         item['project'] = self.settings.get('BOT_NAME')
         item['spider'] = self.name
         
         return item