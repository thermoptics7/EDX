#Complete the code below. We've gone ahead and created
#variables for the current date and current time. Now,
#we want to print date with the format year/month/day,
#and the time with the format hour:minute:second.

from datetime import date
import datetime
todaysDate = date.today()
currentTime = datetime.datetime.now()

#Don't modify the code above!

#Complete the line below to print today's date with the
#form year/month/date. For example, January 15th, 2017
#would be 2016/1/15.
todaysDateAsStringYear = str(todaysDate.year)
todaysDateAsStringMonth = str(todaysDate.month)
todaysDateAsStringDay = str(todaysDate.day)
print(todaysDateAsStringYear + "/" + todaysDateAsStringMonth + "/" + todaysDateAsStringDay)
print()

#Complete the line below to print the current time with
#the form hour:minute:second, such as 12:57:15. Don't worry
#about the leading 0s for single-digit times. If it's
#1:05PM and 7 seconds, the correct answer would be:
#13:5:7 (13 because Python uses 24-hour timeby default).
currentTimeAsStringHour = str(currentTime.hour)
currentTimeAsStringMinute = str(currentTime.minute)
currentTimeAsStringSecond = str(currentTime.second)

print(currentTimeAsStringHour + ":" + currentTimeAsStringMinute + ":" + currentTimeAsStringSecond)
print()