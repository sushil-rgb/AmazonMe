from scrapers.scraper import Amazon
from apify import Actor
import asyncio


if __name__ == '__main__':


    async def main():
        async with Actor:
            input = "https://www.amazon.com/s?k=home+decor&i=handmade-home-and-kitchen&rh=n%3A11434601011%2Cp_n_material_browse%3A11602977011%2Cp_n_style_browse-bin%3A11603046011&lo=image&dc&content-id=amzn1.sym.328133bb-2d2c-4429-bd3e-bcd9fc29f103%3Aamzn1.sym.328133bb-2d2c-4429-bd3e-bcd9fc29f103&pd_rd_r=6753b1ca-b589-46c0-9153-b65c30d03b5e&pd_rd_w=9BDpm&pd_rd_wg=RQNrh&pf_rd_p=328133bb-2d2c-4429-bd3e-bcd9fc29f103&pf_rd_r=49S4H4Z7W4ENHA44BD17&qid=1699127010&rnid=11603043011&ref=sr_nr_p_n_style_browse-bin_1&ds=v1%3AB%2FFVShSFXhSfiz4h%2BiyN4C6pJk3EKMNw0Wwaz%2B6bdXs"

            status = await Amazon().status()

            if status == 503:
                return '503 response. Please try again later.'
            else:
                amazon = Amazon(input)
                datasets = await amazon.concurrent_scraping()
                title = await amazon.category_name()
                await Actor.push_data({'Products': datasets, 'title': title})


    print(asyncio.run(main()))

