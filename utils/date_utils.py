# _*_ utf-8 _*_
# @time: 2024/1/5
# @author: nj
# @file: date_utils
# @project: python_basic2
import time

# 年月日时分秒格式化字符串
date_time_formatter_second = "%Y-%m-%d %H:%M:%S"
# 年月日格式化字符串
date_time_formatter_day = "%Y-%m-%d"

"""
字符串时间类型根据格式化字符串转time类型
"""
def format_str_time(formatter, date_time_str):
    return time.strptime(date_time_str, formatter)

"""
将time类型按格式字符串转换为字符串
"""
def format_time_str(formatter, localtime):
    return time.strftime(formatter, localtime)

"""
获取时间戳, 秒
"""
def get_timestamp(formatter, date_time_str):
    localtime = format_str_time(formatter, date_time_str)
    return time.mktime(localtime)