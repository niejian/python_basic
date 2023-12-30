# _*_ utf-8 _*_
# @time: 2023/12/30 
# @author: nj
# @file: 随机数
# @project: python_basic2
import random
import string

dir(random)
# 随机选择一个字符
print(random.choice("abcdef"))
# 答应一个字符
print(random.randint(9, 10))
# 随机找n个值
nums = range(1, 10)
print(random.sample(nums, 3))

print(string.ascii_lowercase)
print(string.ascii_uppercase)
# 打印数字
print(string.digits)
# 取数范围 [9,10]
print(random.randint(9, 10))
# 取数范围 [9,10)
print(random.randrange(9, 10))
