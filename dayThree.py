#Justin Farquharson
#8/31/2021
#Day 3 - Review, Math, Control Statements

print(3%2)
print(4%2)
print(5%2)
print(6%2)
print(7%2)

number = 12.3456789
print("The value:", "%.2f"%number)

money = int(input("How much money do you have?\n"))

#Interger Division - Always rounds down.

tickets = money//10
# // = Interger Division
print("The number of tickets you can buy are:", tickets)

leftover = money%10
# Modulus(%) = remainder
print("You have", leftover, "dollars left over.")


import random

isStudent = input("Are You A Student?\n")

if(isStudent == "Yes" or isStudent == "yes"):
    print("Free or Discount?")
    chances = random.randint(0,100)
    print(chances)
    if(chances < 70):
        print("You in for Free!")
    else:
        print("You must pay the discounted ticket price.")
else:
    print("You must pay full price")
