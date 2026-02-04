# code to check if the current date and time has passed a certain date and time 
# only run if u have a good system
import datetime

target_datetime = datetime.datetime(31000, 2, 4, 12, 14, 0) 

while True:
    current_datetime = datetime.datetime.now()
    if target_datetime >  current_datetime:
        day = target_datetime - current_datetime
        print(day)
       
    
    elif target_datetime < current_datetime:
        print("Past")
        break
    
    else:
        print("same time") #condition not gonna work cus it icludes microseconds  so it never true 

        time.sleep(1)


