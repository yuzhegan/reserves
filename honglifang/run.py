# encoding='utf-8

# @Time: 2023-10-26
# @File: %
#!/usr/bin/env
import time
from Proxy_JiGuang import Proxy_JiGuang
from icecream import ic
import os
import random


from multiprocessing import Process
import subprocess

# script_path = os.path.join(os.path.dirname(__file__), 'demo2.py')


def run_script(arguments):
    # 在这里执行脚本的代码，使用传递的参数param
    script_path = './honglifang/demo.py'
    # arguments = ['-u', 'yuzhe', '-p', '123456', '-d', '2024-11-03', '-a', '下午场一']

    subprocess.call(['python', script_path] + arguments)


# # 参数列表
params1 = ['-u', '18466183411 ', '-p', 'a376122', '-d', '2023-12-09', '-a', '上午'] # 两个一小
params2 = ['-u', '18466220549', '-p', 'kjg456', '-d', '2023-12-09', '-a', '下午场一'] # 两个一小
params3 = ['-u', '19902893703', '-p', 'aaa234', '-d', '2023-12-09', '-a', '下午场二'] # 两个一小
params4 = ['-u', '18466195967', '-p', 'hlf666', '-d', '2023-12-09', '-a', '上午'] # 两个2小
# params5 = ['-u', '18720600577', '-p', 'hlf4210', '-d', '2023-11-04', '-a', '下午场一'] # 两个2小
# params6 = ['-u', '18974573951', '-p', 'hlf123', '-d', '2023-11-04', '-a', '下午场二']  # 两个2小
# params7 = ['-u', '18172856581', '-p', 'wq6666', '-d', '2023-11-04', '-a', '晚上']  # 两个2小
# params1 = ['-u', '15707974367', '-p', 'ccc123','-d', '2023-11-18', '-a', '上午']  # 两个一小
# params2 = ['-u', '18870011708', '-p', 'sb123456','-d', '2023-11-18', '-a', '下午场一']  # 两个一小
params = [params1, params2, params3, params4]
# params = [params6]
# print(params)
#
# 创建进程列表
processes = []



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

def GenJdIps():
    proxy = Proxy_JiGuang()
    proxy.SetLocalIp2WhiteList()
    ips = proxy.GenJG_Proxy_IPs()
    ic(ips)
    return ips

# 提前1分钟请求下来代理ip 代理ip可以用1-2分钟
time.sleep(GetSleepTimeSecend(15, 58, 35))

for i in range(3):
    try:
        ips = GenJdIps()
        for param in params:
            ip = random.choice(ips)
            proxies = {
                "http": "http://" + str(ip['ip'])+':'+str(ip['port']),
                "https": "https://" + str(ip['ip'])+':'+str(ip['port']),
            }
            # proxies = convert_to_dict(str(proxies))
            param.append('-x')
            param.append(str(proxies))
        break
    except Exception as e:
        time.sleep(5)
        ic(e)

import datetime
current_time = datetime.datetime.now().strftime('%H:%M:%S')
print(current_time)


# 等待到16：00：00 开始执行抢票
# 申请完代理看下时间有么有到16点 提前一秒登陆，保证成功率
current_hour = time.localtime().tm_hour
if current_hour < 16:
    time.sleep(GetSleepTimeSecend(15, 59, 59))

for i in range(1):
    try:
        # 创建并启动进程
        for param in params:
            p = Process(target=run_script, args=(param,))
            p.start()
            processes.append(p)
        # 等待所有进程完成
        for p in processes:
            p.join()
    except Exception as e:
        ic(e)



