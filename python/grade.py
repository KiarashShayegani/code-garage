

def grade_calculator(grade: int) -> str:

    if grade>100:
        return 'Wrong grade(0-100 only!)'

    elif 90 <= grade and grade <= 100:
        return 'A'
    elif 80 <= grade and grade < 90:
        return 'B'
    elif 70 <= grade and grade < 80:
        return 'C'
    elif 60 <= grade and grade < 70:
        return 'D'
    else:
        return 'F'

try:
    grade = int(input('Enter your grade: '))
except ValueError:
    print("Only integer numbers are allowed!")

print(f"Result: {grade_calculator(grade)}")



