import time
import datetime


oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime(r'%Y/%m/%d %H:%M:%S'))

print(oct21st.strftime(r'%I:%M:%p'))

print(oct21st.strftime(r'%yth of %B'))