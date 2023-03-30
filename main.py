import os
import sys
import time

sys.path.append(os.getcwd())
from scrapers.scraper import Amazon

  
start_time = time.time()

# Make False if you want to see the live automation.
make_headless = True

print(Amazon().amazonMe(make_headless))

total_time = round(time.time()-start_time, 2)
time_in_secs = round(total_time)
time_in_mins = round(total_time/60)

print(f"Took {time_in_secs} seconds | {time_in_mins} minutes.")