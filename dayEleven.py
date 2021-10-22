#Justin Farquharson
#10/14/2021
#COP 2500C



def calcAverage(gradeList):

    total = 0
    for index in range(len(gradeList)):
        total = total + gradeList[index]
    return total / len (gradeList)

def weightedGrade(gradeList):
    total = 0
    courses = 0

    for index in range(len(gradeList)):
        if (index %2 == 1):
            total = total + gradeList[index] * 2
            courses = courses + 2
        else:
            total = total + gradeList[index]
        courses + courses + 1

    return total/courses

def roundUp(gradeList, grade):

    assignmentGrades = []

    grade = 0

    while(grade != -1):
        grade = int(input("What grade did you get? (type -1 to exit)"))

    if(grade >= 0):
        assignmentGrades.append(grade) #adds the grade to the end of the list

    print(assignmentGrades)
    print(calcAverage(assignmentGrades))

    lowest = min(assignmentGrades)

    assignmentGrades.remove(lowest)
    print("Dropped Lowest", calcAverage(assignmentGrades))
    print("Max Drop"), max(assignmentGrades)
    print("Lowest Grade", lowest)

    for index in range(len(assignmentGrades)):
        assignmentGrades[index] =assignmentGrades[index] + 4
