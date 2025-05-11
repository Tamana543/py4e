from datetime import date
from datetime import time as t
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
# firstPrac()

def second() :
     # to change the date exactly from date object : ( you can not do it directly as the date output is read-only)
     d = date(2004,3,21)
     d = d.replace(year=2005, month=4 , day=29)
     print(d)
     print(d.weekday())
     print(d.isoweekday())
# second()

def timeObject() :
     #time(hour, minute, second, microsecond, tzinfo, fold)
     d = t(2,23,13,222)
     print("Time:", d)
     print("Hour:", d.hour)
     print("Minute:", d.minute)
     print("Second:", d.second)
     print("Microsecond:", d.microsecond)
timeObject()