import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(90)

lim = int(input("What\'s the last number? "))
print("I'll print all the prime numbers till " + str(lim))

print("1")
print("2")
for num in range(3,lim):
    for x in range(2,int(num/2)):
        if (num%x):
            print(str(int(num/x))+" "+str(num%x)+"/"+str(x))
        else:
            print("nope!")
            break
    print(str(num)+" checked")