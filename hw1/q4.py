import datetime
import calendar

variable = input("Enter a date in the format MM/DD/YYYY: ")
date_arr = variable.split("/")
month = int(date_arr[0])
day = int(date_arr[1])
year = int(date_arr[2])

date = datetime.date(year, month, day)
day_name = calendar.day_name[date.weekday()]
month_name = calendar.month_name[month] 

print(day_name + ", " + month_name + " " + str(day) + ", " + str(year))