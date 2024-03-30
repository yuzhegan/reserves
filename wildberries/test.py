# encoding='utf-8
# @Time: 2024-01-12
# @File: %
#!/usr/bin/env
from icecream import ic
import os
# 创建 JSContext 对象
from py_mini_racer import MiniRacer
ctx = MiniRacer()
ctx2 = MiniRacer()

# 定义 JavaScript 代码
# js_code = """
# function addOne(num) {
#     return num + 1;
# }
# """
with open("./wildberries/delievry.js", "r", encoding="utf-8") as f:
    jscode = f.read()
with open("./wildberries/ImageUrl.js", "r", encoding="utf-8") as f:
    jsimgcode = f.read()

# 在上下文中执行 JavaScript 代码
ctx.eval(jscode)
# 调用 JavaScript 函数并传递参数
# result = ctx.call("addOne", 5)
result = ctx.call("deliveryDateTxt", 123)

# 打印结果
print(result)
ctx2.eval(jsimgcode)

result = ctx2.call("constructHostV2", '113402919')

# 打印结果
print(result)

