# _*_ utf-8 _*_
# @time: 2023/12/30 
# @author: nj
# @file: 年会抽奖
# @project: python_basic2
'''
300个员工抽奖，
一等奖：5名
二等奖：10名
三等奖：30名
抽奖顺序为三等奖、二等奖、一等奖；每人最多只能中一次奖

'''
import random
import string


# 初始化300名员工
def get_emps(count):
    emps = []
    for i in range(count):
        # emp_name = random.choice(string.ascii_lowercase)
        emp_name = "".join(random.sample(string.ascii_lowercase, 3))
        count = emps.count(emp_name)
        while count >= 1:
            emp_name = "".join(random.sample(string.ascii_lowercase, 3))
            count = emps.count(emp_name)
        emps.append(emp_name)

    return emps

# 抽奖
def do_lottery(lottery_level, bonus_count, emps):
    print(f"开始抽{lottery_level}等奖，中奖人数：{bonus_count}.....")
    # 参与抽奖员工列表人数
    emp_count = len(emps)
    # 复制一个员工数组
    lottery_emps = emps

    # 生成随机数，这个随机数就是中奖人的下标。
    lottery_index_list = random.sample(range(emp_count), bonus_count)
    i = 0
    # 倒序一下，再删除
    lottery_index_list.sort(reverse=True)
    print(lottery_index_list)
    # while i < bonus_count:
    #     index = lottery_index_list[i]
    #     print(f"{index}, 恭喜:{lottery_emps[index]}, 中 {lottery_level}等奖")
    #     del lottery_emps[index]
    #     i += 1
    # return lottery_emps
    for i in lottery_index_list:
        index = i - 1
        print(f"{index}, 恭喜:{lottery_emps[index]}, 中 {lottery_level}等奖")
        del lottery_emps[index]
    return lottery_emps

emps = get_emps(300)

print("开始抽三等奖，中奖名单....")
emps = do_lottery("三", 30, emps)
print("开始抽二等奖，中奖名单....")
emps = do_lottery("二", 10, emps)
print("开始抽二等奖，中奖名单....")
emps = do_lottery("一", 5, emps)

