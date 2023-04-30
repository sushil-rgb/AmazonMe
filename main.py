from scrapers.scraper import Amazon
import asyncio
import time


if __name__ == '__main__':    
    
    
    # Define an async main functio that runs the web scraper:
    async def main():
        # Instantiate an Amazon object:
        amazon = Amazon()
        
        # Define the URL to scrape:
        userInput = "https://www.amazon.com/s?k=health+and+beauty&i=beauty-intl-ship&bbn=16225006011&rh=n%3A11062741&dc&ds=v1%3AaTUGn90NLjQvoihGF3%2FqZ1jr%2FIFcsvhBnS3xK%2FaJ3u0&crid=2036DM6EKNYNA&pd_rd_r=fa4603d4-0acc-4de5-a94e-3f047374ec2e&pd_rd_w=LUiIR&pd_rd_wg=yiJls&pf_rd_p=c9097eb6-837b-4ba7-94d7-51428f6e8d2a&pf_rd_r=6W2WTX74X54Y6G5DMXQQ&qid=1682875043&rnid=16225006011&sprefix=health+and+beauty%2Cbeauty-intl-ship%2C173&ref=sr_nr_n_6"
        
        # Split the pagination into URLs 
        split_links = await amazon.split_url(userInput)            
        
        # Define the time interval between scraping requests
        time_interval = 3
        datas = await amazon.amazonMe(time_interval, split_links)
        return datas
    
    
    # Start the timer to measure how long the wb scraping process takes
    start_time = time.time()

    # Run the async main function and run the scraper:
    print(asyncio.run(main()))

    # Calculate and print the total time taken to scrape the data:D
    total_time = round(time.time()-start_time, 2)
    time_in_secs = round(total_time)
    time_in_mins = round(total_time/60)

    print(f"Took {time_in_secs} seconds | {time_in_mins} minutes.")

