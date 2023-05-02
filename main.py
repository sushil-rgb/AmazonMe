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
        
        base_url = """https://www.amazon.com/s?k=work+from+home+fitness&i=sporting&rh=n%3A3375251%2Cn%3A3407731&dc&ds=v1%3AFcBqeddkI8AFCsoSZa8Pcj75OeujOS6gJL5Jqk26XOo&pd_rd_r=31755823-b564-461f-b957-a300b2ebf1a6&pd_rd_w=L9EK6&pd_rd_wg=yzOjA&pf_rd_p=2c73d1ae-9178-422f-ae3b-1b5628bd95bb&pf_rd_r=P6G2816X5D6F883T5QNY&qid=1683019252&ref=sr_ex_n_1"""
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

