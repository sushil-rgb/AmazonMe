from mongo_database.mongo import export_to_mong, mongo_to_sheet
from scrapers.scraper import Amazon
import asyncio
import time


if __name__ == '__main__':


    async def main():
        base_url = "https://www.amazon.com/s?k=gaming+headsets&pd_rd_r=3451eb38-d298-415e-a0ef-c99803200fc1&pd_rd_w=vfDtz&pd_rd_wg=fTTTg&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=SY310NXETBG5Q31FYM2F&ref=pd_gw_unk"
        # amzn = Amazon()
        # return await amzn.scrape_data(base_url)
        mongo_to_db = await export_to_mong(base_url)
        # sheet_name = "Dinner Plates"  # Please use the name of the collection in your MongoDB database to specify the name of the spreadsheet you intend to export.
        # # sheets = await mongo_to_sheet(sheet_name)  # Uncomment this to export to excel database.
        # # return sheets
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

