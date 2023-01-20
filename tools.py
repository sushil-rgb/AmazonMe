import re
import sys
import random
import pandas as pd
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


# Random time interval between each requests made to server.
# You can decrease the time interval for faster scraping, however I discourage you to do so as it may hurt the server and Amazon may ban your IP address.
#  Scrape responsibly:
def randomTime(val):
    ranges = [i for i in range(3, val+1)]
    return random.choice(ranges)


# Hundreds of thousands of user agents for server:
def userAgents():
    with open('user-agents.txt') as f:
        agents = f.read().split("\n")
        return random.choice(agents)


# Try except to return the value when there is no element. This helps to avoid throwing an error when there is no element.
class TryExcept:
    def text(self, element):
        try:
            return element.inner_text().strip()
        except AttributeError:
            return "N/A"

    def attributes(self, element, attr):
        try:
            return element.get_attribute(attr)
        except AttributeError:
            return "Not available"


def amazonMe(head):
    print(f"Initiating the Amazon automation | Powered by Playwright.")
    amazon_dicts = []
    catchClause = TryExcept()

    user_input = str(input("Enter a URL:> "))    
    amazon_link_pattern = re.search("^https://www.amazon.com/s\?k=.*", user_input)
    if amazon_link_pattern != None:
        print(f"Invalid link. Please try proper Amazon link.")
        sys.exit()

    with sync_playwright() as play:
        browser = play.chromium.launch(headless=head, slow_mo=3*1000)
        page = browser.new_page(user_agent=userAgents())
        page.goto(user_input)

        page.wait_for_timeout(timeout=randomTime(4)*1000)

        ##################### XPATH selectors ###########################################################################################################
        search_name = "//span[@class='a-color-state a-text-bold']"
        total_page_number_first = "//span[@class='s-pagination-item s-pagination-disabled']"
        total_page_number_second = "//span[@class='s-pagination-strip']/a"
        next_button = "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']"

        main_content = "//div[@data-component-type='s-search-result']"

        hyperlink = "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']"
        price = "//span[@data-a-color='base']/span[@class='a-offscreen']"
        old_price = "//span[@data-a-color='secondary']/span[@class='a-offscreen']"
        review = "//span[@class='a-declarative']/a/i/span[@class='a-icon-alt']"
        review_count = "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style']/span[@class='a-size-base s-underline-text']"
        image = "//img[@class='s-image']"
        ###################################################################################################################################################

        product_name = re.sub(
            r"[^a-zA-Z0-9]", "", catchClause.text(page.query_selector(search_name))).capitalize()

        try:
            page.wait_for_selector(main_content, timeout=10*1000)
        except PlaywrightTimeoutError:
            print(f"Content loading error. Please try again in few minute.")

        try:
            last_page = page.query_selector(
                total_page_number_first).inner_text().strip()
        except AttributeError:
            last_page = page.query_selector_all(total_page_number_second)[-2].get_attribute('aria-label').split()[-1]

        print(f"Number of pages | {last_page}.")
        print(f"Scraping | {product_name}.")

        for click in range(int(last_page)):
            print(f"Scraping page | {click+1}")
            for content in page.query_selector_all(main_content):
                data = {
                    "Product": catchClause.text(content.query_selector(hyperlink)),
                    "ASIN": catchClause.attributes(content, 'data-asin'),
                    "Price": catchClause.text(content.query_selector(price)),
                    "Original price": catchClause.text(content.query_selector(old_price)),
                    "Review": catchClause.text(content.query_selector(review)),
                    "Review count": re.sub(r"[()]", "", catchClause.text(content.query_selector(review_count))),
                    "Hyperlinnk": f"""http://www.amazon.com{catchClause.attributes(content.query_selector(hyperlink), 'href')}""",
                    "Image": f"""{catchClause.attributes(content.query_selector(image), 'src')}""",
                }

                amazon_dicts.append(data)

            try:
                page.query_selector(next_button).click()
            except AttributeError:
                break

        browser.close()

    print(f"Scraping done. Now exporting to excel database.")

    df = pd.DataFrame(amazon_dicts)
    df.to_excel(f"{product_name}-Amazon database.xlsx", index=False)
    print(f"{product_name} Database is saved.")

