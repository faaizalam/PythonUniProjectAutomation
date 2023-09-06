import asyncio
import openpyxl
from playwright.async_api import async_playwright

Executable = "C:/Program Files/Google/Chrome/Application/chrome.exe"
userdir = "C:/Users/OK Computers/AppData/Local/Google/Chrome/User Data/Profile 1"

async def myfu():
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(headless=False, executable_path=Executable, user_data_dir=userdir)
        page = await browser.new_page()
        await page.goto("https://www.amazon.com/")
    
        print("Current URL:", page.url)
        input_id = "twotabsearchtextbox"
        input_locator = page.locator(f"#{input_id}")
        await input_locator.type("shirts")
        inputbutton="nav-search-submit-button"
        await page.click(f"#{inputbutton}")

        
        element_selector = ".a-text-normal"
        await asyncio.sleep(10)
        elementsprice = await page.query_selector_all('.a-price-whole')
        elementsship = await page.query_selector_all('.s-image')
        inner_price = [await element.inner_text() for element in elementsprice]
        inner_ship = [await element.get_attribute('src') for element in elementsship]
        await asyncio.sleep(5)
        print(inner_price,inner_ship)
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Amazon Data"
        sheet['A1'] = "Price"
        sheet['B1'] = "image"
        for row, (price, href) in enumerate(zip(inner_price, inner_ship), start=2):
            print(row)
            sheet[f'A{row}'] = f'${price}'
            sheet[f'B{row}'] = href
        
        excel_file = "amazon_data.xlsx"
        workbook.save(excel_file)
        print(f"Data saved to {excel_file}")
       
        await asyncio.sleep(60)

        

asyncio.run(myfu())
