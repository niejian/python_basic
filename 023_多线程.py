# _*_ utf-8 _*_
# @time: 2023/12/29 
# @author: nj
# @file: 023_多线程
# @project: python_basic2
import threading
import time
import _thread

from utils.date_utils import format_time_str, date_time_formatter_second


# 为线程定义一个函数
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s:%s" % (thread_name, time.ctime(time.time())))

# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("thread-1", 2, ))
    _thread.start_new_thread(print_time, ("thread-2", 4, ))
except:
    print("error: unable start thread")

# while 1:
#     pass


exitFlag = 0

class my_thread(threading.Thread):
    def __init__(self, thread_id, name, delay):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.delay = delay

    def run(self):
        print(f"开始线程：{self.name}, id: {self.thread_id}")
        print_time(self.name, self.delay, 5)
        print(f"退出线程：{self.name}")

def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            thread_name.exit()
        time.sleep(delay)
        print(f"{thread_name}, {format_time_str(date_time_formatter_second, time.localtime())} \n")
        counter -= 1

# 创建线程
thread_1 = my_thread(1, "thread-1", 1)
thread_2 = my_thread(2, "thread-2", 2)
# 开启线程
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
print("退出主线程")















