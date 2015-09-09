#coding:utf-8
'''
Created on 2015年9月8日

@author: MINUS
'''
from scrapy import log
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
from scrapy.utils.project import get_project_settings

from XinLang_news.spiders.gundongnews import GundongnewsSpider



spider = GundongnewsSpider()
settings = get_project_settings()
crawler = Crawler(settings)
crawler.configure()
crawler.crawl(spider)
crawler.start()

log.start()
reactor.run()
