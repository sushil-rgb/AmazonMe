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
    userInput = input("Enter a URL:> ")
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

