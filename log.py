import re
from datetime import datetime
from longest_time_overheating import overheat_info
from create_log import get_log


def generuj_raport(path):
    try:
        with open(path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return get_log()

    size = len(lines)
    date_temp_data = []
    faulty_lines = []

    for line in lines:
        line = line.strip()
        match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}) (\d+(\.\d+)?)C$", line)
        if match:
            date = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M")
            temp = float(match.group(2))
            date_temp_data.append((date, temp))
        else:
            faulty_lines.append(line)

    faulty_percentage = len(faulty_lines) / size * 100 if size != 0 else 100.0
    report_duration = (date_temp_data[-1][0] - date_temp_data[0][0]).total_seconds() // 60 if date_temp_data else 0
    report_duration = 0 if report_duration in [0, 1] else report_duration

    temperatures = [temp for _, temp in date_temp_data]
    max_temp = max(temperatures) if temperatures else None
    min_temp = min(temperatures) if temperatures else None
    avg_temp = sum(temperatures) / len(temperatures) if temperatures else None

    longest_overheat, periods_count = overheat_info(date_temp_data)

    high_em_interference = faulty_percentage > 10
    high_temp_risk = longest_overheat > 10

    return get_log(faulty_lines, faulty_percentage, report_duration, min_temp, max_temp, avg_temp,
                   longest_overheat, periods_count, high_em_interference, high_temp_risk)


# source_path = "./example/example1.txt"
# source_path = "./example/example2.txt"
source_path = "./example/example3.txt"
# source_path = "./example/example4.txt"
# source_path = "./example/example5.txt"
# source_path = "./example/example6.txt"

report = generuj_raport(source_path)
print(report)
