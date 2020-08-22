def leap_year(year):
    return year % 4 == False and year % 100 != False or year % 400 == False
