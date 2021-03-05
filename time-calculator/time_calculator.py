def add_time(start, duration, day=None):
    start = start.split()
    duration = list(map(int, duration.split(":")))
    hour = list(map(int, start[0].split(":")))
    meridiem = start[1]

    if meridiem == "PM":
        hour[0] = hour[0] + 12

    new_hour = hour[0] + duration[0]
    new_minutes = hour[1] + duration[1]

    if new_minutes >= 60:
        hours_add = new_minutes // 60
        new_minutes -= hours_add * 60
        new_hour += hours_add

    days_to_add = 0

    if new_hour > 24 :
        days_to_add = new_hour // 24
        new_hour -= days_to_add * 24

    if new_hour > 0 and new_hour < 12 :
        meridiem = "AM"
    elif new_hour == 12 :
        meridiem = "PM"
    elif new_hour > 12 :
        meridiem = "PM"
        new_hour -= 12
    else:
        meridiem = "AM"
        new_hour += 12

    if days_to_add > 0 :
        if days_to_add == 1 :
            days_later = " (next day)"
        else :
            days_later = f" ({str(days_to_add)} days later)"
    else:
        days_later = ""

    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    if day:
        weeks = days_to_add // 7
        i = weekdays.index(day.lower().capitalize()) + (days_to_add - 7 * weeks)
        if i > 6 :
            i -= 7
        day = ", " + weekdays[i]
    else:
        day = ""
    
    new_time= str(new_hour) + ":" + \
        (str(new_minutes) if new_minutes > 9 else ("0" + str(new_minutes))) + \
        " " + meridiem + day + days_later

    return new_time

    

    
    




    






# add_time("3:00 PM", "3:10")

print(add_time("6:30 PM", "205:12"))

