from datetime import datetime
import pytz
# Определение временных зон для Бишкека и Лас-Вегаса
timezone_bishkek = pytz.timezone("Asia/Bishkek")
timezone_vegas = pytz.timezone("America/Los_Angeles")
# Получение текущего времени в каждом городе
current_time_bishkek = datetime.now(timezone_bishkek)
current_time_vegas = datetime.now(timezone_vegas)
# Вывод разницы в часовых поясах
print("Текущее время в Бишкеке:", current_time_bishkek.strftime("%Y-%m-%d %H:%M:%S %Z"))
print("Текущее время в Лас-Вегасе:", current_time_vegas.strftime("%Y-%m-%d %H:%M:%S %Z"))
# Разница во времени между городами
time_difference = current_time_bishkek - current_time_vegas
print("Разница во времени между Бишкеком и Лас-Вегасом:", time_difference)
