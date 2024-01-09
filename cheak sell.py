# Input
sales_count = int(input("Enter the total sales count: "))

# Check the group based on sales count
if 30 <= sales_count <= 50:
    group = 'D'
elif 51 <= sales_count <= 60:
    group = 'C'
elif 61 <= sales_count <= 80:
    group = 'B'
elif 81 <= sales_count <= 100:
    group = 'A'
else:
    print("Invalid sales count. Please enter a value between 30 and 100.")
    exit()

# Output
print(group)
