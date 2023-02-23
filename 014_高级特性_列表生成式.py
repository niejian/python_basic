# _*_ utf-8 _*_
# @time: 2023/2/23
# @author: nj
# @project: python_basic

# 列表高级特性，列表生成式

l = list(range(1,11))
print(l)

# 将循环出来的x 处理成 x * x得出的结果作为列表l2中的元素
l2 = [x * x for x in range(1, 10)]
print(l2)
# 判断l2中的偶数
l2 = [x * x for  x in range(1, 10) if x % 2 == 0]
print(l2)
# 双层循环，生成全排列
l2 = [m + n for m in 'ABC' for n in 'XYZ']
print(l2)

d = {'x':'A', 'y':'B', 'z':'C'}
l2 = [k +'=' +v for k,v in d.items()]
print(l2)

