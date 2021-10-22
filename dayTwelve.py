#Math library
#Strings

import math

#Rounding functions

#Ceil = Rounds Up
a = math.ceil(3.1)
print (a)

#Floor = rounds down
a = math.floor(3.1)
print(a)

#Regular rounding
a = round(3.1)
print(a)

#Math.sin
degrees = math.pi
print(math.sin(degrees/2))

#Square Root
a = math.sqrt(25)
print(a)

#Power, base, exp
a = math.pow(2,3) #2^3=8
#or 2**3
print(a)

#Absolute value
a = abs(-5) #5
print(a)

a = "UCentral Florida"

#These are not the same
if("1"==1):
    print("They are the same")
else:
    print("They are different")

#How can I get the C out of UCF
print(a[1])

#Last letter
print(a[-1])

#Sub String
print(a[1:5])

#
print(a[9:])

name = "Justin Farquharson"
value = name.index(" ")
print(value)
print(name[0:value])
print(name[value+1: ])

name2 = "Smith, Jamie Ann"

value = name2.index(",")

print(name2[ value+2 : ])
print(name2[ 0 : value ])

value = name.index(" ")
print(name[ value+1: ] + ", "+ name[0])

roster =[]
IV = "none"

while IV != "Exit":
    print("Menu")
    print("Say help to get to our help menu")
    print("Say Charge On to go to UCF")
    print("Say exit to exit")

    IV = input()

    if(IV == "help"):
        print("You asked for help")
    elif(IV == "charge on"):
        print("You are at UCF now.")
    elif(IV == "exit"):
        print("You are exiting now")
    else:
        print("I don't understand")
