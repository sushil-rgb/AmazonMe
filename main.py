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
            input = f'https://www.amazon.com/s?k=home+decor&rh=p_36%3A-5000&_encoding=UTF8&content-id=amzn1.sym.f7def1d9-177b-415d-89b3-9d866650f7d7&pd_rd_r=73b9a32d-328c-4b5e-8ad1-1d20f4186b3b&pd_rd_w=zJqQU&pd_rd_wg=NcDHj&pf_rd_p=f7def1d9-177b-415d-89b3-9d866650f7d7&pf_rd_r=FA9YHY1T5QTM2HRG9QP5&ref=pd_gw_unk'

            status = await Amazon(input).status()

            if status == 503:
                return '503 response. Please try again later.'
            else:
                amazon = Amazon(input)
                datasets = await amazon.concurrent_scraping()
                # title = await amazon.category_name()
                await Actor.push_data(datasets)


    print(asyncio.run(main()))

