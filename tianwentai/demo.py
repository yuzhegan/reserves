# encoding='utf-8

# @Time: 2024-01-01
# @File: %
#!/usr/bin/env
from icecream import ic
import os
import requests
import re
import json
from readFile import *
import ddddocr
import time
from login import *
from login import WxUserLogin


class TianWenTai:
    def __init__(self,week, pmAm):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://weather.121.com.cn",
            "Pragma": "no-cache",
            "Referer": "https://weather.121.com.cn/sztwt/?",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309071d) XWEB/8447 Flue"
        }
        self.session = requests.session()
        self.session.headers.update(self.headers)
        self.wxuser = ''
        self.token, self.tokenId = self.get_token()
        # self.week = '星期五'
        self.week = week
        self.pmAm = pmAm
        # self.pmAm = "上午"
    def WaiteForUser(self):
        wxuser = None
        while not wxuser:
            WxUser = WxUserLogin('./tianwentai/code.txt')
            code = WxUser.ReadCode()
            wxuser = WxUser.genWxUser(code)
            if wxuser:
                print(wxuser)
                self.wxuser = wxuser
                break
            else:
                print("等待用户分享到文件助手")
                time.sleep(3)
        return wxuser



    def get_token(self):
        url = "https://weather.121.com.cn/szqx/api/token.js"
        response = self.session.get(url).text
        token = re.search('win\.szqbl\.token="([^"]+)"', response).group(1)
        # print(token)
        tokenId = re.search('win\.szqbl\.tokenId="([^"]+)"', response).group(1)
        # print(tokenId)
        return token, tokenId

    def get_tickets_info(self):
        url = "https://weather.121.com.cn/szqx/api/twt_v2/kfr/list.do"
        params = {
            "source": "wx",
            "wxuser": self.wxuser,
            "token": self.token,
            "tokenId": self.tokenId
        }
        data = {
            "yzm": "" 
        }
        try:
            response = self.session.post(url, params=params, data=data).json()
        except:
            print("获取票务信息失败")
            return None
        if response["code"] == 0:
            return response["data"]
        elif response["code"] == 1002:  #促发验证码
            time.sleep(2)
            yzm = twt.yzm_pass()
            data["yzm"] = yzm
            response = self.session.post(url, params=params, data=data).json()
            if response["code"] == 0:
                return response["data"]
        else:
            # TODO:  <03-01-24, getcookies> #
            return None
        return

    def Parse_data(self, data, week):
        # 判断是否有票
        get_ticket_key = data['dydptx']
        ticket_key_lists = list(get_ticket_key.keys())
        # 获取星期几和日期信息所对于的key
        for item in ticket_key_lists:
            if (week in item):
                ture_key = item
        # 判断是否有余票以及有几张
        ticket_nums = data["kfrs"][ture_key]   # 得到一个上午和下午的列表
        for item in ticket_nums:
            # if self.pmAm in item['name']:
            available_ticket = int(item['maxNum']) - int(item['curNum'])
            if available_ticket > 0:
                kfr_id = str(item['kfr_id'])
                kfr_sd_id = str(item['kfr_sd_id'])
            else:
                kfr_id = ''
                kfr_sd_id = ''

        print(week, "有", available_ticket, "张票", "kfr_id", kfr_id,  'kfr_sd_id', kfr_sd_id)
        return available_ticket, kfr_id, kfr_sd_id


    def submit_muplit_tickets(self, kfr_id, kfr_sd_id, df, yzm):
        # 添加随行成人
        url = "https://weather.121.com.cn/szqx/api/twt/kfr/gryy/save.do"
        params = {
            "source": "wx",
            "wxuser": self.wxuser,
            "token": self.token,
            "tokenId": self.tokenId
        }
        renshu = len(df)
        # 随行人生
        entourageCount = str(renshu - 1)
        data = {
            "dyEndDate": "",
            "isTYXY": "no",
            "name": str(df['name'][0]),
            "cardType": "1",
            "cardNumber": str(df['id'][0]),
            "sex": str(df['sex'][0]),
            "mobile": str(df['phone'][0]),
            "carNumber": "",
            "entourageCount": str(entourageCount),
            "nonage": "0",
            "kfrSdId": kfr_sd_id,  # 预约的时间，在上一个函数提取
            "kfrId": kfr_id,   # 预约的时间，在上一个函数提取
            "isDydptx": "0",
            # "yzm": "ih8i9e"  # 验证码
            "yzm": str(yzm)  # 验证码
        }
        if entourageCount == '1':
            data["name1"] = df['name'][1]
            data["cardType1"] = "1"
            data["cardNumber1"] = str(df['id'][1])
            data["sex1"] = str(df['sex'][1])
        elif entourageCount == '2':
            data["name1"] = df['name'][1]
            data["cardType1"] = "1"
            data["cardNumber1"] = str(df['id'][1])
            data["sex1"] = str(df['sex'][1])
            data["name2"] = df['name'][2]
            data["cardType2"] = "1"
            data["cardNumber2"] = str(df['id'][2])
            data["sex2"] = str(df['id'][2])
        elif entourageCount == '3':
            data["name1"] = df['name'][1]
            data["cardType1"] = "1"
            data["cardNumber1"] = str(df['id'][1])
            data["sex1"] = str(df['sex'][1])
            data["name2"] = df['name'][2]
            data["cardType2"] = "1"
            data["cardNumber2"] = str(df['id'][2])
            data["sex2"] = str(df['sex'][2])
            data["name3"] = df['name'][3]
            data["cardType3"] = "1"
            data["cardNumber3"] = str(df['id'][3])
            data["sex3"] = str(df['sex'][3])
        ic(data)




        

        # data = {
        #     "dyEndDate": "",
        #     "isTYXY": "no",
        #     "name": "牛柏寒",
        #     "cardType": "1",
        #     "cardNumber": "411024199308248600",
        #     "sex": "0",
        #     "mobile": "18566660591",
        #     "carNumber": "",
        #     "entourageCount": entourageCount,
        #     "nonage": "0",
        #     "kfrSdId": kfr_sd_id,  # 预约的时间，在上一个函数提取
        #     "kfrId": kfr_id,   # 预约的时间，在上一个函数提取
        #     "isDydptx": "0",
        #     "name1": "徐之昊",
        #     "cardType1": "1",   # type 1 为身份证
        #     "cardNumber1": "430223200008017213",
        #     "sex1": "0",  # 0 为男 1为女
        #     "name2": "区小瑜",
        #     "cardType2": "1",
        #     "cardNumber2": "440684200011281521",
        #     "sex2": "0",
        #     "yzm": "ih8i9e"
        # }
        response = self.session.post(url, params=params, data=data).json()
        print(response)
        return response


    def submit_ticket(self, kfr_id, kfr_sd_id, df, yzm):
        # 单个人预约
        url = "https://weather.121.com.cn/szqx/api/twt/kfr/gryy/save.do"
        params = {
            "source": "wx",
            "wxuser": self.wxuser,
            "token": self.token,
            "tokenId": self.tokenId
        }
        # 单个人预约
        data = {
            "dyEndDate": "",
            "isTYXY": "no",
            "name": str(df['name'][0]),
            "cardType": "1",
            "cardNumber": str(df['id'][0]),
            "sex": str(df['sex'][0]),
            "mobile": str(df['phone'][0]),
            "carNumber": "",
            "entourageCount": "0",
            "nonage": "0",
            "kfrSdId": kfr_sd_id,
            "kfrId": kfr_id,
            "isDydptx": "0",
            "yzm": str(yzm)
        }
        print(data)

        response = self.session.post(url, params=params, data=data).json()
        print(response)
        return response

    def yzm_pass(self):
        url = "https://weather.121.com.cn/szqx/api/twt/kfr/gryy/code.do"
        params = {
        "source": "wx",
        "wxuser": self.wxuser,
        "t": str(int(time.time() * 1000))
    }
        response = self.session.get(url, params=params).content
        # print(response)
        # with open('./yzm.png', 'wb') as f:
        #     f.write(response)
        # with open("./yzm.png", 'rb') as f:
        #     image = f.read()
        ocr = ddddocr.DdddOcr(beta=True)
        res = ocr.classification(response)

        print(res) 
        return res





