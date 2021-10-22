#Justin Farquharson
#09/20/2021
#COP 2500C
#Lab Three

for row in range(6):
    for column in range(row):
        print("*", end="")
    print('')
print('------')
for row in range(1,6):
    for column in range(5-row, -1, -1):
        print("*", end="")
    print('')

for row in range(1,6):
    for column in range(1,6):
        print(column*row, end="\t")
    print('')
