# encoding='utf-8
# @Time: 2023-10-26
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import schedule
import time
import time
# 获取当前时间
# current_time = time.localtime()
# current_hour = current_time.tm_hour
# current_minute = current_time.tm_min
# print("当前时间为：", current_hour, ":", current_minute)
# # 设置目标时间为 10:46
# target_hour = 10
# target_minute = 47
# # 计算需要等待的秒数
# wait_seconds = (target_hour - current_hour) * 3600 + (target_minute - current_minute) * 60
# # 等待到目标时间
# time.sleep(wait_seconds)
# # 在目标时间执行程序
# print("程序已启动！")
import time
def seckill_program():
    # 在这里编写你的秒杀定时程序逻辑
    print("秒杀定时程序已启动！")
    # ...
# 获取当前时间
current_time = time.localtime()
# 设置目标时间为 10:53:00
target_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday, 16, 00, 0, current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst))
# 计算需要等待的秒数
current_timestamp = time.mktime(current_time)
target_timestamp = time.mktime(target_time)
wait_seconds = target_timestamp - current_timestamp
print("等待", wait_seconds, "秒")
# 等待到目标时间
time.sleep(wait_seconds)
# 在目标时间执行秒杀定时程序
seckill_program()
