from scrapers.scraper import Amazon
from tools.tool import verify_amazon
import asyncio
import time


if __name__ == '__main__':          
    
        
    async def main():
        # While it is possible to reduce the time interval for faster scraping, I would advise against doing so as this could potentially overload the server and result in Amazon blocking your IP address.
        # Default time-interval ranges from (2 to 5 minutes). Scrape responsibly:
        sleep = 5 * 60
        
        base_url = "https://www.amazon.com/s?k=Nintendo+Switch+Games&rh=n%3A16227133011&pf_rd_i=23508887011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=434db2ed-6d53-4c59-b173-e8cd550a2e4f&pf_rd_r=MG60RM4M4REFVTTRWYCZ&pf_rd_s=merchandised-search-5&pf_rd_t=101&ref=nb_sb_noss"
        
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
        
        