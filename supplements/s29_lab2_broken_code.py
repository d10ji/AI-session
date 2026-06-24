# ============================================================
# Lab 2: Debug This Program
# AI for IT Students Workshop — Day 2
# ============================================================
#
# This program has 2 bugs. Your job:
#   1. Run the code and read the error message carefully
#   2. Use AI to help you understand WHY each bug exists
#   3. Fix both bugs
#   4. Add a comment on each fixed line explaining what you changed
#
# Hint: there is one bug per marked line below.
# ============================================================

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    average = total / len(number)   # BUG 1 — look carefully at the variable name
    return average

scores = [85, 92, 78, 96, 88]
result = calculate_average(scores)
print("The average score is: " + result)  # BUG 2 — what type is result?
