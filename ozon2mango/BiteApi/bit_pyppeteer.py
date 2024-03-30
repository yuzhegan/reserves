import asyncio
import pyppeteer
# from bit_api_V1 import *
from BiteApi.bit_pyppeteer import *
# from bit_browser.bit_api import *
# from general_purpose.utilslog import logger


class BitBrowser:
    def __init__(self, browserId):
        self.browser = None  # 初始化为 None
        self.browserId = browserId
        # updateBrowser(Ids=[self.browserId], syncTabs=False)
        res = openBrowser(self.browserId)
        detail_data = detailBrowser(self.browserId)['data']['browserFingerPrint']
        self.height = detail_data['openHeight']
        self.width = detail_data['openWidth']
        self.ws = res['data']['ws']
        self.pid = res['data']['pid']
        print(f'[{self.browserId}] -> pid: {self.pid} | ws: {self.ws}')
        self.cookies = None

        asyncio.get_event_loop().run_until_complete(self.main())

    async def init_browser(self):
        self.browser = await pyppeteer.launcher.connect({
            'headless': False,
            'browserWSEndpoint': self.ws,
            'autoclose': False,
            'width': self.width,
            'height': self.height
        })

    async def main(self):
        if self.browser is None:
            await self.init_browser()  # 如果浏览器实例不存在，则初始化
            page = await self.browser.newPage()
            await page.setViewport({'width': self.width, 'height': self.height})
            await page.goto('https://www.ozon.ru/')
            await page.waitFor(10000)
            try:
                # iframe_element = await page.querySelector('iframe')
                # frame = await iframe_element.contentFrame()
                # await frame.click('.ctp-checkbox-label')
                # 定位到 iframe
                iframe_element = await page.querySelector("iframe[id='cf-chl-widget-wzhw4']")
                iframe = await iframe_element.contentFrame()
                # 在 iframe 中找到按钮并点击
                button = await iframe.querySelector("#challenge-stage > div > label > input")
                await button.click()
            except Exception as e:
                print(e)
            self.cookies = await page.cookies()
            # print(cookies)
        return 

    async def close(self):
        await self.browser.close()
        time.sleep(5)
        # closeBrowser(self.browserId)


# if __name__ == '__main__':
#     browser_id = createBrowser('ozon')
#     openBrowser(browser_id)
#     bit_browser = BitBrowser(browser_id)
#     # print(bit_browser.cookies)
#     closeBrowser(browser_id)
#     deleteBrowser(browser_id)


    # asyncio.get_event_loop().run_until_complete(bit_browser.main())
