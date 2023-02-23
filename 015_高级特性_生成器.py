# _*_ utf-8 _*_
# @time: 2023/2/23
# @author: nj
# @file: 015_高级特性_生成器.py
# @project: python_basic

"""
通过列表生成式，可以直接创建一个列表
如果列表中的某个元素是根据某种算法推算而来的，那我们是否可以在循环的过程中根据规律推算出后续袁术
而不用创建完整的list，从而节省空间。在python中，这种一边循环一边计算的机制，称为generator
"""
# 创建一个generator
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))

def fib(max):
    n,a,b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'

fib(10)


"""
如果一个函数定义中包含yield关键字，
那么这个函数就不再是一个普通函数，
而是一个generator函数，
调用一个generator函数将返回一个generator：
"""


# 定义一个偶数
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


print(odd()) # <generator object odd at 0x10812f1d0>
# 三次都是打印step1
# 上述代码实际上创建了3个完全独立的generator，对3个generator分别调用next()当然每个都会返回第一个值。
print(next(odd()))
print(next(odd()))
print(next(odd()))


g = odd()
print(next(g))
print(next(g))
print(next(g))


def triangles(n):
    if n <= 0:
        print('请输入大于o的正整数')
        exit(0)
    index = 0





