'''1.1'''
# import datetime

# def get_week_number(year, month, day):
#   date = datetime.date(year, month, day)
#   return date.isocalendar()[1]
# year = 2015
# month = 6
# day = 16
# week_number = get_week_number(year, month, day)
# print(week_number)

'''1.2'''

# import time

# def get_first_monday(year, week):
#   first_day = time.strptime(f"{year} {week} 0", "%Y %U %w")
#   return time.asctime(time.gmtime(time.mktime(first_day) - 60 * 60 * 24))
# year = 2015
# week = 50
# first_monday = get_first_monday(year, week)
# print(first_monday)

'''1.3'''

# from datetime import date, timedelta

# def all_sundays(year):
#     dt = date(year, 1, 1)
#     dt += timedelta(days = 6 - dt.weekday())  
#     while dt.year == year:
#         yield dt
#         dt += timedelta(days = 7)
# for s in all_sundays(2024):
#     print(s)

'''1.4'''
# import datetime

# def addYears(date, years):
#     try:
#         return date.replace(year = date.year + years)
#     except ValueError:
#         return date.replace(year = date.year + years, day=28)

# print (addYears (datetime.date (2015,1,1), -1))
# print (addYears (datetime.date (2015,1,1), 0))
# print (addYears (datetime.date (2015,1,1), 2))
# print (addYears (datetime.date (2000,2,29), 1))

'''2.1'''
# from datetime import datetime
# import pytz

# dt_now = datetime.now(pytz.timezone('Europe/Greenwich'))
# print(dt_now)

'''2.2'''
# import datetime

# def between(date1, date2):
#     minus = date2 - date1
#     return abs(minus.days)

# date1 = datetime.date(2008, 7, 29)
# date2 = datetime.date(2024, 4, 3)
# print(between(date1, date2))

'''2.3'''
# import datetime

# def replace(daysofdata):
#     days = daysofdata.days
#     hours, remainder = divmod(daysofdata.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)
#     return days, hours, minutes, seconds

# date1 = datetime.date(2024, 4, 3)
# date2 = datetime.date(2008, 7, 29)
# difference = date1 - date2

# days, hours, minutes, seconds = replace(difference)
# print(days)
# print(hours)
# print(minutes)
# print(seconds)

