import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    s = s.strip()
    if not re.match(r'^\d{1,2}(:\d{2})? [AP]M to \d{1,2}(:\d{2})? [AP]M$', s) and not re.match(r'^\d{1,2}([.:]\d{2})? [AP]M to \d{1,2}([.:]\d{2})? [AP]M$', s):
        raise ValueError

    from_time, to_time = s.split(' to ')
    from_time_parts = re.match(r'^(\d{1,2})(?::(\d{2}))? ([AP]M)$', from_time).groups()
    to_time_parts = re.match(r'^(\d{1,2})(?::(\d{2}))? ([AP]M)$', to_time).groups()

    if not from_time_parts or not to_time_parts:
        raise ValueError

    from_hour = int(from_time_parts[0])
    from_minute = int(from_time_parts[1]) if from_time_parts[1] is not None else 0
    from_period = from_time_parts[2]

    to_hour = int(to_time_parts[0])
    to_minute = int(to_time_parts[1]) if to_time_parts[1] is not None else 0
    to_period = to_time_parts[2]

    if from_hour == 12 and from_period == 'AM':
        from_hour = 0
    if to_hour == 12 and to_period == 'AM':
        to_hour = 0
    if from_period == 'PM' and from_hour != 12:
        from_hour += 12
    if to_period == 'PM' and to_hour != 12:
        to_hour += 12

    if from_hour > 23 or to_hour > 23 or from_minute > 59 or to_minute > 59:
        raise ValueError

    total_minutes = (to_hour * 60 + to_minute) - (from_hour * 60 + from_minute)
    if total_minutes < 0:
        total_minutes += 24 * 60

    hours, minutes = divmod(total_minutes, 60)

    to_minute = (from_minute + minutes) % 60
    to_hour = (from_hour + hours + (from_minute + minutes) // 60) % 24

    return f"{from_hour:02}:{from_minute:02} to {to_hour:02}:{to_minute:02}"


if __name__ == "__main__":
    main()
