import re
import os
import pandas as pd
from functionalities.tools import TryExcept, yamlMe, randomTime, userAgents
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError


class Amazon:
    def __init__(self):
        self.headers = {'User-Agent': userAgents()}
        self.catchClause = TryExcept()
        self.selectors = yamlMe('selector')

    async def amazonMe(self, head, url):
        print(f"Initiating the Amazon automation | Powered by Playwright.")
        amazon_dicts = []                  

        # regex pattern to verify if the entered link is correct Amazon link:
        # Below regex pattern is to verify certain pattern on amazon link after clicking products, it may look confusing.
        amazon_link_pattern = re.search("^https://www.amazon\.(com|co\.uk)(/s\?.|/b/.)+", url)
        if amazon_link_pattern == None:
            message = "Invalid link. Please enter an amazon link including product category of your choice."
            return message
        
        async with async_playwright() as play:
            browser = await play.chromium.launch(headless=head, slow_mo=3*1000) 
            context = await browser.new_context(user_agent = userAgents())                      
            page = await context.new_page()
            await page.goto(url)

            await page.wait_for_timeout(timeout=randomTime(4)*1000)

            # Below variable is for the searched product, there could be more that two elements for it.
            try:
                product_name = (await (await page.query_selector(self.selectors['product_name_one'])).inner_text()).strip()                
            except AttributeError:
                product_name = (await (await page.query_selector(self.selectors['product_name_two'])).inner_text()).strip()
                    
            try:
                await page.wait_for_selector(self.selectors['main_content'], timeout=10*1000)
            except TimeoutError:
                print(f"Content loading error. Please try again in few minute.")  
                return     

            num_of_pages = '3'
            try:
                num_of_pages = (await (await page.query_selector(self.selectors['total_page_number_first'])).inner_text()).strip()                
            except AttributeError:
                try:                    
                    num_of_pages = (await page.query_selector_all(self.selectors['total_page_number_second']))[-2].get_attribute('aria-label').split()[-1]      
                except (TimeoutError, IndexError):
                    pass                
        
            print(f"Number of pages | {num_of_pages}.")
            print(f"Scraping | {product_name}.")

            for click in range(1, int(num_of_pages)):
                print(f"Scraping page | {click}")
                await page.wait_for_timeout(timeout=randomTime(8)*1000)

                card_contents = await page.query_selector_all(self.selectors['main_content'])
                for content in card_contents:
                    data = {                        
                        "Product": await self.catchClause.text(content.query_selector(self.selectors['hyperlink'])),                        
                        "ASIN": await content.get_attribute('data-asin'),
                        "Price": await self.catchClause.text(content.query_selector(self.selectors['price'])),
                        "Original price": await self.catchClause.text(content.query_selector(self.selectors['old_price'])),
                        "Review": await self.catchClause.text(content.query_selector(self.selectors['review'])),
                        "Review count": re.sub(r"[()]", "", await self.catchClause.text(content.query_selector(self.selectors['review_count']))),
                        "Hyperlink": f"""http://www.amazon.com{await self.catchClause.attributes(content.query_selector(self.selectors['hyperlink']), 'href')}""",
                        "Image URL": f"""{await self.catchClause.attributes(content.query_selector(self.selectors['image']), 'src')}""",                    
                    }
                    amazon_dicts.append(data)

                try:
                    await (await page.query_selector(self.selectors['next_button'])).click()
                except AttributeError:
                    print(f"Oops content loading error beyond this page. Issue on url {page.url} | number:> {click}")
                    break

            await browser.close()
        print(f"Scraping done. Now exporting to excel database.")

        path_dir = os.path.join(os.getcwd(), 'Amazon database')

        if os.path.exists(path_dir):
            pass
        else:
            os.mkdir(path_dir)

        df = pd.DataFrame(amazon_dicts)
        df.to_excel(f"{os.getcwd()}//Amazon database//{product_name}-Amazon database.xlsx", index=False)
        print(f"{product_name} is saved.")

    async def getASIN(self, url):
        try:
            split_url = url.split('dp')[-1].split('/')[1]
        except IndexError:
            split_url = url.split('dp')[1].split("?")[0].replace("/", "")
        return split_url
        
    async def dataByAsin(self, asin):        
        url = f"https://www.amazon.com/dp/{asin}"   
        # return url     
        async with async_playwright() as play:
            browser= await play.chromium.launch(headless = True)
            context = await browser.new_context(user_agent = userAgents())
            page = await context.new_page() 
           
            await page.goto(url) 
            try:
                await page.wait_for_url(url, timeout = 6 * 1000)
            except PlaywrightTimeoutError:
                return 'Content loading error. Please try again in few minutes.' 

            try:
                image_link = await (await page.query_selector(self.selectors['image_link_I'])).get_attribute('src')          
            except AttributeError:
                image_link = await (await page.query_selector(self.selectors['image_link_II'])).get_attribute('src') 

            try:
                availability = (await (await page.query_selector(self.selectors['availability'])).inner_text()).strip() 
            except AttributeError:
                availability = "In stock"      
            datas = {
                'Name': await self.catchClause.text(page.query_selector(self.selectors['name'])),
                'Price': await self.catchClause.text(page.query_selector(self.selectors['price_us'])),
                'Availability': availability,
                'Rating': await self.catchClause.text(page.query_selector(self.selectors['review'])),
                'Rating count': (await self.catchClause.text(page.query_selector(self.selectors['rating_count']))),
                'Hyperlink': url,
                'Image': image_link,
                'Store': str(await self.catchClause.text(page.query_selector(self.selectors['store']))).split('Visit the')[-1].strip(),
                'Store link': f"""https://www.amazon.com{str(await self.catchClause.attributes(page.query_selector(self.selectors['store']), 'href'))}""",
                
             }

            await browser.close()

            return datas
       
       