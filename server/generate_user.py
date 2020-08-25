#!/usr/bin/env python
# coding: utf-8
# cc@2020/08/25

import argparse
import getpass

from pymongo import MongoClient
from werkzeug.security import generate_password_hash

MONGO_DB = {'host': '127.0.0.1', 'port': 27017}

client = MongoClient(**MONGO_DB)
db = client['nnblog']


def main():
    ''' 创建用户 '''
    parser = argparse.ArgumentParser(description='generate user')
    parser.add_argument('--username', type=str, required=True, help='Name for User')
    args = parser.parse_args()
    username = args.username
    user = db.user.find_one({'username': username}, {'_id': 1})
    if user:
        return print(f'Error: username {username} is already exists!')

    password = getpass.getpass()
    password2 = getpass.getpass('Password (again): ')
    if password != password2:
        return print("Error: Your passwords didn't match.")
    if password.strip() == '':
        return print("Error: Blank passwords aren't allowed.")

    encrypt_passwd = generate_password_hash(password)
    db.user.insert_one({'username': username, 'password': encrypt_passwd})


if __name__ == "__main__":
    main()
