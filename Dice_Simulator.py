from random import randint
def diceRoll():
    d1 = randint(1,6)
    d2 = randint(1,6)
    return d1 + d2
totals = {}
temp = 1
for j in range(1000):
    dice = diceRoll()
    totals[dice] = totals.get(dice, 0) + 1
print("Total \tSimulated % \tExpected %")
for i in range(2, 13):
    print(i, "\t", totals[i] /10, "\t\t", round(temp/0.36, 2))
    if i <= 6:
        temp += 1
    else:
        temp -= 1
