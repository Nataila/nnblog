#!/usr/bin/env python
# coding: utf-8
# cc@2020/08/25

from pymongo import MongoClient

MONGO_DB = {'host': '127.0.0.1', 'port': 27017}

client = MongoClient(**MONGO_DB)
db = client['nnblog']
