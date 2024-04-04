"""
官方文档地址: https://doc2.bitbrowser.cn/jiekou/ben-di-fu-wu-zhi-nan.html
"""
import threading
import requests
import time

from general_purpose.utilslog import logger
from general_purpose.setting import RANDOM_IP

bitLock = threading.Lock()


class BitApi(requests.Session):

    def __init__(self):
        super().__init__()

    def request(self, method, url, **kwargs):
        with bitLock:
            logger.debug(f"[BitApi][{method}:{url}] {kwargs}")
            response = super().request(method, url, **kwargs)
            logger.debug(f"[BitApi][response:{str(response.text)[:200]}]")
            time.sleep(0.15)
        return response


bit_requests = BitApi()
PORT = 54345
URL = f"http://127.0.0.1:{PORT}"
headers = {'Content-Type': 'application/json'}
groupName = ""


# [健康检查接口，无参数，可以用来测试Local Server是否连接成功]
def health():
    return bit_requests.post(url=f"{URL}/health").json()


# [分组详情]
def detailGroup(Id: str):
    data = {
        "id": Id
    }
    res = bit_requests.post(f"{URL}/group/detail", json=data, headers=headers).json()
    return res


# [分组list] /group/list
def listGroup(page=0, pageSize=50, All=True):
    """
    :param page:        分页，从0开始
    :param pageSize:    分页条数，例如10
    :param All:         是否获取权限范围内的所有分组
    :return:
    """
    data = {
        "page": page,
        "pageSize": pageSize,
        "all": All
    }
    res = bit_requests.post(f"{URL}/group/list", json=data, headers=headers).json()
    return res


# 获取浏览器窗口详情
def detailBrowser(Id: str):
    json_data = {
        "id": Id,
    }
    res = bit_requests.post(f"{URL}/browser/detail", json=json_data, headers=headers).json()
    # logger.error(res)
    return res


# [创建或者更新窗口]，指纹参数 browserFingerPrint 如没有特定需求，只需要指定下内核即可，如果需要更详细的参数，请参考文档
def createBrowser(groupName, name=""):
    json_data = {
        'groupId': getGroupId(groupName),  # 群组ID，绑定群组时传入，如果登录的是子账号，则必须赋值，否则会自动分配到主账户下面去
        'platform': '',  # 账号平台open
        'platformIcon': '',  # 取账号平台的 hostname 或者设置为other
        'url': '',  # 打开的url，多个用,分开
        'name': name,  # 窗口名称
        'remark': '',  # 备注
        'userName': '',  # 用户账号
        'password': '',  # 用户密码
        'cookie': '',  # Cookie，符合标准的序列化字符串，具体可参考文档
        # IP库，默认ip-api，选项 ip-api | ip123in | luminati，luminati为Luminati专用
        'ipCheckService': 'ip-api',
        'proxyMethod': 2,  # 代理方式 2自定义 3 提取IP
        # 代理类型  ['noproxy', 'http', 'https', 'socks5', '911s5']
        'proxyType': 'noproxy',
        'host': '',  # 代理主机
        'port': '',  # 代理端口
        'proxyUserName': '',  # 代理账号
        'proxyPassword': '',  # 代理密码
        'ip': '',  # ip
        'city': '',  # 城市
        'province': '',  # 州/省
        'country': '',  # 国家地区
        'dynamicIpUrl': "",  # 提取IP url，参考文档
        'dynamicIpChannel': 'common',  # 提取IP服务商，参考文档
        'isDynamicIpChangeIp': True,  # 提取IP方式，参考文档
        'isGlobalProxyInfo': False,  # 提取IP设置，参考文档
        'isIpv6': False,  # 是否是IP6
        'syncTabs': False,  # 同步标签页
        'syncCookies': True,  # 同步Cookie
        'syncIndexedDb': True,  # 同步IndexedDB
        'syncLocalStorage': True,  # 同步 Local Storage
        'syncBookmarks': False,  # 同步书签
        'credentialsEnableService': True,  # 禁止保存密码弹窗
        'syncHistory': True,  # 保存历史记录
        'clearCacheFilesBeforeLaunch': False,  # 启动前清理缓存文件
        'clearCookiesBeforeLaunch': False,  # 启动前清理cookie
        'clearHistoriesBeforeLaunch': False,  # 启动前清理历史记录
        'randomFingerprint': False,  # 每次启动均随机指纹
        # 浏览器窗口工作台页面，默认 chuhai2345,不展示填 disable 可选 chuhai2345 | localserver | disable
        'workbench': 'disable',
        'disableGpu': False,  # 关闭GPU硬件加速 False取反 默认 开启
        'enableBackgroundMode': False,  # 关闭浏览器后继续运行应用
        'disableTranslatePopup': False,  # 翻译弹窗
        'syncExtensions': False,  # 同步扩展应用数据
        'syncUserExtensions': False,  # 跨窗口同步扩展应用
        'allowedSignin': False,  # 允许google账号登录浏览器
        'abortImage': False,  # 禁止加载图片
        'abortMedia': False,  # 禁止视频自动播放
        'muteAudio': False,  # 禁止播放声音
        'stopWhileNetError': False,  # 网络不通停止打开
        "browserFingerPrint": {  # 指纹对象
            'coreVersion': '112',  # 内核版本 112 | 104，建议使用112，注意，win7/win8/winserver 2012 已经不支持112内核了，无法打开
            'isIpCreateLanguage': False,
            'languages': 'zh-CN',
            'isIpCreateDisplayLanguage': False,
            'displayLanguages': 'zh-CN'

        }
    }
    res = bit_requests.post(f"{URL}/browser/update",
                            json=json_data,
                            headers=headers).json()
    browserId = res['data']['id']
    return browserId


