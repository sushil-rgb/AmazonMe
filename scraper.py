import time
from tools import amazonMe

start_time = time.time()

make_headless = True

amazonMe(make_headless)

total_time = round(time.time()-start_time, 2)
time_in_secs = round(total_time)
time_in_mins = round(total_time/60)

print(f"Took {time_in_secs} seconds | {time_in_mins} minutes.")