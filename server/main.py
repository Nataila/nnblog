#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cc
# @Date  :2020-08-21

import json
import datetime

from bson import json_util, ObjectId
from typing import List, Union

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from pydantic import BaseModel
from pymongo import MongoClient, DESCENDING
from werkzeug.security import check_password_hash

from utils import db, tools, redis, depends

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
def login(user: User, response_class=ORJSONResponse):
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
    created_at: datetime.datetime = datetime.datetime.now()
    tag: List[Union[str, int]] = []


@app.post('/article/new/')
def article_new(article: Article, user: dict = Depends(depends.token_is_true)):
    db.article.insert_one(article.dict())
    return article


@app.get('/article/list/')
def article_list():
    a_list = []
    data = db.article.find().sort('created_at', -1)
    data = json.loads(json_util.dumps(data))
    return {'articles': data}


@app.delete('/article/del/{id}/')
def article_del(id, user: dict = Depends(depends.token_is_true)):
    res = db.article.delete_one({'_id': ObjectId(id)})
    return {'ok': True}


@app.get('/article/detail/{id}/')
def article_new(id, user: dict = Depends(depends.token_is_true)):
    a_list = []
    data = db.article.find_one({'_id': ObjectId(id)})
    data = json.loads(json_util.dumps(data))
    return {'article': data}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app='main:app', host="0.0.0.0", port=8011, reload=True, debug=True)
