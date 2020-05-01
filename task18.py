year = int(input('Enter the year, to check leap year it is, or not: '))

def leap(year):

    if year % 4 != 0:
        print(str(year) + " isn\'t a leap year.")
    elif year % 100 == 0:
        if year % 400 == 0:
            print(str(year) + " is a leap year.")
        else:
            print(str(year) + " isn\'t a leap year.")
    else:
        print(str(year) + " is a leap year.")

leap(year)
