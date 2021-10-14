import time
import datetime

input_time = input("Please enter time (00:00:00): ")
temp = time.strptime(input_time,'%H:%M:%S')
total_seconds = datetime.timedelta(hours = temp.tm_hour, minutes = temp.tm_min, seconds = temp.tm_sec).total_seconds()

print("Total seconds =", total_seconds)