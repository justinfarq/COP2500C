#Justin Farquharson
#09/21/2021
#COP 2500C


slope = 3
yint = 2

print("y =", slope, "* x +", yint)

for x in range(10):
    y = slope * x + yint
    print("X =", x, "Y =", y)

age = int(input("What is the age of your professors?\n"))

while(age < 23 or age > 90):
    print("Invalid Age")
    age = int(input("What is the age of your professors?\n"))


print("You are in the system")
