from apify import Actor
from tools.tool import rand_proxies
from scrapers.scraper import Amazon



if __name__ == '__main__':


    async def main():
        async with Actor:
            input = await Actor.get_input()
            status = await Amazon(input).status()

            if status == 503:
                return '503 response. Please try again later.'
            else:
                amazon = Amazon(input)
                datasets = await amazon.concurrent_scraping()
                title = await amazon.category_name()
                await Actor.push_data({'Products': datasets, 'title': title})

