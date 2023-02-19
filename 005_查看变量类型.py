# _*_ utf-8 _*_
# @time: 2023/2/18 
# @author: nj
# @file: 005_查看变量类型
# @project: python_basic2

"""
使用type查看数据类型
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

print("查看数据类型")
print("name_list", type(name_list))
print("age_tuple", type(age_tuple))
print("person", type(person))

print("name_list数据类型", type(name_list).__name__)
print("age_tuple数据类型", type(age_tuple).__name__)
print("person数据类型", type(person).__name__)