#Justin Farquharson
#09/12/2021
#COP 2500C
#Movie Going

ticket = int(input("How many people are going?\n"))
gprice = 9.75
sprice = 7.50
group = ticket-1

if(ticket == 1):
    print("Price of Admission is $8.50.")
elif(ticket > 1 and ticket <= 19):
    x1=8.50+group*gprice
    dec1=format(x1,".2f")
    print("Price of Admission for group is: $",dec1)
elif(ticket >= 20 and ticket <=50):
    x2=ticket*sprice
    dec2=format(x2,".2f")
    print("Price of Admission for group is: $",dec2)
else:
    print("Invalid Number of Tickets")
