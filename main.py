from apify import Actor
from scrapers.scraper import Amazon



if __name__ == '__main__':


    async def main():
        async with Actor:
            input = await Actor.get_input()
            status = await Amazon(input, None).status()

            if status == 503:
                return '503 response. Please try again later.'
            else:
                amazon = Amazon(input, None)
                datasets = await amazon.scrape_product_info(input['url'])
                await Actor.push_data(datasets)


