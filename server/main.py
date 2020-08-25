#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cc
# @Date  :2020-08-21

import json
from bson import json_util, ObjectId

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from pydantic import BaseModel
from pymongo import MongoClient
from werkzeug.security import check_password_hash

from utils import db, tools, redis

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    username: str
    password: str


@app.post("/login/")
def article_list(user: User, response_class=ORJSONResponse):
    [username, passwd] = map(user.dict().get, ['username', 'password'])
    try:
        db_user = db.user.find_one({'username': username})
        assert db_user
        pwhash = db_user['password']
        passwd_check = check_password_hash(pwhash, passwd)
        assert passwd_check
        token = tools.new_token(20)
        uid = str(db_user['_id'])
        redis.set(token, uid)
        return {'ok': True, 'data': {'token': token, 'username': username, 'id': uid}}
    except Exception as e:
        print(e)
        return {'ok': False, 'msg': '用户名或密码错误!'}


class Article(BaseModel):
    title: str
    content: str
    # tag: list


@app.post('/article/new/')
def article_new(article: Article):
    db.article.insert_one(article.dict())
    return article


@app.get('/article/list/')
def article_new():
    a_list = []
    data = db.article.find()
    data = json.loads(json_util.dumps(data))
    return {'articles': data}


@app.delete('/article/del/{id}/')
def article_del(id):
    res = db.article.delete_one({'_id': ObjectId(id)})
    return {'ok': True}


@app.get('/article/detail/{id}/')
def article_new(id):
    a_list = []
    data = db.article.find_one({'_id': ObjectId(id)})
    data = json.loads(json_util.dumps(data))
    return {'article': data}
