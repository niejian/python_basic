# _*_ utf-8 _*_
# @time: 2023/12/28 
# @author: nj
# @file: 020_图表
# @project: python_basic2
# 安装包 pip install pyecharts
import pyecharts
from pyecharts.charts import Bar

# 准备数据
x_data = ['一月', '二月', '三月', '四月', '五月', '六月']
y_data = [10, 5, 7, 20, 23, 45]
# 创建柱状图
bar_chart = Bar()
bar_chart.add_xaxis( x_data)
bar_chart.add_yaxis("销售额", y_data)

bar_chart.render()


