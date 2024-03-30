# encoding='utf-8
# @Time: 2023-10-21
# @File: %
#!/usr/bin/env
from gentrace import get_trace
import ddddocr
import base64
import re
import json
from icecream import ic
import time
import os
# get sild and bg img
import requests
headers = {
    'authority': 'iv.jd.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://passport.jd.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
session = requests.session()
# add headers to session
session.headers.update(headers)
# params = {
#     'ReturnUrl': 'https://www.jd.com/',
# }
# response = requests.get('https://passport.jd.com/new/login.aspx', params=params, headers=headers)
# # get the cookies in response
# cookies = response.cookies
# ic(cookies)
def gentraceParams():
    params = {
        'appId': '1604ebb2287',
        'scene': 'login',
        'product': 'click-bind-suspend',
        'e': 'FHWFGUXTWJQDJ7VQMTQK243QCO43XEC5CRGLGTKMVTAV7GWKCPSTIEGSFTX2WRFTUSGB4DUXDFINJJWXQW7IYCPHMU',
        'j': '',
        'lang': 'zh_CN',
        'callback': 'jsonp_047453865740509427',
    }
    response = session.get('https://iv.jd.com/slide/g.html',
                           params=params,  headers=headers).text
    # str to json
    # response = response.replace('jsonp_07097674328611292(', '')
    # response = response.replace(')', '')
    # 原始字符串
    # 使用正则表达式匹配 JSON 数据
    pattern = r'\((.*?)\)'  # 匹配括号内的内容
    match = re.search(pattern, response)
    if match:
        response = match.group(1)
    else:
        print("No JSON data found.")
    response = json.loads(response)
    # ic(response)
    bg = response['bg']
    patch = response['patch']
    # base64 to img
    bg = base64.b64decode(bg)
    with open('./jdlogin/img/bg.png', 'wb') as f:
        f.write(bg)
    patch = base64.b64decode(patch)
    with open('./jdlogin/img/patch.png', 'wb') as f:
        f.write(patch)
    # get the instance of sild in bg img
    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    bg = open('./jdlogin/img/bg.png', 'rb').read()
    patch = open('./jdlogin/img/patch.png', 'rb').read()
    instance = det.slide_match(patch, bg, simple_target=True)['target'][0]
    instance = round(instance*242/360+23)
    ic(instance)
    challenge = response['challenge']
    # y = response['y']
    trace = get_trace(instance)
    return trace, challenge
    # print(trace)
def check_trace(trace):
    import execjs
    with open('./jdlogin/demo.js', 'r', encoding='utf-8') as f:
        js = f.read()
    ctx = execjs.compile(js)
    result = ctx.call('getbparms', trace)
    time.sleep(6)
    contexts = session.get(
        'https://seq.jd.com/jseqf.html?bizId=passport_jd_com_login_pc&platform=js&version=1', headers=headers).text
    session_id = re.findall(r'_jdtdmap_sessionId=\"(.+?)\"', contexts)[0]
    print(session_id)
    print(result)
    params_a = {
        'd': result,
        'c': challenge,
        'w': '242',
        'appId': '1604ebb2287',
        'scene': 'login',
        'product': 'click-bind-suspend',
        'e': 'FHWFGUXTWJQDJ7VQMTQK243QCO43XEC5CRGLGTKMVTAV7GWKCPSTIEGSFTX2WRFTUSGB4DUXDFINJJWXQW7IYCPHMU',
        'j': '',
        's': session_id,
        'o': '18566662525',
        'o1': '0',
        'u': 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F',
        'lang': 'zh_CN',
        'callback': 'jsonp_022378571588311447',
    }
    response = session.get('https://iv.jd.com/slide/s.html',
                           params=params_a,  headers=headers).text
    print(response)
    # get validate
    if 'validate' in response:
        validate = re.findall(r'"validate"\:"(.+?)"', response)[0]
    else:
        validate = ''
    print(validate)
    return validate
# 获取登陆验证参数
def genLoginParams(loginname, passwd, validate):
    import re
    import execjs
    import random
    url = 'https://passport.jd.com/uc/login?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
    response = session.get(url, headers=headers).text
    sa_token = re.findall(r' name="sa_token" value="(.*?)"', response)[0]
    # print(sa_token)
    uuid = re.findall(r' name="uuid" value="(.*?)"', response)[0]
    # print(uuid)
    publickey = re.findall(r'id="pubKey" value="(.*?)"', response)[0]
    # print(publickey)
    slideAppId = re.findall(r'id="slideAppId" value="(.*?)"', response)[0]
    # print(slideAppId)
    # 获取需要被加密的参数
    # 获取加密后的密码
    with open('./jdlogin/getpwd.js', 'r', encoding='utf-8') as f:
        js = f.read()
    ctx = execjs.compile(js)
    nloginpwd = ctx.call('getEntryptPwd', publickey, passwd)
    print("enptypwd", nloginpwd)
    originParams = "uuid=" + uuid + "&" + 'ReturnUrl=https%3A%2F%2Fwww.jd.com%2F' + \
        "&r=" + str(random.random()) + "&version=2015"
    with open('./jdlogin/encrypyData.js', 'r', encoding='utf-8') as f:
        jscode = f.read()
    ctx1 = execjs.compile(jscode)
    aksParamsU = ctx1.call('encrypte', originParams)
    print("aksParamsU", aksParamsU)
    # BLNG%2BOAaF6thLXbFEcDU41R1LNus5sMZrAN6br1zl39QRDYPR6koC%2FaggLH2x1HYdoB77Br%2BljNRnIRQbKQ4xhSGyKuXUJ8S98nu5ESBa5sAg7gAiTB7EPKhbqAKT5bDjZ8wq%2B2AJVYePxTb63%2FDhIpTIExGgCTeJDyZovhUKdk%3D  nlogpwd
    # 82fe3dc5d7e34eee954e3078b11297bd validate
    # MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDC7kw8r6tq43pwApYvkJ5laljaN9BZb21TAIfT%2FvexbobzH7Q8SUdP5uDPXEBKzOjx2L28y7Xs1d9v3tdPfKI2LR7PAzWBmDMn8riHrDDNpUpJnlAGUqJG9ooPn8j7YNpcxCa1iybOlc2kEhmJn5uwoanQq%2BCA6agNkqly2H4j6wIDAQAB publickey
    # B68C442BE645754F33277E701208059080DD726A94A73F76DEC3053A838549C06EB7D3797CE1C5BBE7C2B2EF9CA7D467C3C76FF0A28885EE64B432120BA9B13D348C69B7D2A54084AD0AF9F604987E3FF4F05CFA833594DEAA638A1460132F8E4FC41F9984A0550F77FF3A51047D9FFA6937B2323ADE6CDB3A98776094AD46AFC0D104BE5A33FD4B2D219E65930F424CA62E9A76B0553DAFABE006ED3256B130266A76FAF5CCE3ADAB479A1B91EBE72CBE348721157A9ADE4809A653BD76467A03A1E4874489458EE274AA379059955C6DD9645B35BD50AFF11680049E2D6955F71B1EF365B7A42E3D01C2DBECDFE2FCDCA58E96CFF5E4962C207A3C761D64AD6947BFEA97514596191F42E568198C1747C8CF0FFA4D03753651D9C1F0C244AD439948BA95920AD35D78C4EF60BF596647638BED4E9B50DE442DC92E7076CDEEC430A48C806A2A6782F30D95F50E3105025BDB7F90DFB26E7B3C5376C45B083E8B1B15CB05195678AD094B918B9BAE6960B6999BD5CC8685161021941C83C3BBA41311E6B57590040DF23EA93DD5EC8219C5D1FCE4419CA9A884A0990EF6CF43DE9ABBD8C7715D7CA121DAD513E778BBE124D36CBF72E7776B97C53EE38FA43FA54453E308B3DC3479D48EABC15B8A5FD6F010C266BD9BB51D166F3D158654E9A9E6D016C29C5209D54F03FAB05D0AAC  sa_token
    # 20231027145422981%3Btzi5639mggtgzgj6%3B73806%3Btk03w8ab31b9218n0eA1a2haYaiISkBaI-AeEPsAjAYaICnUQ8MkrN4C_QMdlmlnG2_Zqi1FdduCtCMswSFdw55lI22D%3B54d2950b6ae5aa06b7773a93757a5b6c%3B4.1%3B1698389662981%3Bee3cf7f6b94dc20e9265d83066bb9ceece4bb89e2b7e8bf5afb1bfd928788174bfa06c210ddd4437d8a2e234330c3a3980acde1a10effcc27fd84ad69b6a255fa2bacbfc5a0cc8222e4ac53b669906820b1461c75971601a3f031b5c1f40b721502f3b79e32d29b726ebec75a213493a818f67211b187fcf51e032e0b772bee8c70e4a1d7502aa775b148a504a31d627bcf531d9533a7364260209df9b582d6fa3c0169d662d6cbe2768feada51f122dfc2b8af3357745a5216b02d6b66ddb55c1fc12249d0a2369ba3dcfb85153c518d9b4ce79314e830709c96d9b7fb6458c0eeed56a7249662af82f061623b6aeeb11556bae3d955eb02831b1be469aa7f0 h5st
    # get h5st
    import subprocess
    command = "node ./jdlogin/h5st.js 18566660594"
    h5st = subprocess.run(command, shell=True, stdout=subprocess.PIPE).stdout
    h5st = h5st.decode('utf-8')
    print('h5st', h5st)
    from urllib.parse import quote
    nloginpwd = quote(nloginpwd, safe='')
    publickey = quote(publickey, safe='')
    print('publickey', publickey)
    h5st = quote(h5st, safe='')
    # 逆向h5st
    bodyParams = 'uuid='+uuid+'&eid=OWVMH2JHPYAUXHFVNO2HEADDNTXLW5YJMMHWT6U6LFOCL7VKYFPHFEI24RQHHVHND7O4UAZLLK4ZA5QWLR7DMNXGPE&fp=1338dc132072b3bc21630835835e8347&_t=_t&loginType=f&loginname='+loginname+'&nloginpwd='+nloginpwd+'&authcode=' + \
        validate+'&pubKey='+publickey+'&sa_token='+sa_token + \
        '&seqSid=554067931620574840&useSlideAuthCode=1&pageSource=login2023&pageLocation=https%3A%2F%2Fwww.jd.com%2F&firstShowAccountLoginPage=f&rm=false&h5st='+h5st+'&_stk=loginname'
    # print(bodyParams)
    aksParamsB = ctx1.call('encrypte', bodyParams)
    print("aksParamsB", aksParamsB)
    params = {
        'aksParamsU': aksParamsU,
    }
    data = {
        'aksParamsB': aksParamsB,
    }
    response = session.post('https://passport.jd.com/uc/loginService',
                            params=params, headers=headers, data=data)
    print(response.text)
    response = session.post(
        'https://api.m.jd.com/api?functionId=pcorder_getPopTelInfo&appid=order-jd-com&client=pc&clientVersion=1.0.0&uuid=122270672.1698485329708227162308.1698485330.1698485330.1698485330.1&loginType=3&t=1698486696894&body={%22popVenderIds%22:%2211979875%22}',
    ).text
    print(response)

if __name__ == '__main__':
    trace, challenge = gentraceParams()
    validate = check_trace(trace)
    genLoginParams('18566660594', '6600439359gyx', validate)
# https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F 正则匹配一些数据
