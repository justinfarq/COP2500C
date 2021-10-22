#Justin Farquharson
#09/28/2021
#COP 2500C
#Functions

def buyPubSub(meat, cheese):
    price = 6 + meat*1 + cheese*0.30
    #Base = $6.00
    #Extra meat = $1.00
    #Extra cheese = $0.30
#Can't access variables outside of the funtions, must use return

    return price

def buyCookies(number):
    #single cookies = $0.50
    #dozen cookies = $5.00
    # two dozen cookies = $9.00
    price = 0
    while (number>= 24):
        price =  price+9
        number = number - 24
    while (number >= 12):
        price = price+5
        number = number - 12
    price = price + number * 0.50
    return price
        

subOrder = buyPubSub(1, 0) + buyPubSub(3, 2)

print(subOrder)
print(buyCookies(13))

#Alternative for buyCookies
def buyCookies(number):
    #single cookies = $0.50
    #dozen cookies = $5.00
    # two dozen cookies = $9.00
    price = 0
    twoDozens = number // 24
    number = number%24
    oneDozens = number // 12
    number = number%12

    return twoDozens * 9 + oneDozens * 5 + number * 0.50

timeGiven = 6000000
seconds = timeGiven%60
minutes = timeGiven // 60
hours = minutes // 60
days = hours // 24

print(seconds)
print(minutes)
print(hours)
print(days)

def publix():
    option = 0
    price = 0
    while(option != 3):
        print("1. Buy Publix Subs")
        print("2. Buy Cookies")
        print("3. Checkout")

        option = int(input("Pick a number between 1-3\n"))

        if(option ==1):
            meat = int(input("How much extra meat do you want?\n"))
            cheese = int(input("How much extra cheese do you want?\n"))
            tempPrice = buyPubSub(meat, cheese)
            print("You bought a sub for", tempPrice)
            price = price + tempPrice
        elif (option == 2):
            number = int(input("How many cookies would you like?\n"))
            tempPrice = buyCookies(number)
            print("You bought", number,"cookies for", tempPrice)
            price = price + tempPrice
        elif (option == 3):
            print("You are checking out with $",price)
        else:
            print("Invalid option")
publix()
