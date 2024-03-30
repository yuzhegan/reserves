import requests
import json
import re
import numpy as np
import cv2
import base64
import random
import time
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
import subprocess


class jd_verify:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        }
        # 滑动轨迹
        self.base_slide = [
            [
                "944",
                "341",
                1637921521380
            ],
            [
                "967",
                "369",
                1637921521380
            ],
            [
                "967",
                "369",
                1637921521382
            ],
            [
                "968",
                "369",
                1637921521481
            ],
            [
                "968",
                "369",
                1637921521497
            ],
            [
                "969",
                "369",
                1637921521505
            ],
            [
                "970",
                "369",
                1637921521521
            ],
            [
                "971",
                "369",
                1637921521537
            ],
            [
                "972",
                "369",
                1637921521545
            ],
            [
                "973",
                "369",
                1637921521561
            ],
            [
                "974",
                "369",
                1637921521569
            ],
            [
                "976",
                "369",
                1637921521577
            ],
            [
                "976",
                "369",
                1637921521585
            ],
            [
                "978",
                "369",
                1637921521593
            ],
            [
                "979",
                "369",
                1637921521601
            ],
            [
                "980",
                "369",
                1637921521609
            ],
            [
                "981",
                "369",
                1637921521617
            ],
            [
                "982",
                "369",
                1637921521625
            ],
            [
                "984",
                "369",
                1637921521633
            ],
            [
                "985",
                "369",
                1637921521641
            ],
            [
                "987",
                "369",
                1637921521657
            ],
            [
                "988",
                "369",
                1637921521665
            ],
            [
                "990",
                "369",
                1637921521673
            ],
            [
                "991",
                "369",
                1637921521681
            ],
            [
                "992",
                "369",
                1637921521689
            ],
            [
                "993",
                "369",
                1637921521697
            ],
            [
                "995",
                "369",
                1637921521705
            ],
            [
                "996",
                "369",
                1637921521713
            ],
            [
                "999",
                "369",
                1637921521721
            ],
            [
                "1002",
                "369",
                1637921521729
            ],
            [
                "1004",
                "369",
                1637921521737
            ],
            [
                "1006",
                "369",
                1637921521745
            ],
            [
                "1008",
                "369",
                1637921521753
            ],
            [
                "1009",
                "369",
                1637921521761
            ],
            [
                "1012",
                "369",
                1637921521769
            ],
            [
                "1013",
                "369",
                1637921521777
            ],
            [
                "1015",
                "369",
                1637921521785
            ],
            [
                "1016",
                "369",
                1637921521793
            ],
            [
                "1018",
                "369",
                1637921521801
            ],
            [
                "1020",
                "369",
                1637921521809
            ],
            [
                "1022",
                "369",
                1637921521817
            ],
            [
                "1023",
                "369",
                1637921521825
            ],
            [
                "1026",
                "369",
                1637921521833
            ],
            [
                "1028",
                "369",
                1637921521841
            ],
            [
                "1030",
                "369",
                1637921521849
            ],
            [
                "1032",
                "369",
                1637921521857
            ],
            [
                "1036",
                "369",
                1637921521865
            ],
            [
                "1036",
                "369",
                1637921521873
            ],
            [
                "1040",
                "369",
                1637921521881
            ],
            [
                "1041",
                "369",
                1637921521890
            ],
            [
                "1044",
                "369",
                1637921521897
            ],
            [
                "1046",
                "369",
                1637921521905
            ],
            [
                "1048",
                "369",
                1637921521914
            ],
            [
                "1051",
                "369",
                1637921521921
            ],
            [
                "1052",
                "369",
                1637921521930
            ],
            [
                "1054",
                "369",
                1637921521937
            ],
            [
                "1055",
                "369",
                1637921521945
            ],
            [
                "1057",
                "369",
                1637921521953
            ],
            [
                "1059",
                "369",
                1637921521961
            ],
            [
                "1060",
                "369",
                1637921521969
            ],
            [
                "1064",
                "369",
                1637921521978
            ],
            [
                "1065",
                "369",
                1637921521985
            ],
            [
                "1067",
                "369",
                1637921521993
            ],
            [
                "1069",
                "369",
                1637921522001
            ],
            [
                "1072",
                "369",
                1637921522009
            ],
            [
                "1072",
                "369",
                1637921522017
            ],
            [
                "1076",
                "369",
                1637921522025
            ],
            [
                "1078",
                "369",
                1637921522033
            ],
            [
                "1079",
                "369",
                1637921522041
            ],
            [
                "1082",
                "369",
                1637921522049
            ],
            [
                "1084",
                "369",
                1637921522057
            ],
            [
                "1087",
                "369",
                1637921522065
            ],
            [
                "1089",
                "369",
                1637921522073
            ],
            [
                "1092",
                "369",
                1637921522081
            ],
            [
                "1095",
                "369",
                1637921522089
            ],
            [
                "1097",
                "369",
                1637921522097
            ],
            [
                "1100",
                "369",
                1637921522105
            ],
            [
                "1104",
                "369",
                1637921522113
            ],
            [
                "1104",
                "369",
                1637921522121
            ],
            [
                "1108",
                "369",
                1637921522129
            ],
            [
                "1109",
                "369",
                1637921522137
            ],
            [
                "1111",
                "369",
                1637921522145
            ],
            [
                "1114",
                "369",
                1637921522153
            ],
            [
                "1115",
                "369",
                1637921522161
            ],
            [
                "1116",
                "369",
                1637921522169
            ],
            [
                "1117",
                "369",
                1637921522178
            ],
            [
                "1119",
                "369",
                1637921522185
            ],
            [
                "1120",
                "369",
                1637921522193
            ],
            [
                "1121",
                "369",
                1637921522201
            ],
            [
                "1122",
                "369",
                1637921522209
            ],
            [
                "1124",
                "369",
                1637921522217
            ],
            [
                "1125",
                "369",
                1637921522225
            ],
            [
                "1126",
                "369",
                1637921522233
            ],
            [
                "1128",
                "369",
                1637921522241
            ],
            [
                "1128",
                "369",
                1637921522249
            ],
            [
                "1130",
                "369",
                1637921522257
            ],
            [
                "1131",
                "369",
                1637921522265
            ],
            [
                "1132",
                "369",
                1637921522281
            ],
            [
                "1134",
                "369",
                1637921522289
            ],
            [
                "1136",
                "369",
                1637921522305
            ],
            [
                "1138",
                "369",
                1637921522321
            ],
            [
                "1140",
                "369",
                1637921522329
            ],
            [
                "1141",
                "369",
                1637921522337
            ],
            [
                "1143",
                "369",
                1637921522345
            ],
            [
                "1144",
                "369",
                1637921522353
            ],
            [
                "1144",
                "369",
                1637921522361
            ],
            [
                "1146",
                "369",
                1637921522369
            ],
            [
                "1146",
                "369",
                1637921522381
            ],
            [
                "1147",
                "369",
                1637921522385
            ],
            [
                "1148",
                "369",
                1637921522395
            ],
            [
                "1148",
                "369",
                1637921522401
            ],
            [
                "1149",
                "369",
                1637921522409
            ],
            [
                "1150",
                "369",
                1637921522417
            ],
            [
                "1151",
                "369",
                1637921522425
            ],
            [
                "1152",
                "369",
                1637921522433
            ],
            [
                "1153",
                "369",
                1637921522449
            ],
            [
                "1155",
                "369",
                1637921522457
            ],
            [
                "1156",
                "369",
                1637921522481
            ],
            [
                "1156",
                "369",
                1637921522513
            ],
            [
                "1157",
                "369",
                1637921522529
            ],
            [
                "1158",
                "369",
                1637921522537
            ],
            [
                "1159",
                "369",
                1637921522545
            ],
            [
                "1160",
                "369",
                1637921522561
            ],
            [
                "1162",
                "369",
                1637921522569
            ],
            [
                "1164",
                "369",
                1637921522609
            ],
            [
                "1164",
                "369",
                1637921522617
            ],
            [
                "1165",
                "369",
                1637921522633
            ],
            [
                "1166",
                "369",
                1637921522641
            ],
            [
                "1167",
                "369",
                1637921522649
            ],
            [
                "1168",
                "369",
                1637921522657
            ],
            [
                "1170",
                "369",
                1637921522665
            ],
            [
                "1171",
                "369",
                1637921522673
            ],
            [
                "1172",
                "369",
                1637921522681
            ],
            [
                "1173",
                "369",
                1637921522689
            ],
            [
                "1174",
                "369",
                1637921522697
            ],
            [
                "1175",
                "369",
                1637921522705
            ],
            [
                "1176",
                "369",
                1637921522753
            ],
            [
                "1176",
                "369",
                1637921522769
            ],
            [
                "1177",
                "369",
                1637921522777
            ],
            [
                "1179",
                "369",
                1637921522793
            ],
            [
                "1180",
                "369",
                1637921522809
            ],
            [
                "1180",
                "369",
                1637921522817
            ],
            [
                "1181",
                "369",
                1637921522825
            ],
            [
                "1182",
                "369",
                1637921522849
            ],
            [
                "1183",
                "369",
                1637921522873
            ],
            [
                "1183",
                "369",
                1637921522880
            ],
            [
                "1184",
                "369",
                1637921522897
            ],
            [
                "1184",
                "369",
                1637921522921
            ],
            [
                "1185",
                "369",
                1637921522945
            ],
            [
                "1186",
                "369",
                1637921522961
            ],
            [
                "1188",
                "369",
                1637921522985
            ],
            [
                "1190",
                "369",
                1637921522993
            ],
            [
                "1192",
                "369",
                1637921523001
            ],
            [
                "1193",
                "369",
                1637921523010
            ],
            [
                "1196",
                "369",
                1637921523017
            ],
            [
                "1197",
                "369",
                1637921523033
            ],
            [
                "1199",
                "369",
                1637921523049
            ],
            [
                "1200",
                "369",
                1637921523057
            ],
            [
                "1200",
                "369",
                1637921523065
            ],
            [
                "1201",
                "369",
                1637921523073
            ],
            [
                "1202",
                "369",
                1637921523081
            ],
            [
                "1204",
                "369",
                1637921523089
            ],
            [
                "1204",
                "369",
                1637921523097
            ],
            [
                "1205",
                "369",
                1637921523105
            ],
            [
                "1207",
                "369",
                1637921523113
            ],
            [
                "1208",
                "369",
                1637921523121
            ],
            [
                "1208",
                "369",
                1637921523145
            ],
            [
                "1210",
                "368",
                1637921523201
            ],
            [
                "1211",
                "368",
                1637921523249
            ],
            [
                "1211",
                "368",
                1637921523380
            ],
            [
                "1211",
                "368",
                1637921523481
            ]
        ]
        # 晃动的轨迹
        self.push_slide = [
        [
            0,
            "160",
            1638111121463
        ],
        [
            1,
            "160",
            1638111121467
        ],
        [
            2,
            "160",
            1638111121486
        ],
        [
            3,
            "160",
            1638111121498
        ],
        [
            3,
            "159",
            1638111121499
        ],
        [
            4,
            "159",
            1638111121511
        ],
        [
            4,
            "159",
            1638111121520
        ],
        [
            5,
            "159",
            1638111121523
        ],
        [
            6,
            "159",
            1638111121532
        ],
        [
            7,
            "159",
            1638111121538
        ],
        [
            8,
            "159",
            1638111121547
        ],
        [
            8,
            "159",
            1638111121551
        ],
        [
            9,
            "159",
            1638111121555
        ],
        [
            9,
            "158",
            1638111121558
        ],
        [
            10,
            "158",
            1638111121564
        ],
        [
            11,
            "158",
            1638111121570
        ],
        [
            11,
            "157",
            1638111121572
        ],
        [
            12,
            "157",
            1638111121589
        ],
        [
            12,
            "157",
            1638111121644
        ],
        [
            13,
            "157",
            1638111121677
        ],
        [
            14,
            "157",
            1638111121714
        ],
        [
            14,
            "157",
            1638111121715
        ],
        [
            15,
            "157",
            1638111121719
        ],
        [
            16,
            "157",
            1638111121732
        ],
        [
            16,
            "156",
            1638111121735
        ],
        [
            16,
            "156",
            1638111121737
        ],
        [
            17,
            "156",
            1638111121741
        ],
        [
            17,
            "155",
            1638111121745
        ],
        [
            18,
            "155",
            1638111121758
        ],
        [
            19,
            "155",
            1638111121765
        ],
        [
            20,
            "155",
            1638111121782
        ],
        [
            19,
            "155",
            1638111121903
        ],
        [
            18,
            "155",
            1638111121916
        ],
        [
            17,
            "155",
            1638111121925
        ],
        [
            16,
            "155",
            1638111121931
        ],
        [
            16,
            "155",
            1638111121939
        ],
        [
            15,
            "155",
            1638111121947
        ],
        [
            14,
            "155",
            1638111121953
        ],
        [
            13,
            "155",
            1638111121970
        ],
        [
            12,
            "155",
            1638111121975
        ],
        [
            12,
            "155",
            1638111121983
        ],
        [
            12,
            "156",
            1638111121994
        ],
        [
            11,
            "156",
            1638111122009
        ],
        [
            10,
            "156",
            1638111122013
        ],
        [
            9,
            "157",
            1638111122039
        ],
        [
            8,
            "157",
            1638111122053
        ],
        [
            8,
            "157",
            1638111122059
        ],
        [
            7,
            "157",
            1638111122074
        ],
        [
            7,
            "157",
            1638111122078
        ],
        [
            6,
            "157",
            1638111122079
        ],
        [
            5,
            "157",
            1638111122092
        ],
        [
            4,
            "157",
            1638111122123
        ],
        [
            4,
            "158",
            1638111122128
        ],
        [
            4,
            "158",
            1638111122165
        ],
        [
            3,
            "158",
            1638111122240
        ],
        [
            2,
            "158",
            1638111122255
        ],
        [
            2,
            "159",
            1638111122298
        ],
        [
            1,
            "159",
            1638111122337
        ],
        [
            0,
            "159",
            1638111122438
        ],
        [
            0,
            "160",
            1638111122444
        ],
        [
            0,
            "160",
            1638111122489
        ],
        [
            0,
            "160",
            1638111122858
        ]]
        self.res_s = requests.Session()
        self.get_img()
        # self.offer(200)

    def get_img(self):
        res_verify = self.res_s.request('get',
            'https://iv.jd.com/slide/g.html?appId=1604ebb2287&scene=login&product=click-bind-suspend&e=HN7VXPNX7QX4ECLUX4RP5S7HGDUOBCQRR3XUYKT6XTGI27Z7J6C2K5PXGREX4R5LNZTR7D4GHAXHLIQ4OZFUJEW37A&j=&lang=zh_CN&callback=jsonp_05899805141725443',
            headers=self.headers).text
        # print(res_verify)
        verify_item = json.loads(re.search('\((.*?)\)', res_verify).group(1))
        bg_img = verify_item['bg']
        patch_img = verify_item['patch']
        self.challenge = verify_item['challenge']
        return self.img_test(bg_img, patch_img)

    def img_test(self, x, y):
        x = base64.b64decode(x)
        with open('x.png', 'wb') as f:
            f.write(x)
        img_array = np.frombuffer(x, np.uint8)
        img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
        y = base64.b64decode(y)
        with open('y.png', 'wb') as f:
            f.write(y)
        y = np.frombuffer(y, np.uint8)
        template = cv2.imdecode(y, cv2.COLOR_RGB2BGR)
        res = cv2.matchTemplate(img, template, cv2.TM_CCORR_NORMED)
        value = cv2.minMaxLoc(res)[2][0]

        # 获取的图片和显示的验证码图片大小有差
        distance = int(value * 278 / 360+25)
        print(distance)
        return self.offer(distance)

    def offer(self, distance):
        index = 0
        slide = []
        indexTime = str(int(time.time()))[:9]
        for item in self.base_slide:
            index += 1
            item[2] = int(indexTime + str(item[2])[-4:])
            if int(item[0]) >= (distance + int(self.base_slide[0][0])):
                slide = self.base_slide[:index]
                slide.append(
                    [str(distance + int(self.base_slide[0][0])), item[1], item[2] + 700 + int(random.random() * 1000)])
                break
        last = int(slide[-1][0].split('.')[0])
        print(last)
        pIndex = 0
        for item in self.push_slide:
            if pIndex == 0 or pIndex == len(self.push_slide) - 1:
                times = slide[-1][2]
            else:
                times = slide[-1][2] + (self.push_slide[pIndex + 1][2] - self.push_slide[pIndex][2])

            slide.append([str(item[0] + last), '369', times])
            pIndex += 1
        print(slide)
        print(self.get_slide(slide))
        # print(json.dumps(slide))
        return self.get_slide(slide)

    def get_slide(self, slide_value):
        node = execjs.get()
        js = node.compile(open('/home/dav/Github/reserve/jdlogin/other/CSDN/京东滑块js逆向/kkk.js', encoding='utf-8').read())
        func_name = f'JDJRValidate["prototype"].getCoordinate({slide_value})'
        keys = js.eval(func_name)
        print(keys)
        return self.sub_verify(keys)

    def sub_verify(self, d):
        # print('d', d)
        # print('challenge:', self.challenge)
        time.sleep(5)
        res = self.res_s.request('get','https://seq.jd.com/jseqf.html?bizId=passport_jd_com_login_pc&platform=js&version=1').text
        s = re.findall('_jdtdmap_sessionId="(.*?)";', res)[0]
        # print('sessionId', s)
        params = {
            'd': d,
            'c': self.challenge,
            'w': '278',
            'appId': '1604ebb2287',
            'scene': 'login',
            'product': 'click-bind-suspend',
            'e': 'HN7VXPNX7QX4ECLUX4RP5S7HGDUOBCQRR3XUYKT6XTGI27Z7J6C2K5PXGREX4R5LNZTR7D4GHAXHLIQ4OZFUJEW37A',
            'j': '',
            's': s,
            'o': '123',
            'o1': '0',
            'u': 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F',
            'lang': 'zh_CN',
            'callback': 'jsonp_046673984360336296',
        }

        response = requests.get('https://iv.jd.com/slide/s.html', params=params, headers=self.headers)
        print(response.text)


if __name__ == '__main__':
    # for i in range(5):
    jd_verify()

