# encoding='utf-8
# @Time: 2024-01-12
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import subprocess
# 定义 JavaScript 文件路径
js_file_path = "./wildberries/deliv.js"
# 定义要传递给 JavaScript 的参数
param = "136"
# 使用 Node.js 执行 JavaScript 文件，并传递参数
result = subprocess.run(["node", js_file_path, param], capture_output=True, text=True)
# 打印 stdout 和 stderr
print("STDOUT:", result.stdout)
# print("STDERR:", result.stderr)


js_file_path = "./wildberries/ImageUrl.js"

# 定义要传递给 JavaScript 的参数
param = "34659218"
# 使用 Node.js 执行 JavaScript 文件，并传递参数
result = subprocess.run(["node", js_file_path, param], capture_output=True, text=True)
# 打印 stdout 和 stderr
print("STDOUT:", result.stdout)
