# _*_ utf-8 _*_
# @time: 2023/12/30 
# @author: nj
# @file: 026_打印三角形
# @project: python_basic2

for i in range(10):
    if i <= 5:
        print("* " * i)
    else:
        print("* " * (10-i))


# 打印等腰三角形
level = input("请输入层级：")
level = int(level)
while level <= 0:
    print("层级必须大于0")
i = 1
while i <= level:
    # 打印空格 level - i
    print(" " * (level - i), end="")
    print("* " * i)
    i += 1


