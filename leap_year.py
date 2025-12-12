# This is how you work out whether if a particular year is a leap year.
# - on every year that is divisible by 4 with no remainder
# - except every year that is evenly divisible by 100 with no remainder
# - unless the year is also divisible by 400 with no remainder

def is_leap_year(year):
    """ This function takes a year and determines if is a leap year as True or False """
    divisible_by_four = (year % 4 == 0)
    evenly_div_by_hundred = (year % 100 != 0)
    unless_div_by_fourhundred = (year % 400 == 0)
    if divisible_by_four and unless_div_by_fourhundred:
        return True
    elif not evenly_div_by_hundred and not unless_div_by_fourhundred:
        return False
    else:
        return divisible_by_four

print(is_leap_year(2000))
print(is_leap_year(2100))
print(is_leap_year(2400))
print(is_leap_year(1989))

