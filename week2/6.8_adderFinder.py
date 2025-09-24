#---------------------------------------------------------------------------#
# Given a list of numbers and a number, which represents sum, write a       #
# Python program that loop through the list and finds the pair of numbers,  #
# which adds up to sum.                                                     #
#---------------------------------------------------------------------------#

import random

fndFlag = False
sumNumber = random.randint(2,10)
numberList = [random.randint(-10,10) for cnt in range(random.randint(10,20))]

print(f"Searching for the adders of the {sumNumber} in the list:\n{numberList}:")

for i in range(0,len(numberList)):
    for j in range(i,len(numberList)):
        if numberList[i]+numberList[j] == sumNumber:
            fndFlag = True
            print(f"{numberList[i]} + {numberList[j]} = {sumNumber}")
            break

if not fndFlag : print("Not found!")