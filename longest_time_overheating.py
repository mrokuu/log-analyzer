def overheat_info(date_temp_data):
    periods_count = 0
    longest_overheat = 0
    overheat_start = None

    for date, temp in date_temp_data:
        if temp > 100:
            if overheat_start is None:
                overheat_start = date
        else:
            if overheat_start is not None:
                overheat_time = (date - overheat_start).total_seconds() // 60
                longest_overheat = max(longest_overheat, overheat_time)
                periods_count += 1
                overheat_start = None

    if overheat_start is not None:
        date, _ = date_temp_data[-1]
        overheat_time = (date - overheat_start).total_seconds() // 60
        longest_overheat = max(longest_overheat, overheat_time)
        periods_count += 1

    return longest_overheat, periods_count