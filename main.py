import os
import sys
import time
import asyncio

from functionalities.tools import verify_amazon

sys.path.append(os.getcwd())
from scrapers.scraper import Amazon


# Make False if you want to see the live automation.
make_headless = True


async def main():
    userInput = "https://www.amazon.com/s?k=gaming+headsets&pd_rd_r=9a4b1cba-7756-4d6e-896c-7425f9f02b0a&pd_rd_w=Vcxlr&pd_rd_wg=eHBrI&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=8P8E912Y1YGGR8JTXHDH&ref=pd_gw_unk"
    time_interval = 4
    datas = await Amazon().amazonMe(time_interval, make_headless, userInput)
    return datas


if __name__ == '__main__':
    start_time = time.time()

    asyncio.run(main())

    total_time = round(time.time()-start_time, 2)
    time_in_secs = round(total_time)
    time_in_mins = round(total_time/60)

    print(f"Took {time_in_secs} seconds | {time_in_mins} minutes.")

