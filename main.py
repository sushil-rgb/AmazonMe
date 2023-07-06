from mongo_database.mongo import export_to_mong
import asyncio
import time


if __name__ == '__main__':


    async def main():
        base_url = "https://www.amazon.com/s?k=Dinnerware+%26+accessories&rh=n%3A284507%2Cn%3A367155011&dc&ds=v1%3AYjiGQ92N5boPICF0lGxs8%2BHfhbxCKGqThae99X5xlak&crid=IBML6MYDLJ4A&pd_rd_r=d7f8c442-11ba-4bba-8382-9b2832436b2b&pd_rd_w=T81wA&pd_rd_wg=oa9mB&pf_rd_p=c0480761-6b7c-400b-bca5-28ff417248d1&pf_rd_r=V1F3KQQVXDJGHS8A3MAQ&qid=1688628736&rnid=2941120011&sprefix=dinnerware+%26+accessorie%2Caps%2C190&ref=sr_nr_n_5"
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

