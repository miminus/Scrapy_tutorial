# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb.cursors
import scrapy
from scrapy.contrib import spiderstate
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import settings

class Mysql_scrapy_pipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool(
                                    dbapiName='MySQLdb',
                                    host=settings.DB_HOST,
                                    db=settings.DB,
                                    user=settings.DB_NAME,
                                    passwd=settings.DB_PASSWD,
                                    cursorclass= MySQLdb.cursors.DictCursor,
                                    charset = 'utf8',
                                    use_unicode = False
                                    )
        
    def process_item(self,item,spider):
        self.dbpool.runInteraction(self._conditional_insert,item)

        return item    
        
    def _conditional_insert(self,tx,item):  
#         raw_input('input:____________________________________')
        sql = 'insert into post (id , url , board , title , post_time, scratch_time ,language_type, content ,thread_content) values (%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE post_time=%s  '
        param = (item['topic_url'], item['topic_url'], item['topic_channel'] ,item['topic_title'], item['topic_post_time'],item['scratch_time'] ,0,item['topic_content'],item['thread_content'],item['topic_post_time'])
        tx.execute(sql,param) 
        
        
        
        
        