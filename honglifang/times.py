# encoding='utf-8
# @Time: 2023-10-28
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import time
import argparse
import ast
# 创建参数解析器
# import ast
# def convert_to_dict(string):
#     try:
#         dictionary = ast.literal_eval(string)
#         if isinstance(dictionary, dict):
#             return dictionary
#         else:
#             raise ValueError('提供的字符串不是一个有效的字典格式。')
#     except SyntaxError:
#         raise ValueError('提供的字符串不是一个有效的字典格式。')
# string = "{'http': 'http://221.229.53.141:6727', 'https': 'https://221.229.53.141:6727'}"
# proxies = convert_to_dict(string)
# print(proxies)

def GetSleepTimeSecend(hour, minute, second):
    current_time = time.localtime()
    # 设置目标时间为 10:53:00
    target_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,

                                   hour, minute, second, current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst))
    # 计算需要等待的秒数
    current_timestamp = time.mktime(current_time)
    target_timestamp = time.mktime(target_time)
    wait_seconds = target_timestamp - current_timestamp
    print("等待", wait_seconds, "秒")
    return wait_seconds


time.sleep(GetSleepTimeSecend(15, 59, 35))

