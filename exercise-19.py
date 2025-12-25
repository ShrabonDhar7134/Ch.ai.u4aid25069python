# Exercise 19: Grade counting

grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]

A = B = C = below_70 = 0

for g in grades:
    if g >= 90:
        A += 1
    elif g >= 80:
        B += 1
    elif g >= 70:
        C += 1
    else:
        below_70 += 1

print("Grade A (>=90):", A)
print("Grade B (80-89):", B)
print("Grade C (70-79):", C)
print("Below 70:", below_70)
