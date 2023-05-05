from scrapers.scraper import Amazon
import asyncio
import time


if __name__ == '__main__':  
    # Start the timer to measure how long the wb scraping process takes
    start_time = time.time()
        
        
    async def main():
        # While it is possible to reduce the time interval for faster scraping, I would advise against doing so as this could potentially overload the server and result in Amazon blocking your IP address.
        # Default time-interval ranges from (2 to 5 minutes). Scrape responsibly:
        sleep = 5 * 60    
        
        base_url = """https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A3011391011%2Cn%3A172470&dc&ds=v1%3A8N2eRjOSpZiOYgwKFB6ym9syZpPZhKxcxu%2FHnziiHyw&qid=1683035856&rnid=3011391011&ref=sr_nr_n_1"""
        amazon = Amazon()            
        
        datas = await amazon.concurrent_scraping(sleep, base_url)
        return datas
        

    # Run the async main function and run the scraper:
    print(asyncio.run(main()))

    # Calculate and print the total time taken to scrape the data:D
    total_time = round(time.time()-start_time, 2)
    time_in_secs = round(total_time)
    time_in_mins = round(total_time/60)

    print(f"Took {time_in_secs} seconds | {time_in_mins} minutes.")

