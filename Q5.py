import datetime

input_second = int(input("Pleas enter second: "))
time = str(datetime.timedelta(seconds = input_second))

print("Time =", time)