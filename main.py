from scrapers.scraper import Amazon
from apify import Actor
import asyncio


if __name__ == '__main__':


    async def main():
        async with Actor:
            # input_data = await Actor.get_input()
            url = "https://www.amazon.com/s?k=toys&rh=p_36%3A-2500&_encoding=UTF8&content-id=amzn1.sym.44da4965-9668-4613-bec2-a3a75f0c2ad4&pd_rd_r=948831c6-7837-4a26-a075-054f6ba6391e&pd_rd_w=rzz1M&pd_rd_wg=rtU6v&pf_rd_p=44da4965-9668-4613-bec2-a3a75f0c2ad4&pf_rd_r=2MRC4DNSXHB0YQ7YKDAZ&ref=pd_gw_unk"
            status = await Amazon(url).status()

            if status == 503:
                return '503 response. Please try again later.'
            else:
                amazon = Amazon(url)
                datasets = await amazon.concurrent_scraping()
                title = await amazon.category_name()
                await Actor.push_data({'Products': datasets, 'title': title})


    print(asyncio.run(main()))

