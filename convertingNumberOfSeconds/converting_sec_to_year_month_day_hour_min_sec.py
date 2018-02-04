# This program converts a number of seconds to number of years, months, days, hours, minutes and seconds

number_in_sec = int(input("Enter the number of second\n"))
years = number_in_sec // 31536000
modulo = number_in_sec % 31536000 
months = modulo // 2592000
modulo = modulo % 2592000 
days = modulo // 86400
modulo = modulo % 86400 
hours = modulo // 3600
modulo = modulo % 3600 
minutes = modulo // 60
modulo = modulo % 60 
seconds = modulo
print("{} represent {} year(s), {} month(s), {} day(s), {} minute(s), {} second(s).".format(number_in_sec,years,months,days,minutes,seconds))

