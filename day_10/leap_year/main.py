def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """
    Function to calculate the number of days in a given month of a year\n.
    The function takes in two arguments, year and month, and returns the number of days in the specified month of the year.

    Args:
    year (int): The year for which the month is being checked\n.
    month (int): The month for which the number of days is being calculated.

    Returns:
    int: The number of days in the specified month of the year\n.
    str: Error message if invalid data is provided for year or month.
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 31, 30, 31, 30, 31]

    if month > len(month_days) or month < 1:
        return "You have entered an invalid data for the month. E.g 1-12"
    elif year < 1:
        return "You have entered an invalid data for the year. E.g 1999 or 2021"
    else:
        if is_leap(year) and month == 2:
            return 29
        return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
