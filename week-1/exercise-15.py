# Exercise 15: Numbers greater than 30

numbers = [12, 45, 3, 98, 7, 34, 21]
count = 0

print("All numbers:")
for n in numbers:
    print(n)

print("\nNumbers greater than 30:")
for n in numbers:
    if n > 30:
        print(n)
        count += 1

print("\nCount of numbers greater than 30:", count)
