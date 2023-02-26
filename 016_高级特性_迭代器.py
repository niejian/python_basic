# _*_ utf-8 _*_
# @time: 2023/2/26 
# @author: nj
# @file: 016_高级特性_迭代器
# @project: python_basic2

"""
迭代器的类型：
1、 集合类型：list tuple，dict、set、str
2、generator类型；包括range，带yield的genetor function

这些类型可以统称为iterable
可以使用 isinstance() 来判断该对象是否是iterable对象
"""

from collections.abc import Iterable
print("使用函数isinstance()函数来判断对象是否是iterable")
print("[]列表是否是iterable对象：%s" % isinstance([], Iterable))
print("{} 字典是否是iterable对象：%s" % isinstance({}, Iterable))
print("字典是否是iterable对象：%s" % isinstance('abc', Iterable))
# 实质上，g只是个列表
g = [x * x for x in range(1,10)]
print("generator是否是iterable对象：%s" % isinstance(g, Iterable))
print("数字是否是iterable对象：%s" % isinstance(10, Iterable))

# 以上说的可迭代对象，下面要说的是迭代器；需要区分一下
# 可以被next()函数调用并不断返回下一个值的对象统称为 迭代器（iterator）
# 判断对象是否为迭代器
print("================迭代器（iterator）的判断==================")
from collections.abc import Iterator
g = [x * x for x in range(1,10)]

print('generator是否是迭代器：%s' % isinstance(g, Iterator))
g2 = (x for x in range(10))
print(isinstance((x for x in range(10)), Iterator))
print('列表是否是迭代器：%s' % isinstance([], Iterator))
print('字典是否是迭代器：%s' % isinstance({}, Iterator))
print('字符串是否是迭代器：%s' % isinstance('abc', Iterator))
print('元组是否是迭代器：%s' % isinstance((), Iterator))
#  将 list，dict、str对象iterable变为迭代器，可以使用 iter()函数
print('iter(列表)是否是迭代器：%s' % isinstance(iter([]), Iterator))
print('iter(字典)是否是迭代器：%s' % isinstance(iter({}), Iterator))
print('iter(字符串)是否是迭代器：%s' % isinstance(iter('abc'), Iterator))
print('iter(元组)是否是迭代器：%s' % isinstance(iter(()), Iterator))


