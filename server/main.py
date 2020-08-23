#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cc
# @Date  :2020-08-21

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

app = FastAPI()

origins = [
    'http://192.168.0.108:3000',
    'http://mac.com:3000',
]

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

@app.post('/new')
def article_new(article:Article):
    return article