# [更新窗口]，支持批量更新和按需更新，ids 传入数组，单独更新只传一个id即可，只传入需要修改的字段即可，比如修改备注，具体字段请参考文档，browserFingerPrint指纹对象不修改，则无需传入
def updateBrowser(Ids, **kwargs):
    # logger.warning(Ids)
    json_data = {'ids': Ids}
    json_data = {**json_data, **kwargs}
    res = bit_requests.post(f"{URL}/browser/update/partial",
                            json=json_data, headers=headers, timeout=5).json()
    # logger.debug(f"{Ids} -> [更新窗口] {res}")
    return res


# [直接指定ID打开窗口]，也可以使用 createBrowser 方法返回的ID
def openBrowser(Id):
    json_data = {"id": f'{Id}'}
    res = bit_requests.post(f"{URL}/browser/open",
                            json=json_data, headers=headers).json()
    return res


# [获取浏览器窗口列表，注意参数：page从0开始]
def listBrowser(page, pageSize=100, groupName=None):
    json_data = {
        "page": page,
        "pageSize": pageSize
    }
    if groupName:
        json_data['groupId'] = getGroupId(groupName)

    res = bit_requests.post(f"{URL}/browser/list",
                            json=json_data,
                            headers=headers).json()
    return res


# [关闭窗口]
def closeBrowser(Id):
    json_data = {'id': f'{Id}'}
    bit_requests.post(f"{URL}/browser/close",
                      json=json_data, headers=headers).json()
    time.sleep(5)


# [删除浏览器]
def deleteBrowser(Id):
    json_data = {'id': f'{Id}'}
    bit_requests.post(f"{URL}/browser/delete",
                      json=json_data, headers=headers).json()


# [批量修改窗口代理信息]
def browserProxyUpdate(Ids: list, proxy=None):

    if proxy:
        proxyMethod = 3
        proxyType = "socks5"
        dynamicIpUrl = RANDOM_IP
    else:
        proxyMethod = 3
        proxyType = "noproxy"
        dynamicIpUrl = ""

    json_data = {
        "ids": Ids,
        "ipCheckService": 'ip-api',
        "proxyMethod": proxyMethod,
        "proxyType": proxyType,
        "host": "",
        "port": "",
        "proxyUserName": "",
        "proxyPassword": "",
        "dynamicIpUrl": dynamicIpUrl,
        "refreshProxyUrl": "",
        "dynamicIpChannel": "common",
        "isDynamicIpChangeIp": True,
        "isGlobalProxyInfo": False,
        "isIpv6": False
    }
    return bit_requests.post(url=f"{URL}/browser/proxy/update",
                             json=json_data, headers=headers).json()


# [获取所有活着的已打开的窗口的进程ID，会自动过滤掉已死掉的进程，无参数]
def browserPidAll():
    res = bit_requests.post(url=f'{URL}/browser/pids/all', headers=headers).json()
    return res


# [清理窗口缓存] /cache/clear
def clearCache(Ids: list):
    json_data = {
        "ids": Ids
    }
    res = bit_requests.post(url=f'{URL}/browser/pids/all', json=json_data, headers=headers).json()
    return res


# [排列窗口以及调整窗口尺寸]
def windowBounds():
    """
    # :param "type": "box", // 排列方式，宫格 box ， 对角线 diagonal
    # :param "startX": 0, // 起始X位置
    # :param "startY": 0, // 起始Y位置
    # :param "width": 500, // 宽度
    # :param "height": 300, // 高度
    # :param "col": 4, // 宫格排列时，每行列数
    # :param "spaceX": 0, // 宫格横向间距
    # :param "spaceY": 0, // 宫格纵向间距
    # :param "offsetX": 50, // 对角线横向偏移量
    # :param "offsetY": 50 // 对角线纵向偏移量
    # :param "seqlist": [] //序号数组
    :return:
    """
    data = {
        "type": "box",
        "width": 500,
        "height": 500,
        "col": 4
    }
    return bit_requests.post(url=f"{URL}/windowbounds", json=data, headers=headers).json()


"""
以下为自己封装的功能
"""


# [关闭所有开启的浏览器]
def killAll():
    Ids = browserPidAll()['data']
    if len(Ids) == 0:
        return
    for Id in Ids.keys():
        closeBrowser(Id)
    time.sleep(5)


# [检测比特平台是否开启]
def check_port():
    try:
        if bit_requests.get(url=URL).status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        return False


# 根据分组名字获取id
def getGroupId(name):
    for i in listGroup()["data"]["list"]:
        if name == i["groupName"]:
            return i["id"]


if __name__ == '__main__':
    # print(windowBounds())
    # print(getGroupId("淘宝"))
    # print(check_port())
    # while True:
    #     threading.Thread(target=check_port).start())
    # getGroupId("淘宝滑块")
    # print(createBrowser(groupName="淘宝滑块", name="测试"))
    updateBrowser(Ids=["38a3c28651934309b6dca8cd2d3891ce"], name="19231145049")
