# _*_ utf-8 _*_
# @time: 2023/2/20
# @author: nj
# @file: 013_异常.py
# @project: python_basic

# 构造一个异常
"""
try:
    可能出现的异常
expect xxxError:
    提示

"""
try:
    fp = open('test.txt1', 'r')
    fp.read()
except FileNotFoundError:
    print('文件未找到，请检查文件路径')
