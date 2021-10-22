#Justin Farquharson
#10/11/2021
#COP 2500C
#Quad


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

def function():
    part = b**2 - 4*a*c
    return part
def root1():
    part1 = (-b + function()**0.5)/(2*a)
    return part1
def root2():
    part2 = (-b - function()**0.5)/(2*a)
    return part2
    
if(function() == 0):
    print("That quadratic has one root:", root1())
elif(function() > 0):
    print("That quadratic has two roots:", root1(), "and", root2())
else:
    print("Sorry, that quadratic has complex roots.")
