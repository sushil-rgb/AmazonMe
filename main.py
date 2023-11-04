from scrapers.scraper import Amazon
from apify import Actor
import asyncio
import os


if __name__ == '__main__':
    USER_ID = os.getenv('USER_ID')
    APIFY_TOKENS = os.getenv('API_TOKENS')
    ACTOR_ID = os.getenv('ACTOR_ID')

    async def main():
        async with Actor:
            input = f'https://api.apify.com/v2/acts/{ACTOR_ID}/runs/last/dataset/items?token={APIFY_TOKENS}'

            status = await Amazon(input).status()

            if status == 503:
                return '503 response. Please try again later.'
            else:
                amazon = Amazon(input)
                datasets = await amazon.concurrent_scraping()
                title = await amazon.category_name()
                await Actor.push_data({'Products': datasets, 'title': title})


    print(asyncio.run(main()))

