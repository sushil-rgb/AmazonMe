from functionalities.tools import randomTime, verify_amazon, export_to_sheet
from scrapers.scraper import Amazon
import pandas as pd
import asyncio
import time


if __name__ == '__main__':  
    # Start the timer to measure how long the wb scraping process takes
    start_time = time.time()
        
        
    async def main():
        # You can decrease the time-interval, however I discourage you to do say as the action may overload the server and Amazon may block your IP address
        sleep = 20
        base_url = "https://www.amazon.com/s?i=specialty-aps&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A1040658&ref=nav_em__nav_desktop_sa_intl_clothing_0_2_13_2"
        amazon = Amazon()
        
        if await verify_amazon(base_url):
            return "Invalid link. Please try proper amazon link product category of your choice."
        
        # Pull the number of pages of the category
        number_pages = await amazon.num_of_pages(base_url)
        print(f"Total pages || {number_pages}.")
        
        await asyncio.sleep(sleep)
        
        searches = await amazon.search_results(base_url)
        print(f"Scraping category || {searches}.")
        
        # Split the pagination and convert it list of urls
        url_lists = await amazon.split_url(base_url)        
        
        print(f"Initiating the Extraction.")
        coroutines = [amazon.scrape_and_save(sleep, url) for url in url_lists]
        dfs = await asyncio.gather(*coroutines)
        results = pd.concat(dfs)
        
        await export_to_sheet(results, searches)
        

    # Run the async main function and run the scraper:
    print(asyncio.run(main()))

    # Calculate and print the total time taken to scrape the data:D
    total_time = round(time.time()-start_time, 2)
    time_in_secs = round(total_time)
    time_in_mins = round(total_time/60)

    print(f"Took {time_in_secs} seconds | {time_in_mins} minutes.")

