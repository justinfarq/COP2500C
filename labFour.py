#Justin Farquharson
#09/27/2021
#COP 2500C
#Lab Four

import math

#Three ways to print: charge
#                     on
print("charge","on", sep="\n")
print("charge", end="\non")
print('')
print("charge\non")

cost = int(input("Enter the cost: "))
cost = cost + cost*0.065
print(math.ceil(cost))

#Print Remainder after 5 is divided by 2
print(5%2)

#Prints 5/2 without remainder
print(5//2)

#With remainder
print(5/2)

strInput = input("Enter number with 3 digits\n")
num = int(strInput)
sum = 0
for i in range(len(strInput)):
    sum +=num%10
    num = num//10
print(sum)


months = int(input("How many months?\n"))
saving = 400
for i in range (months):
    print("Month: ", i+1)
    print("Julia has saved", saving,"dollars.")
    saving = saving + 400
