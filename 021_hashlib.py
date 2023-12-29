# _*_ utf-8 _*_
# @time: 2023/12/28 
# @author: nj
# @file: 021_hashlib
# @project: python_basic2

import hashlib
# 查看这个包中有多少个方法
print(dir(hashlib))
print('==========================\n')
sha256_hash = hashlib.new('sha256')
sha256_hash.update(b'qq123123')
print(sha256_hash.hexdigest())
print('==========================\n')
md5_hash = hashlib.new('md5')
md5_hash.update(b'qq123123')
# 获取MD5值
print(md5_hash.hexdigest())

