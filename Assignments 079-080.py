#Assignment 1 

import datetime

date = datetime.datetime(2021,6,25).date()
today = datetime.datetime.now().date()
result = today - date
print(f"Days From {date} to {today} is => {result.days}")

#Assignment 2 

print (datetime.datetime.now().date())
print (datetime.datetime.now().date().strftime("%b"),datetime.datetime.now().date().day,",",datetime.datetime.now().date().year)
print (datetime.datetime.now().date().day ,"-",datetime.datetime.now().date().strftime("%b"),"-",datetime.datetime.now().date().year)
print (datetime.datetime.now().date().day ,"/",datetime.datetime.now().date().strftime("%b"),"/",datetime.datetime.now().strftime("%y"))
print (datetime.datetime.now().date().day ,"/",datetime.datetime.now().date().strftime("%B"),"/",datetime.datetime.now().year)
print (datetime.datetime.now().strftime("%a") , datetime.datetime.now().date().day , datetime.datetime.now().strftime("%B"),datetime.datetime.now().year)




