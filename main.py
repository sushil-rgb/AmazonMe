from mongo_database.mongo import export_to_mong
from tools.tool import rand_proxies
from scrapers.scraper import Amazon
import asyncio
import time


if __name__ == '__main__':


    async def main():
        base_url = "https://www.amazon.com/s?k=beauty&rh=p_36%3A-2500&_encoding=UTF8&content-id=amzn1.sym.f9836480-cfbe-4ad3-ad9c-168436b5cd55&pd_rd_r=e7f0b407-5d50-4304-9834-e16d45350a0d&pd_rd_w=YT9MX&pd_rd_wg=7MvkN&pf_rd_p=f9836480-cfbe-4ad3-ad9c-168436b5cd55&pf_rd_r=Z128GHCSZH9Y2B5ZM15K&ref=pd_gw_unk"
        status = await Amazon(base_url, None).status()

        if status == 503:
            return "503 response. Please try again later."
        # Type True if you want to export to CSV and avoid MongoDB
        csv = True
        # Type True if you want to use proxy:
        proxy = False
        if csv:
            if proxy:
                amazon = Amazon(base_url, None)
                return await amazon.export_csv()
            else:
                amazon = Amazon(base_url, f"http://{rand_proxies()}")
                return await amazon.export_csv()
        else:
            if proxy:
                mongo_to_db = await export_to_mong(base_url, f"http://{rand_proxies()}")
            else:
                mongo_to_db = await export_to_mong(base_url, None)
            return mongo_to_db


    # Start the timer to measure how long the wb scraping process takes
    start_time = time.time()
    # Run the async main function and run the scraper:
    results = asyncio.run(main())
    end_time = time.time()
    print(results)
    # Calculate and print the total time taken to scrape the data:D
    execution_time = round(end_time - start_time, 2)
    print(f"Took {execution_time} seconds | {round(execution_time / 60, 2)} minutes.")

