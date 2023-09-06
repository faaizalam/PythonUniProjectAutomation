import asyncio
import openpyxl
from playwright.async_api import async_playwright

Executable = "C:/Program Files/Google/Chrome/Application/chrome.exe"
userdir = "C:/Users/OK Computers/AppData/Local/Google/Chrome/User Data/Profile 1"



async def myfu():
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(headless=False, executable_path=Executable, user_data_dir=userdir)
        page = await browser.new_page()
        

        await page.goto("https://articlerewritertool.com/")
        await asyncio.sleep(10)

        await page.click('[data-testid="CloseIcon"]')
        await asyncio.sleep(2)
        await page.type('div.MuiBox-root.css-1u74t8s > div.MuiBox-root.css-c9w6ej > textarea',"hello my name is faaiz")
        # input_locator = await page.locator(".css-fanl19")
        await page.click("#\:r0\:")
    #   div.MuiBox-root.css-1jlhxqr > textarea
        await asyncio.sleep(5)
        Newtxet = await page.query_selector_all('div.MuiBox-root.css-1jlhxqr > textarea')
        for element in Newtxet:
         value = await element.get_property('value')
        print("this is you new text ", await value.json_value())

        # await input_locator.type("i am faaiz alam i fuck akhiyar")
    
        
       
        await asyncio.sleep(5)

        

asyncio.run(myfu())