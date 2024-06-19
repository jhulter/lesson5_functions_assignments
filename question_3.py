# Task 1

grades = [66, 76, 89, 45, 99, 100, 96, 76, 78]
grades_sum = sum(grades)

def ave_grade():
    return grades_sum / len(grades)

print(ave_grade())

# Task 2
def get_highest_lowest(grades):
    return max(grades), min(grades)

print(get_highest_lowest(grades))
# Task 3

for grade in grades:
    print(grade)
    if grade <= 60:
        print("F")
    elif grade >= 60 and grade <= 70:
        print("D")
    elif grade >= 70 and grade <= 80:
        print("C")
    elif grade >= 80 and grade <= 90:
        print("B")
    else:
        print("A")
