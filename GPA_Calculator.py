# Unweighted GPA Letter to Number Conversion
def unweighted(gpa):
    if gpa == "A+":
        gpa = 4.33
    elif gpa == "A":
        gpa = 4.00
    elif gpa == "A-":
        gpa = 3.67
    elif gpa == "B+":
        gpa = 3.33
    elif gpa == "B":
        gpa = 3.00
    elif gpa == "B-":
        gpa = 2.67
    elif gpa == "C+":
        gpa = 2.33
    elif gpa == "C":
        gpa = 2.00
    elif gpa == "C-":
        gpa = 1.67
    elif gpa == "D:":
        gpa = 1.00
    elif gpa == "F":
        gpa = 0.00
    return gpa

# Weighted GPA Letter to Number Conversion
def weighted(gpa, course):
    if course == "AP" or course == "Honors" or course == "H":
        if gpa == "A+":
            gpa = 6.33
        elif gpa == "A":
            gpa = 6.00
        elif gpa == "A-":
            gpa = 5.67
        elif gpa == "B+":
            gpa = 5.33
        elif gpa == "B":
            gpa = 5.00
        elif gpa == "B-":
            gpa = 4.67
        elif gpa == "C+":
            gpa = 4.33
        elif gpa == "C":
            gpa = 4.00
        elif gpa == "C-":
            gpa = 3.67
        elif gpa == "D:":
            gpa = 1.00
        elif gpa == "F":
            gpa = 0.00
    elif course == "Accelerated" or course == "A":
        if gpa == "A+":
            gpa = 5.33
        elif gpa == "A":
            gpa = 5.00
        elif gpa == "A-":
            gpa = 4.67
        elif gpa == "B+":
            gpa = 4.33
        elif gpa == "B":
            gpa = 4.00
        elif gpa == "B-":
            gpa = 3.67
        elif gpa == "C+":
            gpa = 3.33
        elif gpa == "C":
            gpa = 3.00
        elif gpa == "C-":
            gpa = 2.67
        elif gpa == "D:":
            gpa = 1.00
        elif gpa == "F":
            gpa = 0.00
    elif course == "Regular" or course == "R" or course == None:
        gpa = unweighted(gpa)
    return gpa

# Variables and Input
english_grade, english_course = input("Input your English letter grade: "), input("Input your English course level: ")
math_grade, math_course = input("Input your Math letter grade: "), input("Input your Math course level: ")
science_grade, science_course = input("Input your Science letter grade: "), input("Input your Science course level: ")
history_grade, history_course = input("Input your History letter grade: "), input("Input your History course level: ")
gym_grade = input("Input your Gym letter grade: ")
health_grade = input("Input your Health letter grade: ")
elective1_grade, elective1_course = input("Input your Elective letter grade: "), input("Input your Elective course level: ")
elective2_grade, elective2_course = input("Input your Elective letter grade: "), input("Input your Elective course level: ")

# Calculations and Output
unweighted_gpa = (5*unweighted(english_grade) + 5*unweighted(math_grade) + 6*unweighted(science_grade) + 5*unweighted(history_grade) + 3.75*unweighted(gym_grade) + 1.25*unweighted(health_grade) + 5*unweighted(elective1_grade) + 5*unweighted(elective2_grade)) / 36
print(f"Your Unweighted GPA is: {unweighted_gpa}")

weighted_gpa = (5*weighted(english_grade, english_course) + 5*weighted(math_grade, math_course) + 6*weighted(science_grade, science_course) + 5*weighted(history_grade, history_course) + 3.75*weighted(gym_grade, None) + 1.25*weighted(health_grade, None) + 5*weighted(elective1_grade, elective1_course) + 5*weighted(elective2_grade, elective2_course)) / 36
print(f"Your Weighted GPA is: {weighted_gpa}")