from datetime import date
import time

def firstPrac() : 
     today = date.today()
     my_date = date(2004,3,21)
     timestamp = time.time()
     dTimestamp = date.fromtimestamp(timestamp)
     print("Today:", today)
     print("Year:", today.year)
     print("Month:", today.month)
     print("Day:", today.day)
     print(my_date)
     print(timestamp)
     print(dTimestamp)


firstPrac()