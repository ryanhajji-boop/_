import datetime

answered = False

while not answered:
    day = int(input("What day were you born? "))
    month = int(input("What month were you born? "))

    today = datetime.date.today()
    year = today.year

    
    try:
        birthday = datetime.date(year, month, day)
    except ValueError:
        print("Invalid date. Try again.")
        continue

    if birthday < today:
        birthday = datetime.date(year + 1, month, day)

    delta = birthday - today
    print(delta.days, "days until your birthday")

    answered = True