if __name__ == "__main__":
    df = read_file("./tianwentai/setttings.xlsx")
    while True:
        try:
            flowered_df = read_file("./tianwentai/flowered.csv")
        except:
            flowered_df = df.clear()
        df = get_buji(df, flowered_df)  # 去除已经预约过的人信息
        twt = TianWenTai(df['week'][0], df['pmAm'][0])
        data = twt.get_tickets_info()
        if data == None:
            twt.WaiteForUser()
            data = twt.get_tickets_info()
            
        available_ticket, kfr_id, kfr_sd_id = twt.Parse_data(data, twt.week)
        if available_ticket > 0: # 有票
            flower_df = create_flower_data(available_ticket, df, twt.week, twt.pmAm)
            if len(flower_df) == 1:
                try:
                    res = twt.submit_ticket(kfr_id, kfr_sd_id, flower_df, '')
                    if res['code'] == 1002:
                        yzm = twt.yzm_pass()
                        time.sleep(1)
                        res = twt.submit_ticket(kfr_id, kfr_sd_id, flower_df, yzm)
                except:
                    continue
            else:
                try:
                    res = twt.submit_muplit_tickets(kfr_id, kfr_sd_id, flower_df, '')
                    if res['code'] == 1002:
                        yzm = twt.yzm_pass()
                        time.sleep(1)
                        res = twt.submit_muplit_tickets(kfr_id, kfr_sd_id, flower_df, yzm)
                except:
                    continue
            # append flower_df to flowered.csv
            pandas_df = flower_df.to_pandas()
            pandas_df.to_csv("./tianwentai/flowered.csv", mode='a', header=False, index=False)


        time.sleep(1)

        if len(df) == len(flowered_df):  # 预约完成的人数和设置人数相等
            break

    


