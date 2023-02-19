# _*_ utf-8 _*_
# @time: 2023/2/19 
# @author: nj
# @file: 011_文件操作
# @project: python_basic2

# 文件操作相关api, 如果文件存在，则会先删除再写入
f = open('test.txt', 'w')
f.write('hello world\n')
f.close()
# 写文件，住家 mode = a
f = open('test.txt', 'a')
f.write('hello world \n')
f.write('hello world \n')
f.write('hello world \n')
# # 读文件
fp = open('test.txt', 'r')
# 一个一个字节的读取
content = fp.read()
print(content)
fp.close()
# 行读取
fp = open('test.txt', 'r')
readline = fp.readline()
print('=====readline=====')
print(readline)
fp.close()
# 读取多行
fp = open('test.txt', 'r')
print('=====readlines=====')
readlines = fp.readlines()
print(readlines)
fp.close()



