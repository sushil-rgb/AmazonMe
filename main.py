from mongo_database.mongo import export_to_mong
from tools.tool import rand_proxies
from scrapers.scraper import Amazon
import asyncio
import time


if __name__ == '__main__':


    async def main():
        base_url = "https://www.amazon.com/s?i=toys-and-games&bbn=165793011&rh=n%3A165793011%2Cp_36%3A-3000&dc&_encoding=UTF8&content-id=amzn1.sym.eb39b83d-c690-496d-9f16-0a9bd66ca6c8&pd_rd_r=db10c08d-805f-4eb2-8215-6db7244dfd33&pd_rd_w=U10YV&pd_rd_wg=XWFTR&pf_rd_p=eb39b83d-c690-496d-9f16-0a9bd66ca6c8&pf_rd_r=1B8D3BHD1HB21JDP9X4B&qid=1663255924&rnid=386491011&ref=pd_gw_unk"
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

