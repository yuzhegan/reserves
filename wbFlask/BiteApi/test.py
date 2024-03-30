import asyncio
from pyppeteer import launch



async def click_checkbox_in_iframe():
    # browser = await launch({'headless': False},)
    width, height = 1366, 768
    browser = await launch(headless=False, args=['--disable-infobars', f'--window-size={width},{height}'])
    page = await browser.newPage()
    await page.setViewport(
        {'width': width, 'height': height}
    )
    await page.evaluateOnNewDocument(
        'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    )
    
    page = await browser.newPage()
    await page.setViewport(
        {'width': 1920, 'height': 1080}
    )
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
    await page.goto('https://www.ozon.ru/')  # Replace with the actual URL

    # Wait for the iframe to load and get the iframe element
    iframe_element = await page.waitForXPath('/html/body/div[1]/div/div[1]/div/div/iframe')

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

    await browser.close()

asyncio.get_event_loop().run_until_complete(click_checkbox_in_iframe())
