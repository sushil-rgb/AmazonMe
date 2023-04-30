from scrapers.scraper import Amazon
import asyncio
import time


if __name__ == '__main__':    
    
    
    # Define an async main functio that runs the web scraper:
    async def main():
        # Instantiate an Amazon object:
        amazon = Amazon()
        
        # Define the URL to scrape:
        userInput = "https://www.amazon.com/s?k=gaming+keyboard&rh=n%3A402051011&dc&ds=v1%3AmQ2bbJkh8OLoIWrFEACV3bSUJZPf%2FZg2CsMgtTXggLk&pd_rd_r=f0581525-9ff7-456e-b6df-0dadac916753&pd_rd_w=ebVVQ&pd_rd_wg=LvfFA&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=K1S9Y5GB9QVBF7VWCAKM&qid=1682867151&rnid=2941120011&ref=sr_nr_n_1"
        
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

