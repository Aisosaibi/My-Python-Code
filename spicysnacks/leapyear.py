year = int(input("Enter year: "))

divisibleby4 = year % 4 == 0
notby100 = year % 100 != 0
unlessby400 = year % 400 == 0

isleapyear = (
    f"{year} is a leap year" 
    if (divisibleby4 and notby100) or unlessby400 
    else f"{year} is not a leap year")

print(isleapyear)
