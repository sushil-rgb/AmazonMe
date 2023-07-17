from mongo_database.mongo import export_to_mong, mongo_to_sheet
import asyncio
import time


if __name__ == '__main__':


    async def main():
        base_url = "https://www.amazon.com/s?i=garden&rh=n%3A1055398&dc&fs=true&ds=v1%3AFhPh6ZQUQWvPWc2o2%2BwLBuzuFA7Ltc61eXt5b0NMrXE&qid=1689611383&ref=sr_ex_n_1"
        mongo_to_db = await export_to_mong(base_url)
        # sheet_name = "Dinner Plates"  # Please use the name of the collection in your MongoDB database to specify the name of the spreadsheet you intend to export.
        # # sheets = await mongo_to_sheet(sheet_name)  # Uncomment this to export to excel database.
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

