from mongo_database.mongo import export_to_mong, mongo_to_sheet
from scrapers.scraper import Amazon
from tools.tool import static_connection, rand_proxies
import asyncio
import time

# print(userAgents())



if __name__ == '__main__':


    async def main():
        base_url = "https://www.amazon.com/s?k=gaming+keyboard&pd_rd_r=1ae898eb-29e4-4b07-ba33-4ab28d4405bc&pd_rd_w=CZSEz&pd_rd_wg=lvwa6&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=RP6GNKB5E9P9NPSCS5JJ&ref=pd_gw_unk"
        mongo_to_db = await export_to_mong(base_url)
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

