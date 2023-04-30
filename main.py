import os
import sys
import time
import asyncio

from functionalities.tools import verify_amazon

sys.path.append(os.getcwd())
from scrapers.scraper import Amazon


if __name__ == '__main__':
    # Make False if you want to see the live automation.
    make_headless = True
    
    
    async def main():        
        userInput = "https://www.amazon.com/s?k=pet+supplies&s=date-desc-rank&crid=3IF5TSVMY5YRB&pd_rd_r=1d0e730c-a5ac-4cf1-81c4-c5dc08935339&pd_rd_w=DxSyR&pd_rd_wg=Qfftc&pf_rd_p=ab475c0d-7817-4703-9d6d-f003bf2156bf&pf_rd_r=5V5JYYGATNCEKDE7ZJYZ&qid=1632868254&sprefix=pet+sup%2Caps%2C268&ref=pd_gw_unk"
        time_interval = 5
        datas = await Amazon().amazonMe(time_interval, make_headless, userInput)
        return datas
    
    
    start_time = time.time()

    print(asyncio.run(main()))

    total_time = round(time.time()-start_time, 2)
    time_in_secs = round(total_time)
    time_in_mins = round(total_time/60)

    print(f"Took {time_in_secs} seconds | {time_in_mins} minutes.")

