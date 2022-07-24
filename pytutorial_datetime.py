import datetime
from datetime import timedelta

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A" ))
print(x)
 
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

delta = timedelta(
     days=50,
     seconds=27,
     microseconds=10,
     milliseconds=29000,
     minutes=5,
     hours=8,
     weeks=2
 )

