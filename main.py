from scrapers.scraper import Amazon
from apify import Actor
import asyncio
import os


if __name__ == '__main__':
    USER_ID = os.getenv('USER_ID')
    APIFY_TOKENS = os.getenv('APIFY_TOKENS')
    ACTOR_ID = os.getenv('ACTOR_ID')

    async def main():
        async with Actor:
            input = f'https://www.amazon.com/s?k=Jeans&rh=n%3A1040660%2Cn%3A1048188%2Cp_36%3A-5000&dc&ds=v1%3AZrh2YeJ%2Bmo6tc5p1QJD9idnCpBDTF2pKNTUbGqlhFKk&_encoding=UTF8&content-id=amzn1.sym.b0c3902d-ae70-4b80-8f54-4d0a3246745a&crid=1TZCO6ZC2HZVA&pd_rd_r=d2d812ec-1839-446b-b13c-080b49f2026c&pd_rd_w=SQ59S&pd_rd_wg=6taBx&pf_rd_p=b0c3902d-ae70-4b80-8f54-4d0a3246745a&pf_rd_r=MEEWY614NXBTSG4MW7R6&qid=1684823801&rnid=2941120011&sprefix=jeans%2Caps%2C155&ref=pd_gw_unk'

            status = await Amazon(input).status()

            if status == 503:
                return '503 response. Please try again later.'
            else:
                amazon = Amazon(input)
                datasets = await amazon.concurrent_scraping()
                # title = await amazon.category_name()
                await Actor.push_data(datasets)


    print(asyncio.run(main()))

