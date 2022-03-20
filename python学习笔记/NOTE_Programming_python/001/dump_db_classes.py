#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :dump_db_classes.py
@邮箱    :lcmg.sty@gmail.com
@时间    :2022/03/19 16:45:17
@作者    :lcmg_STY
@版本    :1.0
'''
import shelve
db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n  ', db[key].name, db[key].pay)

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())
