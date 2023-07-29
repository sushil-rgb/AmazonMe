from mongo_database.mongo import export_to_mong
from tools.tool import rand_proxies
import asyncio
import time


if __name__ == '__main__':


    async def main():
        # return rand_proxies()
        base_url = "https://www.amazon.com/s?k=gaming+laptops&i=computers&rh=n%3A565108%2Cp_n_feature_browse-bin%3A23760604011%2Cp_89%3AASUS%7CDell&dc&pf_rd_i=23508887011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=434db2ed-6d53-4c59-b173-e8cd550a2e4f&pf_rd_r=DTVBSAXM7V8FZHKX345V&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1690628261&rnid=2528832011&ref=sr_nr_p_89_3&ds=v1%3AMeHfsSAH4YAGjb8wbReGtqEAB1Hy7p58P6ccweMULG4"
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

