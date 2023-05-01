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
        
        base_url = "https://www.amazon.com/s?k=gaming+laptops&rh=n%3A565108&dc&ds=v1%3AZn7LVZmG1FzeUynGJkMc9NgpLjSEtjqo7e4JEg0ky%2B8&pf_rd_i=23508887011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=434db2ed-6d53-4c59-b173-e8cd550a2e4f&pf_rd_r=ZPW1PS5X1DPJQWGRXWKD&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1682970011&rnid=2941120011&ref=sr_nr_n_1"
        amazon = Amazon()
        
        if await verify_amazon(base_url):
            return "I'm sorry, the link you provided is invalid. Could you please provide a valid Amazon link for the product category of your choice?"
        
        print(f"-----------------------Welcome to Amazon crawler---------------------------------")
        
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
        
        print(f"The extraction process has begun and is currently in progress. The web scraper is scanning through all the links and collecting relevant information. Please be patient while the data is being gathered.")
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

