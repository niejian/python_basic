# _*_ utf-8 _*_
# @time: 2023/12/31 
# @author: nj
# @file: 字符串的操作
# @project: python_basic2

s = "hello myname is jim, and i am very happy to be here"
# 切片
print(s[1:3])
# 字符串的基本操作
print(s.center(50, "-"))
print(s.find("iss")) # -1表示没找到吗，找到了返回所查字符的索引
print("22".isdigit()) # 判断是否是整数

l = ['a', 'b', 'c']
# 将数组通过字符链接成字符串
print("-".join(l)) # a-b-c
print("".join(l)) # abc
# 替换
print(s.replace("h", "a"))
print(s.replace("h", "a", 1)) # 替换一次
# split, 将字符串转换为列表；默认分割字符是空格
print(s.split())
