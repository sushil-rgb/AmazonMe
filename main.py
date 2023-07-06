from mongo_database.mongo import export_to_mong
import asyncio
import time


if __name__ == '__main__':


    async def main():
        base_url = "https://www.amazon.com/s?i=electronics&bbn=1266092011&rh=n%3A172282%2Cn%3A1266092011%2Cn%3A172659&field-shipping_option-bin=3242350011&pf_rd_i=16225009011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=85a9188d-dbd5-424e-9512-339a1227d37c&pf_rd_r=QAXJDW5692A2A6XJ3KFY&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1588978526&rnid=1266092011&ref=sr_nr_n_13"
        mongo_to_db = await export_to_mong(base_url)
        sheet_name = "Dinnerware & accessories"  # Please use the name of the collection in your MongoDB database to specify the name of the spreadsheet you intend to export.
        # sheets = await mongo_to_sheet(sheet_name)  # Uncomment this to export to excel database.
        # return sheets
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

