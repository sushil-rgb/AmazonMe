from scrapers.scraper import Amazon
from apify import Actor
import asyncio
import os


if __name__ == '__main__':


    async def main():
        async with Actor:
            input_data = await Actor.get_input()
            url = input_data['url']['prefill']
            status = await Amazon(url).status()

            if status == 503:
                return '503 response. Please try again later.'
            else:
                amazon = Amazon(url)
                datasets = await amazon.concurrent_scraping()
                title = await amazon.category_name()
                await Actor.push_data({'Products': datasets, 'title': title})


    print(asyncio.run(main()))

