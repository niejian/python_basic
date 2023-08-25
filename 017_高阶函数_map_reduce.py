# _*_ utf-8 _*_
# @time: 2023/2/26 
# @author: nj
# @file: 017_高阶函数_map_reduce
# @project: python_basic2

"""
map: map()函数接收两个参数，一个是函数，一个是iterable；map将传入的函数
依次作用到参数iterable序列中的每个元素，并把结果作为新的iterator（迭代器）返回；
比如我们有一个函数f(x)=x*x，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：

            f(x) = x * x

                  │
                  │
  ┌───┬───┬───┬───┼───┬───┬───┬───┐
  │   │   │   │   │   │   │   │   │
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

[ 1   2   3   4   5   6   7   8   9 ]

  │   │   │   │   │   │   │   │   │
  │   │   │   │   │   │   │   │   │
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

[ 1   4   9  16  25  36  49  64  81 ]
"""


def f(x):
    return x * x


"""
map()传入的第一个参数是函数f，由于结果r是一个iterator，
"""

r = map(f, [x for x in range(10)])
print(r)
print(list(r))

# 将数字列表转换为字符串列表
r2 = map(str, [x for x in range(10)])
print('使用map将数字列表转换为字符串列表: %s' % list(r2))
"""
reduce 用法
reduce()把一个函数作用的序列[x1,x2....xn]上，这个函数必须接收两个参数，
reduce把结果继续和序列上的下一个元素做累积计算；效果如下：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""
print('==============reduce======')
from functools import reduce


def add(x, y):
    return x + y


r = reduce(add, [1, 3, 5, 7, 9])
print(r)


def fn(x, y):
    return x * 10 + y


r = reduce(fn, [1, 3, 5, 7, 9])
print(r)

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return digits[s]


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return digits[s]

    return reduce(fn, map(char2num, s))


print(str2int('13579'))

print('abc'[1:2])


def normalize(name):
    length = len(name)
    if length == 0:
        print('姓名为空')
        return name

    return str(name[0]).upper() + name[1: length]


names = map(normalize, ['adam', 'LISA', 'barT'])
print(list(names))
print('sum求list的和：%d' % sum([1, 3, 5, 7, 8]))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def muti(x, y):
    return x * y


r = reduce(muti, [3, 5, 7, 9])
print(r)
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
print('123.45'[:3])
print('123.45'[4:])
print(str('123.45').index('.'))


def str2float(s):

    def char2num(s):
        index = str(s).index('.')
        numa = s[:index]  # 正整数部分
        numb = s[index + 1:]  # 小数部分
        length = len(numb)
        totalLen = len(s) - 1  # 总位数
        return digits[numa + numb]
    def convert(x, y):

        return x * 10 + y
    print(list(map(char2num(s))))
    return reduce(convert, map(char2num(s)))
print()
r = str2float('123.456')
print("====")
print()
print(r)

