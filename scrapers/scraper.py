import re
import os
import requests
import pandas as pd
from lxml import etree
from bs4 import BeautifulSoup
from functionalities.tools import TryExcept, yamlMe, randomTime, userAgents
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError


class Amazon:
    def __init__(self):
        self.catchClause = TryExcept()
        self.selectors = yamlMe('selector')

    def amazonMe(self, head):
        print(f"Initiating the Amazon automation | Powered by Playwright.")
        amazon_dicts = []       

        user_input = str(input("Enter a URL:> "))   

        # regex pattern to verify if the entered link is correct Amazon link:
        # Below regex pattern is to verify certain pattern on amazon link after clicking products, it may look confusing.
        amazon_link_pattern = re.search("^https://www.amazon\.(com|co\.uk)(/s\?.|/b/.)+", user_input)
        if amazon_link_pattern == None:
            message = "Invalid link. Please enter an amazon link including product category of your choice."
            return message


        with sync_playwright() as play:
            browser = play.chromium.launch(headless=head, slow_mo=3*1000)
            context = browser.new_context(user_agent=userAgents())
            page = context.new_page()
            page.goto(user_input)

            page.wait_for_timeout(timeout=randomTime(4)*1000)

            # Below variable is for the searched product, there could be more that two elements for it.
            try:
                product_name = page.query_selector(self.selectors['product_name_one']).inner_text().strip()
            except AttributeError:
                product_name = page.query_selector(self.selectors['product_name_two']).inner_text().strip()        

            try:
                page.wait_for_selector(self.selectors['main_content'], timeout=10*1000)
            except PlaywrightTimeoutError:
                print(f"Content loading error. Please try again in few minute.")        

            try:
                last_page = page.query_selector(
                    self.selectors['total_page_number_first']).inner_text().strip()
            except AttributeError:
                try:
                    last_page = page.query_selector_all(self.selectors['total_page_number_second'])[-2].get_attribute('aria-label').split()[-1]
                except IndexError:
                    last_page = 3

            print(f"Number of pages | {last_page}.")
            print(f"Scraping | {product_name}.")

            for click in range(1, int(last_page)+1):
                print(f"Scraping page | {click}")
                page.wait_for_timeout(timeout=randomTime(8)*1000)
                for content in page.query_selector_all(self.selectors['main_content']):
                    data = {
                        "Product": self.catchClause.text(content.query_selector(self.selectors['hyperlink'])),
                        "ASIN": self.catchClause.attributes(content, 'data-asin'),
                        "Price": self.catchClause.text(content.query_selector(self.selectors['price'])),
                        "Original price": self.catchClause.text(content.query_selector(self.selectors['old_price'])),
                        "Review": self.catchClause.text(content.query_selector(self.selectors['review'])),
                        "Review count": re.sub(r"[()]", "", self.catchClause.text(content.query_selector(self.selectors['review_count']))),
                        "Hyperlink": f"""http://www.amazon.com{self.catchClause.attributes(content.query_selector(self.selectors['hyperlink']), 'href')}""",
                        "Image URL": f"""{self.catchClause.attributes(content.query_selector(self.selectors['image']), 'src')}""",                    
                    }
                    amazon_dicts.append(data)

                try:
                    page.query_selector(self.selectors['next_button']).click()
                except AttributeError:
                    print(f"Oops content loading error beyond this page. Issue on url {page.url} | number:> {click}")
                    break

            browser.close()

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
        async with async_playwright() as play:
            browser = await play.chromium.launch(headless = True, slow_mo = 3 * 1000)
            context = await browser.new_context(user_agent = userAgents())
            page = await context.new_page()

            await page.goto(url)
            
            asin_element = await page.query_selector(self.selectors['ASIN'])
            try:
                asin = await asin_element.get_attribute('data-csa-c-asin')
            except AttributeError:
                try:
                    asin_one = await page.query_selector(self.selectors['ASIN_I'])
                    asin = await asin_one.get_attribute('data-csa-c-asin')
                except PlaywrightTimeoutError:
                    asin = "Content loading error. Please try again in few minutes."

            return asin
       
        
