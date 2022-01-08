year = int(input())
is_leap_year = False
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    is_leap_year = True
print(1 if is_leap_year else 0)