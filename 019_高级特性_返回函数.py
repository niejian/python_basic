# _*_ utf-8 _*_
# @time: 2023/3/22 
# @author: nj
# @file: 019_返回函数
# @project: python_basic2

"""函数作为返回值"""
def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax

# 将函数作为返回值


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

# 调用
f = lazy_sum(1, 3, 5, 7)
print(f)
print('求和结果：%d' % f())
# 函数lazy_sum里面定了了子函数sum；像这种内部函数引用了外部的参数变量，相关参数和变量都保存在返回的函数中，称为闭包
"""
闭包
"""
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

# f1 = count()
f1, f2, f3s = count()
print(f1())
print(f2())
print(f3s())


