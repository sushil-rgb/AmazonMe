from mongo_database.mongo import export_to_mong, mongo_to_sheet
from scrapers.scraper import Amazon
import asyncio
import time


if __name__ == '__main__':


    async def main():
        base_url = "https://www.amazon.com/s?k=Shoes&rh=p_36%3A-5000&crid=1QEZIUFPCL3YZ&pd_rd_r=f9174b12-d1e3-491c-8faa-358847a9ccfa&pd_rd_w=i0kWf&pd_rd_wg=ipulU&pf_rd_p=b0c3902d-ae70-4b80-8f54-4d0a3246745a&pf_rd_r=7P47VRB2WZ3PNW2MTV59&qid=1684823927&rnid=2661611011&sprefix=shoes%2Caps%2C145&ref=pd_gw_unk"
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

