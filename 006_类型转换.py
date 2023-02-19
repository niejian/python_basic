# _*_ utf-8 _*_
# @time: 2023/2/18 
# @author: nj
# @file: 006_类型转换
# @project: python_basic2

# 转换为整型
# str -> int
a = "123"
print(type(a))
b = int(a)
print(type(b))

# float -> int
c = 1.23
print(type(c))
d = int(c)
print("float -> int 结果", d)

# 转换为浮点数
# str -> float
a = "1.23"
b = float(a)
print(b)

# 转成字符串
a = 1.23
b = 1
c = str(a) + str(b)
print(c)
