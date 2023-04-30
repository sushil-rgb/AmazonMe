from functionalities.tools import TryExcept, yamlMe, randomTime, userAgents, verify_amazon, create_path

from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from bs4 import BeautifulSoup
import pandas as pd
import aiohttp
import re
import os


class Amazon:
    def __init__(self):
        self.headers = {'User-Agent': userAgents()}
        self.catchClause = TryExcept()
        self.selectors = yamlMe('selector')

    
    async def static_connection(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers = self.headers) as resp:
                content = await resp.read()
                return content
    

    async def getASIN(self, url):
        try:
            split_url = url.split('dp')[-1].split('/')[1]
        except IndexError:
            split_url = url.split('dp')[1].split("?")[0].replace("/", "")
        return split_url

  
    async def amazonMe(self, interval, head, url):
        amazon_dicts = []
        if await verify_amazon(url):
            print("Invalid link. Please try proper amazon link product category of your choice.")
            return

        async with async_playwright() as play:            
            browser = await play.chromium.launch(headless=head, slow_mo=3*1000)
            context = await browser.new_context(user_agent = userAgents())
            page = await context.new_page()
            
            await page.set_viewport_size({"width": 1200, "height": 1080})

            print(f"Initiating the Amazon automation | Powered by Playwright.")
            
            await page.goto(url)
            await page.wait_for_timeout(timeout=randomTime(interval)*1000)
            await page.wait_for_load_state("networkidle")
                        
            try:
                await page.wait_for_selector(self.selectors['main_content'], timeout=10*1000)
            except PlaywrightTimeoutError:
                print(f"Content loading error. Please try again in a few minutes.")
                return "Content loading error"
            
            try:
                search_results = re.sub(r"""["]""", "", ((await (await page.query_selector(self.selectors['searches'])).inner_text()).strip()).title())
            except AttributeError:
                search_results = "Results"
            try:
                await page.wait_for_selector(self.selectors['main_content'], timeout=10*1000)
            except PlaywrightTimeoutError:
                print(f"Content loading error. Please try again in few minute.")
                return
        
            pages = 0
            while True:
                pages += 1
                next_btn = await page.query_selector(self.selectors['next_button'])
                print(f"Scraping pages {pages}" 
                      )
                await page.wait_for_timeout(timeout=randomTime(interval)*1000)

                card_contents = await page.query_selector_all(self.selectors['main_content'])
                for content in card_contents:
                    prod_hyperlink = f"""http://www.amazon.com{await self.catchClause.attributes(content.query_selector(self.selectors['hyperlink']), 'href')}"""
                    data = {
                        "Product": await self.catchClause.text(content.query_selector(self.selectors['hyperlink'])),
                        "ASIN": await self.getASIN(prod_hyperlink),
                        "Price": await self.catchClause.text(content.query_selector(self.selectors['price'])),
                        "Original price": await self.catchClause.text(content.query_selector(self.selectors['old_price'])),
                        "Review": await self.catchClause.text(content.query_selector(self.selectors['review'])),
                        "Review count": re.sub(r"[()]", "", await self.catchClause.text(content.query_selector(self.selectors['review_count']))),
                        "Hyperlink": prod_hyperlink,
                        "Image URL": f"""{await self.catchClause.attributes(content.query_selector(self.selectors['image']), 'src')}""",
                    }
                    amazon_dicts.append(data)

                try:
                    await (next_btn).click()
                except Exception as e:
                    print(f"Message | {str(e)}")
                    break                

            await browser.close()
            
        print(f"Scraping done. Now exporting to excel database.")

        directory_name = 'Amazon database'
        await create_path(directory_name)

        df = pd.DataFrame(amazon_dicts)
        df.to_excel(f"{os.getcwd()}//Amazon database//{search_results}-Amazon database.xlsx", index=False)
        print(f"{search_results} is saved.")


    async def dataByAsin(self, asin):
        url = f"https://www.amazon.com/dp/{asin}"
        content = await self.static_connection(url)       
        soup = BeautifulSoup(content, 'lxml')
        
        try:
            image_link = soup.select_one(self.selectors['image_link_I']).get('src')
        except AttributeError:
            try:
                image_link = soup.select_one(self.selectors['image_link_II']).get('src')
            except AttributeError:
                return 'Content loading error. Please try again in few minutes.'
        
        
        try:
            availabilities = soup.select_one(self.selectors['availability']).text.strip()
        except AttributeError:
            availabilities = 'In stock'
            
        store = await self.catchClause.static_text(soup.select_one(self.selectors['store']))
        store_link = f"""https://www.amazon.com{await self.catchClause.static_attributes(soup.select_one(self.selectors['store']), 'href')}"""
                        
        datas = {
            'Name': await self.catchClause.static_text(soup.select_one(self.selectors['name'])),
            'Price': await self.catchClause.static_text(soup.select_one(self.selectors['price_us'])),
            'Rating': await self.catchClause.static_text(soup.select_one(self.selectors['review'])),
            'Rating count': await self.catchClause.static_text(soup.select_one(self.selectors['rating_count'])),
            'Availability': availabilities,
            'Hyperlink': url,
            'Image': image_link,
            'Store': store,
            'Store link': store_link,

        }                
        
        return datas
                
        