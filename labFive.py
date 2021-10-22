#Justin Farquharson
#10/04/2021
#COP 2500C
#Lab

import random
#a = input("Range for outer loop: ")
games = 0
group = 0
while games < 20:
    group += 1
    print("Visiting Group #", group)
    b = random.randint(1,2)
    while b==1:
        print("Play game!")
        games += 1
        b = random.randint(1,2)





pages = 0
days = int(input("How many days of school did you attend?\n"))
while days != 0:
    days = days - 1
    pages = pages + 3
    print("Total:",pages, "has been used")


# or

pages = 0
days = int(input("How many days of school did you attend?\n"))
for i in range(days):
    pages = pages + 3
    print("Total:",pages, "has been used")
