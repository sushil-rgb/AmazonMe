from scrapers.scraper import Amazon
import asyncio
import time


if __name__ == '__main__':          
    
        
    async def main():
        # While it is possible to reduce the time interval for faster scraping, I would advise against doing so as this could potentially overload the server and result in Amazon blocking your IP address.
        # Default time-interval ranges from (2 to 5 minutes). Scrape responsibly:
        sleep = 10 * 60
        
        base_url = "https://www.amazon.com/s?k=Shoes&rh=p_36%3A-5000&crid=1QEZIUFPCL3YZ&pd_rd_r=66a979bf-9714-4313-a90b-11286642a632&pd_rd_w=w9b6r&pd_rd_wg=pXpiE&pf_rd_p=cdad119c-551b-402b-9f9e-1171c44ec6fa&pf_rd_r=11F7T2122FY54A4EXE26&qid=1684823927&rnid=2661611011&sprefix=shoes%2Caps%2C145&ref=pd_gw_unk"
        
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
        
        