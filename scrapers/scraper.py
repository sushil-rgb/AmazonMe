import re
import os
import pandas as pd
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

from functionalities.tools import TryExcept, yamlMe, randomTime, userAgents, verify_amazon, create_path


class Amazon:
    def __init__(self):
        self.headers = {'User-Agent': userAgents()}
        self.catchClause = TryExcept()
        self.selectors = yamlMe('selector')


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

            print(f"Initiating the Amazon automation | Powered by Playwright.")
            await page.goto(url)
            await page.wait_for_timeout(timeout=randomTime(interval)*1000)

            # Below variable is for the searched product, there could be more that two elements for it.
            try:
                product_name = (await (await page.query_selector(self.selectors['product_name_one'])).inner_text()).strip()
            except AttributeError:
                product_name = (await (await page.query_selector(self.selectors['product_name_two'])).inner_text()).strip()

            try:
                await page.wait_for_selector(self.selectors['main_content'], timeout=10*1000)
            except PlaywrightTimeoutError:
                print(f"Content loading error. Please try again in few minute.")
                return

            num_of_pages = '3'
            try:
                num_of_pages = (await (await page.query_selector(self.selectors['total_page_number_first'])).inner_text()).strip()
            except AttributeError:
                try:
                    num_of_pages = (await page.query_selector_all(self.selectors['total_page_number_second']))[-2].get_attribute('aria-label').split()[-1]
                except (PlaywrightTimeoutError, IndexError):
                    pass

            print(f"Number of pages | {num_of_pages}.")
            print(f"Scraping | {product_name}.")

            for click in range(1, int(num_of_pages)):
                print(f"Scraping page | {click}")
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
                    await (await page.query_selector(self.selectors['next_button'])).click()
                except AttributeError:
                    print(f"Oops content loading error beyond this page. Issue on url {page.url} | number:> {click}")
                    break

            await browser.close()
        print(f"Scraping done. Now exporting to excel database.")

        directory_name = 'Amazon database'
        await create_path(directory_name)

        df = pd.DataFrame(amazon_dicts)
        df.to_excel(f"{os.getcwd()}//Amazon database//{product_name}-Amazon database.xlsx", index=False)
        print(f"{product_name} is saved.")


    async def dataByAsin(self, asin):
        url = f"https://www.amazon.com/dp/{asin}"
        async with async_playwright() as play:
            browser= await play.firefox.launch(headless = True)
            context = await browser.new_context(user_agent = userAgents())
            page = await context.new_page()

            await page.goto(url)
            await page.wait_for_url(url, timeout = 30 * 1000)

            try:
                image_link = await (await page.query_selector(self.selectors['image_link_I'])).get_attribute('src')
            except AttributeError:
                try:
                    image_link = await (await page.query_selector(self.selectors['image_link_II'])).get_attribute('src')
                except AttributeError:
                    return "Content loading error. Please try again in few minutes."

            try:
                availabilities = (await (await page.query_selector(self.selectors['availability'])).inner_text()).strip()
            except AttributeError:
                availabilities = "In stock"

            datas = {
                'Name': await self.catchClause.text(page.query_selector(self.selectors['name'])),
                'Price': await self.catchClause.text(page.query_selector(self.selectors['price_us'])),
                'Rating': await self.catchClause.text(page.query_selector(self.selectors['review'])),
                'Rating count': (await self.catchClause.text(page.query_selector(self.selectors['rating_count']))),
                'Availability': availabilities,
                'Hyperlink': url,
                'Image': image_link,
                'Store': str(await self.catchClause.text(page.query_selector(self.selectors['store']))).split('Visit the')[-1].strip(),
                'Store link': f"""https://www.amazon.com{str(await self.catchClause.attributes(page.query_selector(self.selectors['store']), 'href'))}""",

             }

            await browser.close()

            return datas

