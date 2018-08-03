# -*- coding: utf-8 -*-
# @Time    : 2018.8.3 15:57
# @Author  : Hofer

from pymongo import MongoClient
import os

IP = os.environ["ip"]
print(IP)
PORT = os.environ["port"]
# PROJECT_KEY = os.environ["PROJECT_KEY"]

# client = MongoClient('10.10.62.146', 27017)
client = MongoClient('%s'%(IP), PORT)

# 连接mydb数据库,账号密码认证
db = client.axdoc
db.authenticate("dev", "9kC95[yadYxKy")

account = db.account
a = account.find_one({'mobile': '15811210028'})

print(a)

# for i in a:
#     print(i)

