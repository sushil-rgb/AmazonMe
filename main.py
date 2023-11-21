from mongo_database.mongo import export_to_mong
from tools.tool import rand_proxies
from scrapers.scraper import Amazon
import asyncio
import time


if __name__ == '__main__':


    async def main():
        base_url = "https://www.amazon.com.br/s?rh=n%3A19778000011&fs=true&ref=lp_19778000011_sar"
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

