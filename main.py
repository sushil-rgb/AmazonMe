from mongo import export_to_mong, export_to_sheet
import asyncio
import time


if __name__ == '__main__':          
    
        
    async def main():
        # While it is possible to reduce the time interval for faster scraping, I would advise against doing so as this could potentially overload the server and result in Amazon blocking your IP address.
        # Default time-interval ranges from (2 to 5 minutes). Scrape responsibly:
        # sleep = 1 * 60
        
        base_url = "https://www.amazon.com/s?k=Knits+clothing&crid=23OTKP0I0AQDD&pd_rd_r=cdb0b781-3395-4f1d-b1ca-be09bae8b440&pd_rd_w=fOkVl&pd_rd_wg=INv7H&pf_rd_p=b4114be9-6d3d-4aed-8b31-fcbf38a83486&pf_rd_r=B88MMHMZZ45RP5A0AQ2T&sprefix=knits+clothing%2Caps%2C147&ref=pd_gw_unk"
        # amazon = Amazon() 
        
        # # Below script checks if the Amazon is a Deal (goldbox) URL:
        # if 'gp' in base_url:
        #     urls = await amazon.goldbox(base_url)            
        #     datas = await amazon.concurrent_scraping_gb(urls)
        #     return datas
        # else:
        #     datas = await amazon.concurrent_scraping(sleep, base_url)     
        mongo_to_db = await export_to_mong(base_url)     
        # mongo_to_sheets = await export_to_sheet("s")     
        return mongo_to_db  
    
    
    # Start the timer to measure how long the wb scraping process takes
    start_time = time.time()
    
    # Run the async main function and run the scraper:
    results = asyncio.run(main())
    end_time = time.time()     

    print(results)
    
    # Calculate and print the total time taken to scrape the data:D
    execution_time = round(end_time - start_time, 2)    
    print(f"Took {execution_time} seconds | {round(execution_time / 60, 2)} minutes.")       
        
        