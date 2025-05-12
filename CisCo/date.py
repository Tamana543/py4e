from datetime import date
from datetime import datetime
from datetime import time as t
from datetime import timedelta
import time
import calendar

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
    dataTime = datetime(2004,3,21)
    print(time.gmtime(timestamp))
    print(time.localtime(timestamp))
    print(time.asctime(st))
    print(time.mktime((2004, 11, 4, 14, 53, 0, 0, 308, 0))) # the number of seconds since the Unix epoch
    print("today:", datetime.today())
    print("now:", datetime.now())
    print("utcnow:", datetime.utcnow())
    print("Timestamp: ",dataTime.timestamp()) # to change a given date to a timestamp

# structTime()
def third():
     d = date(2020, 1, 4)
     print(d.strftime('%Y;%m;%d')) # to reFormat date
     # strptime function in datetime and time 
     print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")) 
     print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
     # time as number 
     d1 = date(2025, 11, 4)
     d2 = date(2004, 11, 4)
     print(d1 - d2) # timedelta
     dt1 = datetime(2020, 11, 4, 0, 0, 0)
     dt2 = datetime(2019, 11, 4, 14, 53, 0)
     print(dt1 - dt2)
# third()
def timeDelta():
     delta = timedelta(weeks=3, days=4, hours=3)
     print("Days:", delta.days)
     print("Seconds:", delta.seconds)
     print("Microseconds:", delta.microseconds)
     delta2 = delta * 2
     print(delta2)
     d = date(2019, 10, 4) + delta2
     print(d)
     dt = datetime(2019, 10, 4, 14, 53) + delta2
     print(dt)
     my_date = datetime(2020, 11, 4, 14, 53)
     print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
     print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
     print(my_date.strftime("%a, %Y %b %d"))
     print(my_date.strftime("%A, %Y %B %d"))
     print(my_date.strftime("Weekday: %w"))
     print(my_date.strftime("Day of the year: %j"))
     print(my_date.strftime("Week number of the year: %W"))
# timeDelta()

# Calender Realated Functions 
def first_calendar() :
     print(calendar.calendar(2025,3))
     print("_________________________")
     print(calendar.calendar(2025))
     calendar.setfirstweekday(calendar.SATURDAY)
     calendar.prmonth(2025,11)
     print(calendar.weekday(2025,5,12)) # it print 0 because in calnder madule the first day of the week (Monday) is 0
     print(calendar.weekheader(5))
     print(calendar.isleap(2020))
     print(calendar.leapdays(2020, 2021))  # Up to but not including 2021.
     c = calendar.Calendar(calendar.SUNDAY)
     for weekday in c.iterweekdays():
      print(weekday, end=", ")
# first_calendar()
def delinder(data): 
    c = calendar.Calendar()
    for data in c.monthdays2calendar(2020, 12):
          print(data)
    

# Labe Test 
class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        current_month = 1
        number_of_days = 0
        while (current_month <= 12):
            for data in self.monthdays2calendar(year, current_month):
                if data[weekday][0] != 0:
                    number_of_days = number_of_days + 1

            current_month = current_month + 1
        return number_of_days

my_calendar = MyCalendar()
number_of_days = my_calendar.count_weekday_in_year(2019, calendar.MONDAY)

print(number_of_days)