"""
import requests


params = {
    "source": "wx",
    "wxuser": "8bdeff9194094319a6854594b8051726",
    "token": "639957149F191A16379C27F5C4169541F6EDB2B29C82940A5EAEC8B90B58E0DC7AA454C9ED7682CFBE945E124F7762CA6EEC615CFB1B9E603B8A46103E45E71F752CE59C522A0D423C0DA31CAFDAD402729A05E8A9036B5FBC7C3B408EE98F55E327887F800ACFD2E3E8A104BF31478E50A4C5DD859265CEF01A5C3C05D2E7C73393597A913F42382A7310F10EA86CBD30FE0EA4072D99DE85EED531A152A7E6576C0AF5E3189B5F986DDFE292A4733CA6EDE5C3B13B2025526AD82089DABAF4CB7C55251545B7D75E6FF44DCF6544C42855311992D151E4C2B1D55F6CECED5110E6F27DE71AE91DE64B5C296587F9D1C29E080764DB85B6F1821A0EF3670C4ECDD44D3082802387EEDFE038770358ABAA447CEAC9F7EA4206579AEB4DBEAB9DA397EDD1A1FC9A2D3F2A9383F7FA83682AD06499D4C93A5FE9D41A928831736D2E3C80703A8626CFBAFE40F7DAD0CA4B94F025FF39C923D4EAAAD47C919A1EF6BFF4B515F96BEEE0BF578CAD021D3BF5A495B48B07CC3A880D88DA5EA1E6D2A9",
    "tokenId": "1656753922-1290373290-1689564990-1889704473"
}
# 单个人预约
data = {
    "dyEndDate": "",
    "isTYXY": "no",
    "name": "牛柏寒",
    "cardType": "1",
    "cardNumber": "411024199308248600",
    "sex": "0",
    "mobile": "18566660591",
    "carNumber": "",
    "entourageCount": "0",
    "nonage": "0",
    "kfrSdId": "100220",
    "kfrId": "201764",
    "isDydptx": "0"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.text)
print(response)"""
