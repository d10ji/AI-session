# ============================================================
# Lab 2: Debug This Program — INSTRUCTOR ANSWER KEY
# ============================================================
#
# Bug 1: "number" should be "numbers" — NameError
#        The variable is named "numbers" (the parameter) but we
#        accidentally typed "number" (which does not exist).
#
# Bug 2: result is a float, not a string — TypeError
#        You cannot join a string and a number with +
#        Use str() to convert, or use an f-string.
#
# ============================================================

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    average = total / len(numbers)   # FIXED: "number" → "numbers"
    return average

scores = [85, 92, 78, 96, 88]
result = calculate_average(scores)
print("The average score is: " + str(result))  # FIXED: wrapped result in str()

# Alternative fix for Bug 2 using f-string (also correct):
# print(f"The average score is: {result}")
