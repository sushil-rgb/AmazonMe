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
        userInput = "https://www.amazon.com/s?k=gaming+mouse&rh=n%3A402052011%2Cp_n_feature_fifteen_browse-bin%3A23974318011&dc&ds=v1%3A0zO58sX6fcMBFhsRC%2BaQX2j%2B0dl%2FF%2FVLTYj3LYlL3qk&pd_rd_r=0a3620f7-00fd-4f1c-b005-3d059df8303d&pd_rd_w=o3Scp&pd_rd_wg=H8F8c&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=T6N3Y9JMWWR276B6G4SC&qid=1682685655&rnid=23974204011&ref=sr_nr_p_n_feature_fifteen_browse-bin_1"
        time_interval = 2
        datas = await Amazon().amazonMe(time_interval, make_headless, userInput)
        return datas
    
    
    start_time = time.time()

    print(asyncio.run(main()))

    total_time = round(time.time()-start_time, 2)
    time_in_secs = round(total_time)
    time_in_mins = round(total_time/60)

    print(f"Took {time_in_secs} seconds | {time_in_mins} minutes.")

