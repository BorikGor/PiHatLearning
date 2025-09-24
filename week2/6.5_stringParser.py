#---------------------------------------------------------------------------#
# Given a string that contains numbers (separated by spaces), write a       #
# program that parse these numbers to a list and then sum all the values in #
# the list and print the sum.                                               #
#---------------------------------------------------------------------------#

import random

# Creating a string with random numbers, separated by spaces
ranString = ""
for cnt in range(random.randint(5,10)):
    ranString += str(random.randint(-100,100)) + " "

ranString = ranString.strip()
print(f"String: {ranString}")

ranList = ranString.split()
sumOfList = int(sum(float(number) for number in ranList))
print(f"List: {ranList}")
print(f"Sum: {sumOfList}")