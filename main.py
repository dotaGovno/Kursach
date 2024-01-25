from datetime import datetime:

current_date = datetime.now()

target_date = datetime(current_date.year, 9, 1)

if current_date > target_date:
    target_date = datetime(current_date.year + 1, 9, 1)

time_until_target = target_date - current_date

print(f"До 1 сентября осталось: {time_until_target}")
