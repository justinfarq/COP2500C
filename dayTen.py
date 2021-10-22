#Justin Farquharson
#10/07/2021
#COP 2500C

import math

#Square Root
print(math.sqrt(16))
print(16 ** 0.5)


publixShopping = ["subs", "cookies", "oreos", "milk", "popcorn", "salsa", "chips"]

print(publixShopping)

#Checks to see if it is in the list
if("watermelon" in publixShopping):
    #Removes from the list
    publixShopping.remove("watermelon")
else:
    print("its not")

while("subs" in publixShopping):
    publixShopping.remove("subs")

print(publixShopping)

#Removes at index value
publixShopping.pop(3)

print(publixShopping)

#Adds to the end of the list
publixShopping.append("Soda")

publixShopping.insert(0, "Bread")

print(publixShopping)

choice = random.randint(0, len(publixShopping))

print(publixShopping[choice] - 1)
