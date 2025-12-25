# Exercise 05: Operations on two numbers (with division)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

# Division (with safety check)
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division by zero is not allowed")

# Bigger number check
if num1 > num2:
    print("First number is bigger")
elif num2 > num1:
    print("Second number is bigger")
else:
    print("Both numbers are equal")
