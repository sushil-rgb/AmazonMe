from scrapers.scraper import Amazon
from tools.tool import verify_amazon
import asyncio
import time


if __name__ == '__main__':          
    
        
    async def main():
        # While it is possible to reduce the time interval for faster scraping, I would advise against doing so as this could potentially overload the server and result in Amazon blocking your IP address.
        # Default time-interval ranges from (2 to 5 minutes). Scrape responsibly:
        sleep = 10 * 60
        
        base_url = "https://www.amazon.com/s?k=Home&i=kitchen-intl-ship&crid=1QBODY970JKYC&pd_rd_r=b267967b-3f42-4fb9-99a3-c67d84414b1e&pd_rd_w=sRda0&pd_rd_wg=ysq5U&pf_rd_p=c9097eb6-837b-4ba7-94d7-51428f6e8d2a&pf_rd_r=C6SGM2A5M594847FZDVC&sprefix=home%2Ckitchen-intl-ship%2C164&ref=pd_gw_unk"
        
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
        
        