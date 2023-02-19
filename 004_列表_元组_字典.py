# _*_ utf-8 _*_
# @time: 2023/2/18 
# @author: nj
# @file: 004_列表_元组_字典
# @project: python_basic2

"""
list    列表
tuple   元组
dict    字典
"""

# 列表
name_list = ["zhangsan", "lisi", "wangwu"]
print(name_list)
name_list1 = name_list
name_list1[0] = "张三"
print(name_list)
print(name_list1)

# 元组
age_tuple = (18,19,20)
print(age_tuple)
age_tuple2 = age_tuple
# age_tuple[0] = 180
print(age_tuple)
print(age_tuple2)

# 字段
person = {"name": "zhangsan", "age": 18}
print(person)
person.get("23")
print(person.get("name"))