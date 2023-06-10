from scrapers.scraper import Amazon
import asyncio
import time


if __name__ == '__main__':          
    
        
    async def main():
        # While it is possible to reduce the time interval for faster scraping, I would advise against doing so as this could potentially overload the server and result in Amazon blocking your IP address.
        # Default time-interval ranges from (2 to 5 minutes). Scrape responsibly:
        sleep = 10 * 60
        
        base_url = "https://www.amazon.com/gp/goldbox?deals-widget=%257B%2522version%2522%253A1%252C%2522viewIndex%2522%253A0%252C%2522presetId%2522%253A%25224E5C9DB973738BFCB9FE3802733596E7%2522%252C%2522departments%2522%253A%255B%25223760911%2522%252C%2522283155%2522%255D%252C%2522sorting%2522%253A%2522FEATURED%2522%257D"
        amazon = Amazon() 
        
        # Below script checks if the Amazon is a Deal (goldbox) URL:
        if 'gp' in base_url:
            urls = await amazon.goldbox(base_url)            
            datas = await amazon.concurrent_scraping_gb(urls)
            return datas
        else:
            datas = await amazon.concurrent_scraping(sleep, base_url)                     
    
    
    # Start the timer to measure how long the wb scraping process takes
    start_time = time.time()
    
    # Run the async main function and run the scraper:
    results = asyncio.run(main())
    end_time = time.time()     

    print(results)
    
    # Calculate and print the total time taken to scrape the data:D
    execution_time = round(end_time - start_time, 2)    
    print(f"Took {execution_time} seconds | {round(execution_time / 60, 2)} minutes.")       
        
        