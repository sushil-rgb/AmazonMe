from scrapers.scraper import Amazon
from apify import Actor
import asyncio


if __name__ == '__main__':


    async def main():
        async with Actor:
            input_data = await Actor.get_input()
            status = await Amazon(input_data).status()

            if status == 503:
                return '503 response. Please try again later.'
            else:
                amazon = Amazon(input_data)
                datasets = await amazon.concurrent_scraping()
                title = await amazon.category_name()
                await Actor.push_data({'Products': datasets, 'title': title})


    print(asyncio.run(main()))

