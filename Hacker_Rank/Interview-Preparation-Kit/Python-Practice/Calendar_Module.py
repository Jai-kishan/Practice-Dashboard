import calendar

# week_name =(list(calendar.day_name))
# user=input("Enter the date in this format--> 'MM DD YYYY' : ").split()
# month=int(user[0])
# day=int(user[1])
# year=int(user[2])
# a=(calendar.TextCalendar(firstweekday=6).formatyear(year))
# print(a)

# week_j=calendar.weekday(year,month,day)
# print(week_name[week_j])


week_name =(list(calendar.day_name))
user=input("Enter the date in this format--> 'MM DD YYYY' : ")
month,day,year=[int(i) for i in user.split(" ")]
# print(day,month,year)
# day=int(user[1])
# year=int(user[2])
cal=(calendar.TextCalendar(firstweekday=6).formatyear(year))
print(cal)

week_day=calendar.weekday(year,month,day)
print(week_name[week_day].upper())
