#task 1
import datetime

from dateutil.relativedelta import relativedelta


today_info=datetime.date.today()

user_date=input("Enter your date YYYY:MM:DD ")
formated_date=datetime.datetime.strptime(user_date,'%Y:%m:%d')

your_age=relativedelta(today_info,formated_date)

print(f'You are {your_age.years} years {your_age.months} months {your_age.days} days')

#task 2
from datetime import date
birth_year=int(input("Input your birth year "))

birth_month=int(input("Input your birth month "))

birth_day=int(input("Input your birth day "))

birthdate=date.today()

next_year_birth=date(year=birthdate.year,month=birth_month,day=birth_day)

difference=next_year_birth-birthdate

print(f'There are {difference.days} days')

#task 3
import datetime
from datetime import timedelta

current_date_and_time=input("Enter the current date and time YYYY:mm:DD:HH:MM")

meeting=input("Enter the duration meeting HH/MM")
formated_mmeting=datetime.datetime.strptime(meeting,'%H:%M')

t2 = datetime.datetime.strptime(current_date_and_time, '%Y:%m:%d:%H:%M')

t1=timedelta(hours=formated_mmeting.hour,minutes=formated_mmeting.minute)

print(t1+t2)

#task 4
from datetime import datetime
from datetime import timezone
import pytz

current_date_and_time=input("Enter the current date and time YYYY:mm:DD:HH:MM")
formatted_time=datetime.strptime(current_date_and_time,'%Y:%m:%d:%H:%M')

current_timezone=input("Enter the current timezone Continent/Capital ")
second_timezone=input("Enter the another timezone Continent/Capital")

t1=pytz.timezone(current_timezone)
t2=pytz.timezone(second_timezone)

connected_time=t1.localize(formatted_time)

converted_time=connected_time.astimezone(t2)

print(converted_time)

#task 5
import datetime
from datetime import time,timedelta
import time
t1=input("Enter time time HH:MM:SS ")

fr_t=datetime.datetime.strptime(t1,'%H:%M:%S')
fr_t=timedelta(hours=fr_t.hour,minutes=fr_t.minute,seconds=fr_t.second)

seconds=fr_t.total_seconds()

while True:
    print(seconds)
    seconds=seconds-1
    time.sleep(1)
    if seconds==0:
        break

  #task 6
import re
pattern='^[a-zA-z0-9.%+-]+@[a-z]+[\\.](com)$'

email=input("Enter your email ")

if re.match(pattern,email):
    print("matched")
else:
    print("Unmatched")

  #ask 7

t_number=input("Enter the phone number")

num=t_number[0:4]+' '+t_number[4:7]+'-'+t_number[7::]
print(num)

#task 8
import re
password=input("Enter the password ")
pattern1='[a-zA-Z0-9]+'
pattern2='[^a-zA-Z0-9]+'
if len(password)>=12 and re.search(pattern1,password) and re.search(pattern2,password):
    print("accepted")
else:
    print("Please enter another password ")

#task 9
import re
text=input("Enter the text ")

word=input("Enter the word ")

lis=[]

t=text.split(' ')

for x in range(len(t)):
    if word == t[x].lower():
        print(f'{t[x]} word in {x} position')

#task 10
import datefinder
text=input("Enter the text ")

dates=datefinder.find_dates(text)

for date in dates:
    print(date)


