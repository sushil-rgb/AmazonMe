from mongo_database.mongo import export_to_mong, mongo_to_sheet
from tools.tool import static_connection, retry_request, rand_proxies
from scrapers.scraper import Amazon
import asyncio
import time

# print(userAgents())



if __name__ == '__main__':


    async def main():
        base_url = "https://www.amazon.com/s?k=Jeans&rh=n%3A1040660%2Cn%3A1048188%2Cp_36%3A-5000&ds=v1%3AZrh2YeJ%2Bmo6tc5p1QJD9idnCpBDTF2pKNTUbGqlhFKk&crid=1TZCO6ZC2HZVA&pd_rd_r=05c15343-c72f-4978-a8a1-1d2b10979fd7&pd_rd_w=PFA16&pd_rd_wg=rWgND&pf_rd_p=b0c3902d-ae70-4b80-8f54-4d0a3246745a&pf_rd_r=6ZRR60HE1056ZC3CNW6V&qid=1684823801&rnid=2941120011&sprefix=jeans%2Caps%2C155&ref=pd_gw_unk"
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

