# Exercise 17: Find biggest and smallest number (without max/min)

numbers = [23, 67, 12, 89, 4, 56, 90, 31]

largest = numbers[0]
smallest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Numbers:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
