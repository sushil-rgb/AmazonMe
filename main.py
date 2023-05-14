from scrapers.scraper import Amazon
from tools.tool import verify_amazon
import asyncio
import time


if __name__ == '__main__':          
    
        
    async def main():
        # While it is possible to reduce the time interval for faster scraping, I would advise against doing so as this could potentially overload the server and result in Amazon blocking your IP address.
        # Default time-interval ranges from (2 to 5 minutes). Scrape responsibly:
        sleep = 10 * 60
        
        base_url = "https://www.amazon.com/s?i=stripbooks&bbn=1000&rh=n%3A283155%2Cn%3A3&dc&fs=true&ds=v1%3AquYJ%2FdhELcWi%2FDjm7W%2FF6XW0CiUJcVO%2Frp%2FnKP%2BJp2A&qid=1684055913&rnid=1000&ref=sr_nr_n_3"
        
        amazon = Amazon()      
        datas = await amazon.concurrent_scraping(sleep, base_url)
        
        return datas 
    
    
    # Start the timer to measure how long the wb scraping process takes
    start_time = time.time()
    
    # Run the async main function and run the scraper:
    results = asyncio.run(main())
    end_time = time.time()     

    print(results)
    
    # Calculate and print the total time taken to scrape the data:D
    execution_time = round(end_time - start_time, 2)    
    print(f"Took {execution_time} seconds | {round(execution_time / 60, 2)} minutes.")       
        
        