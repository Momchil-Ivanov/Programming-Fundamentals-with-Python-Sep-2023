def grade_checker(grade: float):
    result = str()
    if 2.00 <= grade <= 2.99:
        result = "Fail"
    elif 3.00 <= grade <= 3.49:
        result = "Poor"
    elif 3.50 <= grade <= 4.49:
        result = "Good"
    elif 4.50 <= grade <= 5.49:
        result = "Very Good"
    elif 5.50 <= grade <= 6.00:
        result = "Excellent"

    return result

tested_grade = float(input())

print(grade_checker(tested_grade))