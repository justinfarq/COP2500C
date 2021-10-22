run = int(input("How many days would you like to track?\n"))
x = 0

while(run != 0 and run >= 0):
    run = run - 1
    miles = int(input("How many miles did you run?\n"))
    if(miles < 0):
        print("Please use positive whole numbers")
        run = run + 1
        miles = miles - miles
    
    x = x + miles

print("Total Miles:",x)

