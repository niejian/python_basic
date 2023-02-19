# _*_ utf-8 _*_
# @time: 2023/2/18 
# @author: nj
# @file: 008_for循环
# @project: python_basic2

s = 'china'
for i in s:
    print(i)

# 使用range
for i in range(5):
    print('range: %d' % i)

# 使用range，从某个下标开始
for i in range(1, 5):
    print("range指定起始范围：%d" % i)

# 使用range，取某些值
for i in range(1, 6, 4):
    print(i)
# 使用下标趣元素
a_list = ['a', 'b', 'c']
length = len(a_list)
for index in range(length):
    print('index: %d, value: %s' % (index, a_list[index]))
