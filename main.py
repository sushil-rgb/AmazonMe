from mongo_database.mongo import export_to_mong
from tools.tool import rand_proxies, static_connection
from scrapers.scraper import Amazon
import asyncio
import time


if __name__ == '__main__':


    async def main():
        # return rand_proxies()
        base_url = "https://www.amazon.co.jp/AmazonBasics-DisplayPort-Converter-Cable-Monitors/dp/B015OW3M1W?ref_=ast_sto_dp&th=1&psc=1"
        # Type True if you want to use proxy:
        proxy = False
        if proxy:
            mongo_to_db = await export_to_mong(base_url, f"http://{rand_proxies()}")
        else:
            mongo_to_db = await export_to_mong(base_url, None)
        # sheet_name = "Dinner Plates"  # Please use the name of the collection in your MongoDB database to specify the name of the spreadsheet you intend to export.
        # sheets = await mongo_to_sheet(sheet_name)  # Uncomment this to export to excel database.
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

