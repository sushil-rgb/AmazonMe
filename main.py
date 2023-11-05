from scrapers.scraper import Amazon
from apify import Actor
import asyncio


if __name__ == '__main__':


    async def main():
        try:
            async with Actor:
                input_data = await Actor.get_input()
                url = input_data.get('url')
                status = await Amazon(url).status()

                if status == 503:
                    return '503 response. Please try again later.'
                else:
                    amazon = Amazon(url)
                    datasets = await amazon.concurrent_scraping()
                    await Actor.push_data({'Products': datasets})
        except Exception as e:
            print(f'WebSocket connection error: {e}')


    print(asyncio.run(main()))

