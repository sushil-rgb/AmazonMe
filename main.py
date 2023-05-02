from functionalities.tools import verify_amazon, export_to_sheet
from scrapers.scraper import Amazon
import pandas as pd
import asyncio
import time


if __name__ == '__main__':  
    # Start the timer to measure how long the wb scraping process takes
    start_time = time.time()
        
        
    async def main():
        # While it is possible to reduce the time interval for faster scraping, I would advise against doing so as this could potentially overload the server and result in Amazon blocking your IP address.
        # Default time-interval ranges from (2 to 5 minutes). Scrape responsibly:
        sleep = 5 * 60    
        
        base_url = """https://www.amazon.com/s?k=toys&rh=n%3A165793011%2Cp_lbr_characters_browse-bin%3AMarvel&s=date-desc-rank&dc&ds=v1%3A%2FeymYW%2FsRcJHKpJ5thadssumCt46%2BYpL8ZSuUFudxQs&pd_rd_r=31755823-b564-461f-b957-a300b2ebf1a6&pd_rd_w=lWA8X&pd_rd_wg=yzOjA&pf_rd_p=779cadfb-bc4d-465d-931f-0b68c1ba5cd5&pf_rd_r=P6G2816X5D6F883T5QNY&qid=1683017903&rnid=3296952011&ref=sr_nr_p_lbr_characters_browse-bin_1"""
        amazon = Amazon()
        return await amazon.search_results(base_url)
        datas = await amazon.concurrent_scraping(sleep, base_url)
        return datas
        

    # Run the async main function and run the scraper:
    print(asyncio.run(main()))

    # Calculate and print the total time taken to scrape the data:D
    total_time = round(time.time()-start_time, 2)
    time_in_secs = round(total_time)
    time_in_mins = round(total_time/60)

    print(f"Took {time_in_secs} seconds | {time_in_mins} minutes.")

