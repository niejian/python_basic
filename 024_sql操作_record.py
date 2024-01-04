# _*_ utf-8 _*_
# @time: 2023/12/29 
# @author: nj
# @file: 024_sql操作_record
# @project: python_basic2
import pymysql
import records
pymysql.install_as_MySQLdb()

db = records.Database('mysql://root:123456@localhost:3306/test?charset=utf8mb4')
rows = db.query("select * from admin")
# 获取所有结果
for row in rows:
    print(row)
# 读取字段内容
print(rows[0][0])
# print(rows[0].get('username'))
# 按条件查询
# params = 1
db.get_table_names()
admin = {"id": 1}
rows = db.query('id = :id', params=1)
for row in rows:
    print(row)



