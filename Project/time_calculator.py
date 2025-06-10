def add_time(start, duration, weekdays=None):
    start_time, meridiem = start.split()
    start_hr, start_min = map(int, start_time.split(':'))
    duration_hr, duration_min = map(int, duration.split(':'))

    if meridiem == 'PM' and start_hr != 12:
        start_hr_24 = start_hr + 12
    elif meridiem == 'AM' and start_hr == 12:
        start_hr_24 = 0
    else:
        start_hr_24 = start_hr

    final_min = start_min + duration_min
    extra_hr = final_min // 60
    final_min %= 60

    total_hours_24 = start_hr_24 + duration_hr + extra_hr
    days_later = total_hours_24 // 24

    final_hr_24 = total_hours_24 % 24

    if final_hr_24 >= 12:
        meridiem = 'PM'
    else:
        meridiem = 'AM'

    final_hr = final_hr_24 % 12
    if final_hr == 0:
        final_hr = 12

    if final_min < 10:
        min_str = '0' + str(final_min)
    else:
        min_str = str(final_min)

    if weekdays:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(weekdays.capitalize())
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time = f'{final_hr}:{min_str} {meridiem}, {new_day}'
    else:
        new_time = f'{final_hr}:{min_str} {meridiem}'

    if days_later == 1:
        new_time += ' (next day)'
    elif days_later > 1:
        new_time += f' ({days_later} days later)'

    return new_time

# Example usage
print(add_time('8:16 PM', '466:02', 'Sunday'))

