times = '1h 45m,360s,25m,30m 120s,2h 60s'

minutes_in_unit = 0

for time in times.split(","):
    unit = time.split()
    for u in unit:
        if "h" in u:
            hours = int(u.replace("h", ""))
            minutes_in_unit += hours * 60

        elif "m" in u:
            minutes = int(u.replace("m", ""))
            minutes_in_unit += minutes

        else:
            seconds = int(u.replace("s", ""))
            minutes_in_unit += seconds // 60

print(minutes_in_unit)