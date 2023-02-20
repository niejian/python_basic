# _*_ utf-8 _*_
# @time: 2023/2/20
# @author: nj
# @file: 012_序列化与反序列化.py
# @project: python_basic

fp = open('test.txt', 'w')
# 定义一个列表
name_list = ['zs', 'lisi']

import json
# 序列化,将python列表转为json字符串，否则无法直降将对象写入文件
names = json.dumps(name_list)
print(names)
fp.write(names)
fp.close()

fp = open('test.txt', 'w')
# dump 将某个对象写入到句柄中
json.dump(name_list, fp)
fp.close()

# 将json对象转换为python对象
fp = open('test.txt', 'r')

content = fp.read()
# json -> python obj
load = json.loads(content)
print(type(content))
print(content)
print(type(load))
print(load)

