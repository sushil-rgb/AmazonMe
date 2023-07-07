from mongo_database.mongo import export_to_mong, mongo_to_sheet
from scrapers.scraper import Amazon
import asyncio
import time


if __name__ == '__main__':


    async def main():
        base_url = "https://www.amazon.com/s?k=sexy+dresses&rh=n%3A1045024%2Cn%3A11006703011&dc&ds=v1%3A%2B%2B%2BeqnlN6RopN%2BQAazKtqRPqLIORlC%2FwkWAKUFM%2B9Kc&qid=1688721535&rnid=2941120011&ref=sr_nr_n_4"
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

