import time

def day():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    time_hour = int(current_time[0:2])
    time_min = int(current_time[3:5])

    if time_hour <= 12:
        timezz = "Good Morning,"

    elif time_hour >= 12 and time_hour < 16:
        timezz = "Good AfterNoon,"

    else:
        timezz = 'Good Evening,'
    return timezz