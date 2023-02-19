# _*_ utf-8 _*_
# @time: 2023/2/19 
# @author: nj
# @file: 009_切片
# @project: python_basic2
# 所谓切片就是对某个对象（string，list、tuple）整体做的部分操作

s = 'hello world'
# 切片
s1 = s[0]
print(s1)
# 从其实位置开始切片, 从下标为1的位置开始
s2 = s[1:]
print(s2)
s3 = s[:3]
print(s3)
# 截取指定长度, 从下标为2->下标为6截取两个字符、
s4 = s[1:6:2]
print(s4)
