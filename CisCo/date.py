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
# timeObject()

class Break : 
     def take_nap(self,seconds):
          print("Breadk time Start ")
          time.sleep(seconds)
          print("Time Up darling lets go to class")
          # to change a timestamp to real 
          timestamp = time.time()
          print(time.ctime(timestamp))

student = Break()
# student.take_nap(5)
def structTime() :
     #time.struct_time:{tm_year   # Specifies the year. ,tm_mon    # Specifies the month (value from 1 to 12) ,tm_mday   # Specifies the day of the month (value from 1 to 31) ,tm_hour   # Specifies the hour (value from 0 to 23) ,tm_min    # Specifies the minute (value from 0 to 59) ,tm_sec    # Specifies the second (value from 0 to 61 ) ,tm_wday    # Specifies the weekday (value from 0 to 6) ,tm_yday   # Specifies the year day (value from 1 to 366) ,tm_isdst  # Specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known) ,tm_zone   # Specifies the timezone name (value in an abbreviated form) ,tm_gmtoff # Specifies the offset east of UTC (value in seconds)}
    timestamp = time.time()
    st = time.gmtime(timestamp)
    print(time.gmtime(timestamp))
    print(time.localtime(timestamp))
    print(time.asctime(st))
    print(time.mktime((2004, 11, 4, 14, 53, 0, 0, 308, 0))) # the number of seconds since the Unix epoch

structTime()