age = input("what is your curent age?")
age_as_int = int(age)

years_remaining = 90 - age_as_int
daysLeft =  years_remaining * 365
weeksLeft = years_remaining * 52
monthsLeft = years_remaining * 12



print(f"you have {daysLeft} days, {weeksLeft} weeks and {monthsLeft} months lefts")