bill = int(input('How much was the total bill?\n'))
people = int(input('Between how many people would you like to split the bill?\n'))
tip = int(input('How much of a tip would you like to give? [Popular tips = 10 / 12 / 15%]\n'))

total = round(bill * (1 + tip/100), 2)
share = round(total / people, 2)

print('Each person should pay ${}, resulting in a total of ${}.'.format(share, total))
