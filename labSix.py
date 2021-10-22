#Justin Farquharson
#10/11/2021
#COP 2500C
#Lab

a = 2
b = 4
c = 2

def function(p1, p2, p3):
    res = -p2+(p2**2-4*p1*p3)**0.5/2*p1
    return res
def function2():
    res = b + function()
    return res

def function1(*args):
    total = 0
    for i in  args:
        total += i
    return total
    
    print("--------------")
student1 = function1(10, 5, 4, 8, 20)
student2 = function1(10, 20)
student3 = function1(10, 15)
print("Student1:", student1)
print("Student2:", student2)
print("Student3:", student3)
#Recursive function
def addition(num):
    if num > 0:
        return num + addition(num -1)
    else:
        return 0
res = addition(100)
print(res)

gloabl_var = 0
def addition_job(param1, param2):
    sqr = param1**2
    def add(param3, param4):
        return param3 + param4
    result = add(sqr, param2)
    global_var = result
    print(global_var)
    return result+5

result = addition_job(4,10)
print(result)


def salary_count(name, deduction, b_salary = 5000, bonus = 200):
    salary = b_salary + bonus - deduction
    print(name, ", salary:", salary)

salary_count("Jose", 30)
salary_count("Henry", 0, 4500, 300)
salary_count("Ann", 10, 6000, 500)


def calculations(p1, p2):
    return p1+p2, p1-p2

result1 = calculations(5, 2)
print(result1)
print(calculations(8, 3))

add, sub = calculations(200, 150)
print(add, sub)




def printName(param1, param2):
    print(param1, param2)


printName("Justin", 30)
printName('Elly', 20)
