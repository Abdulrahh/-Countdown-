#upadted version
# reliable  and counts in real time 
#ensure target not missed 
import datetime
import time

target_datetime = datetime.datetime(2026, 2, 4, 12, 28, 0)

while True:
    now = datetime.datetime.now()
    remaining = target_datetime - now 
    
    if remaining.total_seconds() <= 0:
        print("Target reached")
        break
    
    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds =divmod(rem, 60)
    
    print(F"{days}d, {hours}h, {minutes}m, {seconds}s")

    time.sleep(1)
