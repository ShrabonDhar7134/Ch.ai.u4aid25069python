# Exercise 09: Exam Result Checker (Improved Version)

print("EXAM RESULT CHECKER")
print("Please enter your exam scores (0 to 100).\n")

score1 = int(input("Enter score for Subject 1: "))
score2 = int(input("Enter score for Subject 2: "))

print("\n--- RESULT SUMMARY ---")

# Individual subject status
if score1 >= 50:
    print("Subject 1: Pass")
else:
    print("Subject 1: Fail")

if score2 >= 50:
    print("Subject 2: Pass")
else:
    print("Subject 2: Fail")

# Final decision
if score1 >= 50 and score2 >= 50:
    print("\nFinal Result: You PASSED the exams!")
else:
    print("\nFinal Result: You need to RETAKE some exams.")

# Extra feedback
average = (score1 + score2) / 2
print("Average score:", average)

if average >= 75:
    print("Performance: Excellent")
elif average >= 60:
    print("Performance: Good")
else:
    print("Performance: Needs improvement")
