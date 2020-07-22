import datetime
import pytz
today= datetime.date.today()
print(today)


birthday=datetime.date(1999,2,4)
print(birthday)


days_since_birth=(today-birthday).days
print(days_since_birth)

time_delta=datetime.timedelta(days=10)
print(today-time_delta)

print(today.day)
print(today.weekday())

print(datetime.time(7,1,15,20))
print(datetime.datetime(5,4,5,3,4,8,6))




hour_delta=datetime.timedelta(hours=10)
print(datetime.datetime.now()+hour_delta)

datetime_today=datetime.datetime.now(tz=pytz.UTC)
datetime_maldives=datetime_today.astimezone(pytz.timezone('Indian/Maldives'))
print(datetime_maldives)

#for tz in pytz.all_timezones:
  #print(tz)

#string formatting

print(datetime_maldives.strftime('%B %d %Y'))
