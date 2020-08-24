#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cc
# @Date  :2020-08-21

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from pymongo import MongoClient


import json
from bson import json_util, ObjectId

MONGO_DB = {'host': '127.0.0.1', 'port': 27017}

client = MongoClient(**MONGO_DB)
db = client['nnblog']
table = db['article']

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def article_list():
    return {"Hello": "World"}


class Article(BaseModel):
    title: str
    content: str
    # tag: list

@app.post('/new/')
def article_new(article:Article):
    table.insert_one(article.dict())
    return article

@app.get('/article/list/')
def article_new():
    a_list = []
    data = table.find()
    data = json.loads(json_util.dumps(data))
    return {'articles': data}

@app.delete('/article/del/{id}/')
def article_del(id):
    res = table.delete_one({'_id': ObjectId(id)})
    print(res)
    return {'ok': True}

@app.get('/article/detail/{id}/')
def article_new(id):
    a_list = []
    data = table.find_one({'_id': ObjectId(id)})
    data = json.loads(json_util.dumps(data))
    return {'article': data}


