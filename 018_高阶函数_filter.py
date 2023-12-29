# _*_ utf-8 _*_
# @time: 2023/3/5 
# @author: nj
# @file: 018_高阶函数_filter
# @project: python_basic2

# 类似于java8 stream()中的filter()
# 在一个list中，删除偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(is_odd, l)))


# 把数组中的空字符串删掉
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
