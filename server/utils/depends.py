#!/usr/bin/env python
# coding: utf-8
# cc@2020/08/25

from bson import ObjectId

from fastapi import Header

from .db import db
from .redis_db import redis

async def token_is_true(token: str = Header(..., description="token验证")):
    uid = redis.get(token)
    if not uid:
        raise HTTPException(
            status_code=401,
            detail='Authorization Failed'
        )
    user = db.user.find_one({'_id': ObjectId(uid)})
    return user

