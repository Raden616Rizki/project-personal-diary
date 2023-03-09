# first_name = 'Joseph'
# last_name = 'Fars'
# full_name = f'{first_name} {last_name}'
# print(full_name)

from datetime import datetime
today = datetime.now()
# print(type(today))
# print(today)
date_time = today.strftime("%Y-%m-%d-%H-%M-%S")

print(type(date_time))
print(date_time)