def is_leap_year(year):
    if (year %4 ==0 and year%100 !=0) or year%400 == 0:
        return True
    else:
        return False
    
year=int(input())

if is_leap_year(year):
    print(f"{year}is a leap year")

else:
    print(f"{year} is not leap year")