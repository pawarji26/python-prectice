# Input
year = int(input("Enter a year: "))

# Check if it's a leap year
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Output
print(is_leap_year)
