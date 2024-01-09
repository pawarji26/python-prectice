# Input
number = int(input("Enter a number: "))

# Calculate sum of digits
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

# Output
print(sum_of_digits)
