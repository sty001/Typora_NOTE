#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :dump_db_file.py
@邮箱    :lcmg.sty@gmail.com
@时间    :2022/03/19 16:45:49
@作者    :lcmg_STY
@版本    :1.0
'''
from make_db_file import loadDbase
db = loadDbase()
for key in db:
    print(key, '=>\n  ', db[key])
print(db['sue']['name'])
