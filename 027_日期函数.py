# _*_ utf-8 _*_
# @time: 2024/1/5 
# @author: nj
# @file: 026_日期函数
# @project: python_basic2
import time

from utils.date_utils import *

local_time = time.localtime(time.time())
print(f"本地时间为：{local_time}")
# 本地时间为：time.struct_time(tm_year=2024, tm_mon=1, tm_mday=5, tm_hour=10, tm_min=4, tm_sec=58, tm_wday=4, tm_yday=5, tm_isdst=0)
# 格式化时间
local_time = time.asctime(time.localtime(time.time()))
print(f"本地时间为：{local_time}") # 本地时间为：Fri Jan  5 10:06:29 2024
# yyyy-MM-dd HH:mm:ss
date_time_formatter = "%Y-%m-%d %H:%M:%S"
# 格式化本地时间
local_time = time.strftime(date_time_formatter, time.localtime())
print(local_time) # 2024-01-05 10:11:26

# 将字符串转换为日期 time 类型
data_time_str = "2024-01-05 10:11:26"
date_time = time.strptime(data_time_str, date_time_formatter)
print(f"字符串转time类型：{date_time}")
print(time.strftime(date_time_formatter, date_time))


# 获取时间戳，精确到秒
timestamp_sec = time.mktime(time.localtime())

print(f"当前时间戳: {timestamp_sec}")

# 自定义包引入使用
# 格式化时间
date_time_str = format_time_str(date_time_formatter_day, time.localtime())
print(date_time_str)
date_time_str = format_time_str(date_time_formatter_second, time.localtime())
print(date_time_str)
# 字符串转time类型
date_time = format_str_time(date_time_formatter_second, "2024-01-05 10:41:51")
print(f"字符串转time类型：{date_time}")
# 获取时间戳
sec = get_timestamp(date_time_formatter_second,"2024-01-05 10:45:44" )
print(f"时间戳: {sec}")

# 获取某月日历



