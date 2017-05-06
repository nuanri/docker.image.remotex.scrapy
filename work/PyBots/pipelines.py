# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests


class PybotsPipeline(object):

    def __init__(self):
        self.headers = {
            'authorization': 'Basic ' + os.environ.get('API_KEY'),
            'Content-Type': 'application/json',
            'cache-contro': 'no-cache',
        }
        self.url = os.environ.get('API_PREFIX') + '/spider/jobx/job'

    def process_item(self, item, spider):
        res = requests.post(self.url, headers=self.headers, json=dict(item))
        if res.status_code != 200:
            print(res.text)
