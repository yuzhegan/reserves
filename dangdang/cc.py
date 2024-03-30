# encoding='utf-8
# @Time: 2023-09-12
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests
import execjs
import os
import time
from PIL import Image
from io import BytesIO
import ddddocr
import json
import random


class dangdang():
    def __init__(self):
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://login.dangdang.com',
            'Pragma': 'no-cache',
            'Referer': 'https://login.dangdang.com/?returnurl=https%3A%2F%2Fwww.dangdang.com%2F',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }
        with open('./dangdang/dd-AES.js', 'r', encoding='utf-8') as f:
            js = f.read()
        self.ctx1 = execjs.compile(js)
        with open('./dangdang/paswd-AES.js', 'r', encoding='utf-8') as f:
            jscode = f.read()
        self.ctx2 = execjs.compile(jscode)

        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.permanent_id = self.get_permanent_id()
        self.time_stamp = self.get_time_stamp()
        self.requestId, self.rankey = self.get_randkey()
        print("requestId:", self.requestId)
        print("rankey:", self.rankey)
        # self.GetSlidingVerifyCode()
        self.sildeImg, self.bgImg, self.encryptKey, self.y, self.token = self.GetSlidingVerifyCode()
        print(self.sildeImg, self.bgImg, self.encryptKey, self.y, self.token)
        self.writeImg(self.sildeImg, 61, 61, 'sildeImg')
        self.writeImg(self.bgImg, 350, 175, 'bgImg')
        self.distance = self.get_distance()
        print("滑块距离为:", self.distance)
        self.point_json, self.slide_sign = self.get_encrypt_distance()
        print("point_json:", self.point_json)
        print("slide_sign:", self.slide_sign)
        self.encrypt_paswd = self.get_passwd('Gyx.6600439359')
        self.username = "18566660594"
        # print('passwd++++', self.encrypt_paswd)
        self.checkSlidingVerifyCode()
        self.login_sign = self.get_login_sign()
        if self.check_code:
            self.login()

    # 第一步获取__permanent_id

    def get_permanent_id(self):
        with open('./dangdang/__permanent_id.js', 'r', encoding='utf-8') as f:
            js = f.read()
        ctx = execjs.compile(js)
        __permanent_id = ctx.call('createPermanentID')
        return __permanent_id
    # 获取时间戳

    def get_time_stamp(self):
        return str(int(time.time()*1000))
    # 第二步 获取randkey, requestid, /getRankey

    def get_randkey(self):
        a = 'ct=pc&permanent_id={}&t={}'.format(
            self.permanent_id, self.time_stamp)
        sign = self.ctx1.call('AesEncrypt', a, '')
        # print(sign)
        data = {
            't': self.time_stamp,
            'ct': 'pc',
            'permanent_id': self.permanent_id,
            'requestId': '',
            'sign': sign
        }

        response = self.session.post('https://login.dangdang.com/api/customer/loginapi/getRankey',
                                     data=data)
        return response.json()['requestId'], response.json()['rankey']
    # 第三步 获取图片验证码接口 /loginapi/getSlidingVerifyCode，图片验证码接口
    # 需要两张图片，一张是滑块，一张是背景，encryptKey，用于后面point_json AES加密的key, ‘y’用于后面point_json 需要被加密的参数

    def GetSlidingVerifyCode(self):
        timestamp = self.get_time_stamp()
        a = 'ct=pc&permanent_id={}&requestId={}&situation=login&t={}'.format(
            self.permanent_id, self.requestId, timestamp)
        # print(a)
        sign = self.ctx1.call('AesEncrypt', a, self.rankey)
        # print(sign)
        data = {
            't': timestamp,
            'ct': 'pc',
            'permanent_id': self.permanent_id,
            'requestId': self.requestId,
            'situation': 'login',
            'sign': sign
        }
        response = self.session.post('https://login.dangdang.com/api/customer/loginapi/getSlidingVerifyCode',
                                     data=data)
        # print(response.json())
        return response.json()['data']['slideImg'], response.json()['data']['bgImg'], response.json()['data']['encryptKey'], response.json()['data']['y'], response.json()['data']['token']
    # 第四步 下载滑块图片

    def writeImg(self, url, width, height, imgname):
        response = self.session.get(url)
        if os.path.exists('./dangdang/Img') == False:
            os.mkdir('./dangdang/Img')
        origin_img = Image.open(BytesIO(response.content))
        resized_img = origin_img.resize((width, height))
        resized_img.save(f'./dangdang/Img/{imgname}.png')
    # 获取滑块距离

    def get_distance(self):
        det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
        # print(ocr.classification('./dangdang/Img/sildeImg.png'))
        return det.slide_match(open('./dangdang/Img/sildeImg.png', 'rb').read(), open('./dangdang/Img/bgImg.png', 'rb').read(), simple_target=True)['target'][0]
    # 第五步 获取加密后的滑块距离 point_json

    def get_encrypt_distance(self):
        self.encrypt_timestamp = self.get_time_stamp()
        self.cost_time = str(
            int(self.encrypt_timestamp) - int(self.time_stamp))
        print(self.cost_time)

        with open('./dangdang/point_json-AES.js', 'r', encoding='utf-8') as f:
            js = f.read()
        ctx = execjs.compile(js)
        point_json = ctx.call('AesEncrypt', self.distance,
                              self.y, self.encryptKey)
        # aa = "ct=pc&need_new_verifydata=0&permanent_id={}&point_json={}&requestId={}&situation=login&slide_cost_time=1277&t={}&verifyToken={}".format(
        #     self.permanent_id, point_json, self.requestId, self.encrypt_timestamp, self.token)
        aa = 'ct=pc&need_new_verifydata=0&permanent_id={}&point_json={}&requestId={}&situation=login&slide_cost_time={}&t={}&verifyToken={}'.format(
            self.permanent_id, point_json, self.requestId, self.cost_time,  self.encrypt_timestamp, self.token)
        print(aa)
        ic(len(aa))
        sign = self.ctx1.call('AesEncrypt', aa, self.rankey)
        # print(point_json)
        return point_json, sign
    # 第六步 获取滑块后的passwd加密

    def get_passwd(self, passwd):
        enpy_passwd = self.ctx2.call('AesEncrypt', passwd, 'qrcode_p@ssw0rdK')
        return enpy_passwd
    # 第七步 验证checkSlidingVerifyCode 滑块, 获取checkCode

    def checkSlidingVerifyCode(self):
        timestamp = self.encrypt_timestamp
        data = {
            't': timestamp,
            'ct': 'pc',
            'permanent_id': self.permanent_id,
            'requestId': self.requestId,
            'situation': 'login',
            'verifyToken': self.token,
            'slide_cost_time': self.cost_time,
            'need_new_verifydata': '0',
            'point_json': self.point_json,
            'sign': self.slide_sign
        }
        print(data)

        response = self.session.post('https://login.dangdang.com/api/customer/loginapi/checkSlidingVerifyCode',
                                     data=data)
        if response.json()['errorMsg'] == '成功':
            self.check_code = response.json()['data']['checkCode']
        print(response.json())

    # 第八步 获取登录sign
    def get_login_sign(self):
        self.timestamp = self.get_time_stamp()
        a = 'autokey=off&check_code={}&check_code_type=1&ct=pc&password={}&permanent_id={}&requestId={}&t={}&token={}&username={}'.format(
            self.check_code, self.encrypt_paswd, self.permanent_id, self.requestId, self.timestamp, self.token, self.username
        )
        print(a)
        sign = self.ctx1.call('AesEncrypt', a, self.rankey)
        print(sign)
        return sign

    # 第九步 登录

    def login(self):
        data = {
            't': self.timestamp,
            'ct': 'pc',
            'permanent_id': self.permanent_id,
            'requestId': self.requestId,
            'username': self.username,
            'password': self.encrypt_paswd,
            'autokey': 'off',
            'token': self.token,
            'check_code': self.check_code,
            'check_code_type': '1',
            'sign': self.login_sign
        }
        print(data)

        response = requests.post(
            'https://login.dangdang.com/api/customer/loginapi/accountLogin', data=data).json()

        ic("login ===>>", response)


if __name__ == "__main__":
    a = dangdang()
