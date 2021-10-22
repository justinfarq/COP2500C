#Justin Farquharson
#09/19/2021
#COP 2500C
#Line Plotter


delay = int(input("Enter the per delay:"))
time = int(input("Enter the time off work:"))
number = int(input("Enter the number of delays in our table:"))

total = 0

while(total < number):
    for d in range(number):
        print("Delay #", total, ", Time =", time)
        total = total + 1
        time = time+delay
