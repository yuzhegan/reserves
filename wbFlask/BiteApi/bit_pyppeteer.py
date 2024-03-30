import asyncio
import pyppeteer
from BiteApi.bit_api_V1 import *

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
            # page = await self.browser.newPage()
            
            await page.evaluateOnNewDocument(
                'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
            )
            
            # await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
            await page.goto('https://www.ozon.ru/')  # Replace with the actual URL
            try:
                # Wait for the iframe to load and get the iframe element
                button = await page.waitForXPath('/html/body/div/div/div/div[2]/button', timeout=6000)
                await button.click()
                # 
                iframe_element = await page.waitForXPath('/html/body/div[1]/div/div[1]/div/div/iframe', timeout=6000)
                await page.waitFor(10000)

                if iframe_element:
                    # Switch to the iframe
                    iframe = await iframe_element.contentFrame()

                    if iframe:
                        # Wait for the checkbox to load in the iframe
                        await iframe.waitForSelector('input[type=checkbox]')
                        iframe.hover("#challenge-stage > div > label > input")
                        # Find and click the checkbox
                        checkbox = await iframe.querySelector('input[type=checkbox]')
                        if checkbox:
                            await page.waitFor(20000)
                            await checkbox.click( options={
                        'button': 'left',
                        'clickCount': 1,  # 1 or 2
                        'delay': 3000,  # 毫秒
                    })
                            print("Checkbox clicked.")
                            await page.waitFor(20000)
                        else:
                            print("Checkbox not found.")
                    else:
                        print("Iframe content not found.")
                else:
                    print("Iframe not found.")
            except Exception as e:
                print(e)
                pass
            self.cookies = await page.cookies()
            # print(cookies)

            await self.browser.close()
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
