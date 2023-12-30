# _*_ utf-8 _*_
# @time: 2023/2/18 
# @author: nj
# @file: 007_输入输出
# @project: python_basic2

# 格式化输出
print('-----格式化输出-----')
name = 'tom'
age = 18
print('名字：%s, 年龄：%d' % (name, age))

# 输出，使用input()
print('-----输出-----')
password = input('请输入密码: \n')
print('密码是：%s' % password)

# 将字符串写入到文件中
# 打开文件
tmp_file = "./foo.txt"
f = open("tmp_file", "w")
f.write("hello world \n python")
# 关闭文件
f.close()
# 文件对象的方法，读文件
f = open(tmp_file, "r")
content = f.read()
print("读取文件====>")
print(content)
f.close()
# 读第一行
f = open(tmp_file, "r")

line = f.readline()
print("读一行数据======>")
print(line)
f.close()

# 返回文件中的所有行数据
f = open(tmp_file, "r")

lines = f.readlines()
print("返回文件中的所有行数据======>")
print(lines)
f.close()
# 使用循环的方式读取所有行数据
f = open(tmp_file, "r")
for line in f:
    print(line, end='')

f.close()
# f.tell() 当前文件指针所在的位置
f = open(tmp_file, "r")
f.read(2)
print(f.tell())
f.close()

'''
f.seek()
如果要改变文件指针当前的位置, 可以使用 f.seek(offset, from_what) 函数。

from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：

seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
'''
f = open(tmp_file, "r")
# 移动到文件的第2个字节
f.seek(1)
# 移动指针后，读取第一个字符
print(f.read(12))
f.close()
# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:
with open(tmp_file, 'r') as f:
    data = f.read()
    print("读取文件：%s" % (data))
f.close()

