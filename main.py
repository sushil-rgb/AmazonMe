from mongo_database.mongo import export_to_mong
from tools.tool import rand_proxies
import asyncio
import time


if __name__ == '__main__':


    async def main():
        base_url = "https://www.amazon.com/s?k=gaming+chairs&i=garden&rh=n%3A1055398%2Cn%3A1063306%2Cn%3A5422303011%2Cn%3A18682062011&dc&ds=v1%3A6C33Jx3qghkZt9FgtjwYLvNSdAVYdD2CbpN1UcegjMQ&_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&pd_rd_r=a91a7a20-da5a-48f7-8214-9046f53ad170&pd_rd_w=HKqeM&pd_rd_wg=KsApY&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=C9JBDEB8Q5ENT0D7R08W&qid=1690656560&ref=sr_ex_n_1"
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

