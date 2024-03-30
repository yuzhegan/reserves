# encoding='utf-8

# @Time: 2023-10-26
# @File: %
#!/usr/bin/env
from icecream import ic
import os


from multiprocessing import Process
import subprocess

# script_path = os.path.join(os.path.dirname(__file__), 'demo2.py')
def run_script(arguments):
    # 在这里执行脚本的代码，使用传递的参数param
    script_path = './honglifang/demo.py'
    # arguments = ['-u', 'yuzhe', '-p', '123456', '-d', '2024-11-03', '-a', '下午场一']

    subprocess.call(['python', script_path] + arguments)



# # 参数列表
params1 = ['-u', '19842655890', '-p', 'hlf137', '-d', '2023-11-04', '-a', '上午'] # 两个一小
params2 = ['-u', '18466241111', '-p', 'hlf138', '-d', '2023-11-04', '-a', '下午场一'] # 两个一小
params3 = ['-u', '18682851861', '-p', 'kjg3578', '-d', '2023-11-04', '-a', '下午场二'] # 两个一小
params4 = ['-u', '15107042854', '-p', '459000', '-d', '2023-11-04', '-a', '上午'] # 两个2小
params5 = ['-u', '18720600577', '-p', 'hlf4210', '-d', '2023-11-04', '-a', '下午场一'] # 两个2小
params6 = ['-u', '18974573951', '-p', 'hlf123', '-d', '2023-11-04', '-a', '下午场二']  # 两个2小
params7 = ['-u', '18172856581', '-p', 'wq6666', '-d', '2023-11-04', '-a', '晚上']  # 两个2小

# params = [params1, params2]
params = [params1, params2, params3, params4, params5, params6, params7]
# print(params)
#
# 创建进程列表
processes = []

# 创建并启动进程
for param in params:
    p = Process(target=run_script, args=(param,))
    p.start()
    processes.append(p)

# 等待所有进程完成
for p in processes:
    p.join()
