#---------------------------------------------------------------------------#
# Write a program, which finds maximum and minimum as well as the indexes   #
# on which they are located, in an unsorted list. (You are not allowed to   #
# use built-in sort function).                                              #
#                                                                           #
#---------------------------------------------------------------------------#

import random

for i in range(10) :
    a = [random.randint(-10,10) for cnt in range(random.randint(5,10))]
    print("#---------------------------------------------------------------------------#")
    print(f"Random number {i}: {a}")

    print(f"Max in this list is: {max(a)}.\nThe first one is located at {a.index(max(a))}.")
    print(f"Min in this list is: {min(a)}.\nThe first one is located at {a.index(min(a))}.")
print("#---------------------------------------------------------------------------#")
