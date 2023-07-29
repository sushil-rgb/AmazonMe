from mongo_database.mongo import export_to_mong
from tools.tool import rand_proxies
import asyncio
import time


if __name__ == '__main__':


    async def main():
        # return rand_proxies()
        base_url = "https://www.amazon.com/s?k=Spring+Jackets&i=fashion-womens&rh=n%3A7141123011&dc&ds=v1%3ABk6NhBRoKfacSsRLqyE%2Fkk6gHCfOi4WHp6oHpf1ajaY&_encoding=UTF8&content-id=amzn1.sym.b4114be9-6d3d-4aed-8b31-fcbf38a83486&crid=28AAZ2JDZCYX1&pd_rd_r=5b632487-9047-466f-8b75-4982d6db5e25&pd_rd_w=9WUr6&pd_rd_wg=3TU7l&pf_rd_p=b4114be9-6d3d-4aed-8b31-fcbf38a83486&pf_rd_r=A1VMNJS2YNT401B381SH&qid=1690625319&sprefix=spring+jackets%2Caps%2C140&ref=sr_ex_n_1"
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

