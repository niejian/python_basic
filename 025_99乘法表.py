# _*_ utf-8 _*_
# @time: 2023/12/30 
# @author: nj
# @file: 025_99乘法表
# @project: python_basic2

data = [1,2,3,4,5,6,7,8,9]
for i in data:
    j = 1
    while j <= i:
        print("%d * %d = %d" % (i, j, i * j), end="\t") # 不换行打印
        j += 1
    print("")

