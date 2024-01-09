# Input
num = int(input("Enter an integer: "))

# Check even, odd, or invalid
if num >= 0:
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("invalid")
