#!/usr/bin/env python
# coding: utf-8
# cc@2020/08/25
from redis import Redis

conf = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': '5',
    'password': '',
    'decode_responses': True,
}

redis = Redis(**conf)
