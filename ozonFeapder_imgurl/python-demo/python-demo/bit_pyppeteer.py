import asyncio
import pyppeteer

from bit_browser.bit_api import *
from general_purpose.utilslog import logger
from bit_api_v1 import *


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
        logger.debug(f'[{self.browserId}] -> pid: {self.pid} | ws: {self.ws}')

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

    async def close(self):
        await self.browser.close()
        time.sleep(5)
        # closeBrowser(self.browserId)


if __name__ == '__main__':
    bit_browser = BitBrowser("6438f135952748f1aadcee4320feb0eb")
    # asyncio.get_event_loop().run_until_complete(bit_browser.main())
