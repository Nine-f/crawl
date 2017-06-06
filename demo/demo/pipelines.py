# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class DemoPipeline(object):
#     def process_item(self, item, spider):
#         return item

import json


class JsonWritePipeline(object):
    def __init__(self):
        self.file = open('item.jl', 'wb')

    def process_item(self,item,spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item
