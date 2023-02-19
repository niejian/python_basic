# _*_ utf-8 _*_
# @time: 2023/2/19 
# @author: nj
# @file: 010_函数的定义
# @project: python_basic2

def f1():
    print("函数的定义")


f1()


def add(a, b):
    print('参数 a=%d, b = %d' % (a,b))
    return a + b


print(add(1, 2))

# 关键字传参
print(add(b = 100, a = 1))
# 函数的返回值

a = 1

