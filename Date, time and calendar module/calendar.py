import calendar

try:
    year = int(input("Enter the current year : "))
    print(calendar.calendar(year))
except:
    print("Exceptional Error")

