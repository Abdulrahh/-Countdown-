# code to check if the current date and time has passed a certain date and time 
import datetime

target_datetime = datetime.datetime(2026, 2, 4, 11, 52, 0)

while True:
    current_datetime = datetime.datetime.now()
    if target_datetime >  current_datetime:
        day = target_datetime - current_datetime
        print(day)
       
    
    elif target_datetime < current_datetime:
        print("Past")
        break
    
    else:
        print("same time")
        time.sleep()