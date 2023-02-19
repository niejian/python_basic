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
