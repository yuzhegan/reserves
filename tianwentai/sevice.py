# encoding='utf-8
# @Time: 2024-01-02
# @File: %
#!/usr/bin/env
# from icecream import ic
from flask import Flask, request
from urllib.parse import urlparse, parse_qs
app = Flask(__name__)
@app.route('/api/msg', methods=['POST'])
def receive_message():
    data = request.get_json()# 获取POST请求的JSON数据
    event = data.get('event')# 获取event字段的值
    if event == 10010:
        msg = data['data']['data']['msg']# 提取data.data.msg字段的值
        start_index = msg.find('<shareUrlOpen>') + len('<shareUrlOpen>')
        end_index = msg.find('</shareUrlOpen>')
        content = msg[start_index:end_index]
        if len(content) > 0:
            # 解析URL
            parsed_url = urlparse(content)
            # 提取查询字符串
            query_params = parse_qs(parsed_url.query)
            # 获取'code'参数的值
            code = query_params.get('code', [None])[0]
            with open('code.txt', 'a') as f:
                f.write(code + '\n')
            print(code)
        else:
            print("content is empty")
    return 'Message received'# 返回响应
if __name__ == '__main__':
    app.run(port=12589)
