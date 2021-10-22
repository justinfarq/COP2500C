grade = int(input("What grade did you receive on the assignment\n"))
late = int(input("How many hours late did you turn in the assignment\n"))

if(late >= 1 and late <= 12):
    grade = grade*0.90
    print(grade)
elif(late >= 13 and late <= 48):
    grade = grade*0.80
    print(grade)
elif(late == 0):
    print(grade)
else:
    grade = 0
    print(grade)

