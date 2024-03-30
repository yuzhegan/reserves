# encoding='utf-8

# @Time: 2023-10-26
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import sys
import getopt
import time


def main(argv):
    username = ''
    passwd = ''
    dateTime = ''
    amopm = ''

    try:
        opts, args = getopt.getopt(argv[1:], "ha:u:p:d:a", ["ufile=", "pfile=", "dfile=", "afile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile> <++>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            useage(argv[0])
            sys.exit()
        elif opt in ("-u", "--ufile"):
            username = arg
        elif opt in ("-p", "--pfile"):
            passwd = arg
        elif opt in ("-d", "--dfile"):
            dateTime = arg
        elif opt in ("-a", "--pfile"):
            amopm = arg
        # 获取当前时间
    # current_time = time.localtime()
    # # 设置目标时间为 10:53:00
    # target_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
    #                                16, 00, 0, current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst))
    # # 计算需要等待的秒数
    # current_timestamp = time.mktime(current_time)
    # target_timestamp = time.mktime(target_time)
    # wait_seconds = target_timestamp - current_timestamp
    # print("等待", wait_seconds, "秒")
    # # 等待到目标时间
    # time.sleep(wait_seconds)
    # 在目标时间执行秒杀定时程序
    # seckill_program('18682001980', '123456', '2021-09-26', '上午')
    def seckill_program(username, passwd, dateTime, amopm):
        print('username:', username)
        print('passwd:', passwd)
        print('dateTime:', dateTime)
        print('amopm:', amopm)
    seckill_program(username, passwd, dateTime, amopm)


    # print('输入的文件为：', inputfile)
    # print('输出的文件为：', outputfile)


if __name__ == "__main__":
    main(sys.argv)
