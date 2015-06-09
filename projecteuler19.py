#Project Euler 19
#Counting Sundays

#Initialize final variable we are solving for
sunday_count = 0

#Diciontary of # of days in a month
month_days = {
	1: 31,
	2: 28,
	3: 31,
	4: 30,
	5: 31,
	6: 30,
	7: 31,
	8: 31,
	9: 30,
	10: 31,
	11: 30,
	12: 31
}

#List of Days 
#days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#Tracker for current day
current_day = 1

for year in range(1901, 2001, 1):
	for current_month in range(1, 13, 1):
		if year % 4 == 0 and current_month == 2:
			for j in range(1, month_days[current_month]+2, 1):
				if current_day == 6:
					current_day = 0
				else:
					current_day += 1
		else:
			for j in range(1, month_days[current_month]+1, 1):
				if current_day == 6:
					current_day = 0
				else:
					current_day += 1

		if current_day == 6:
			sunday_count += 1

print sunday_count

