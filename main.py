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
        # Default time-interval ranges from (30 seconds to 2 minutes). Scrape responsibly:
        sleep = 2 * 60    
        
        base_url = "https://www.amazon.com/s?i=specialty-aps&bbn=4954955011&rh=n%3A4954955011%2Cn%3A%212617942011%2Cn%3A378733011&ref=nav_em__nav_desktop_sa_intl_crafting_0_2_8_4"
        amazon = Amazon()
        
        if await verify_amazon(base_url):
            return "I'm sorry, the link you provided is invalid. Could you please provide a valid Amazon link for the product category of your choice?"
        
        print(f"-----------------------Welcome to Amazon scraper---------------------------------")
        
        await asyncio.sleep(2)
        
        searches = await amazon.search_results(base_url)
        print(f"Scraping category || {searches}.")
        
        await asyncio.sleep(2)
        # Pull the number of pages of the category       
        number_pages = await amazon.num_of_pages(base_url)
        print(f"Total pages || {number_pages}.")
        
        await asyncio.sleep(2)        
        
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

