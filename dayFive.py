#Justin Farquharson
#09/09/2021
#COP 2500C

running = True

while(running == True):
    stop = input("Do you want to stop?\n")
    if(stop == "yes" or stop == "Yes"):
       running = False


x = 4

if(x == 1):
   print(8.5)

elif(x < 20):
    print(4*9.5)

else:
    print(100)


#For Loops

value = int(input("How many speakers did we have?"))

for count in range(1, value+1):
    print("Who was speaker #", count)
    speaker = input()

    print("Great! I am glad ", speaker, "was able to come")

for count in range(1, 10, 2):
    print(count)

total = 0

for count in range(2, 10, 2):
    print(count)
    total = total + count

print(total)

import random
total = 0

for count in range(2):
    dice = random.randit(1,6)
    total = dice+total

    print("Total =", total, "Die roll:", dice)

#range(start, end, step)
for count in range(5, 1, -1):
    print(count)
