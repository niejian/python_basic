# _*_ utf-8 _*_
# @time: 2023/12/30 
# @author: nj
# @file: 摇号小程序
# @project: python_basic2
'''
需求
1、用户最多选3次
2、每次放出20个车牌供用户选择
3、车牌规则：京[a-Z]-[xxxxxx]
'''
import string
import random


def get_car_no():
    # 生成号码随机数
    ran_str = string.digits + string.ascii_uppercase
    # print(ran_str)
    # 从随机数获取6位作为车牌号 random.sample 返回的数组
    num = random.sample(ran_str, 6)
    # random.sample 返回的数组，通过join来将数组转成字符串
    num = "".join(num)

    # 归属地
    # location = "".join(random.sample(string.ascii_uppercase, 1))
    location = random.choice(string.ascii_uppercase)
    num = "京" + location + " " + num

    return num

def gen_no():
    i = 1
    car_nums = []
    while i <= 20:
        car_no = get_car_no()
        car_nums.append(car_no)
        print(car_no, end="\t")
        if i % 5 == 0:
            print("")
        i += 1
    return car_nums

#生成编码
car_nums = gen_no()

def choice_car_num(count):
    choice = input("请输入车牌号....")

    if choice in car_nums:
        print(f"恭喜您选择了车牌号：{choice}")
        exit("good luck")
    else:
        count += 1
        if count > 3:
            exit(f"最多选3次，您已经选了{count}次")
        print(f"选择不合法, 请进行第{count}次选择")
        choice_car_num(count)

choice_car_num(1)


