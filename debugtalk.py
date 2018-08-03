# -*- coding: utf-8 -*-
# @Time    : 2018.8.3 15:57
# @Author  : Hofer

from pymongo import MongoClient
import os

# IP = os.environ["ip"]
# PORT = os.environ["port"]
# PROJECT_KEY = os.environ["PROJECT_KEY"]

client = MongoClient('10.10.62.146', 27017)
print(client.list_database_names())

