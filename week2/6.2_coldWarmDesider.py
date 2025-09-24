#---------------------------------------------------------------------------#
# Write a program that asks the user to input value (from the command line) #
# for temperature and based on the entered value your program should decide #
# whether it is cold or warm now. (Use your own criteria for warmness and   #
# coldness.)                                                                #
#---------------------------------------------------------------------------#

IDEAL_TEMP_L = 18 # As per WorkSafe
IDEAL_TEMP_H = 23 # As per WorkSafe

while True:
    currTemp = input("What's the temperature right now?\n")
    if currTemp.isalpha():
        print(f"{currTemp} is not a number.\nGive me a number, please.")
    else:
        break

if float(currTemp) in range(IDEAL_TEMP_L, IDEAL_TEMP_H):
    print(f"{currTemp}°C seems nice.")
elif float(currTemp) >= IDEAL_TEMP_H:
    print(f"{currTemp}°C is too hot according to WorkSafe!")
elif float(currTemp) < IDEAL_TEMP_L:
    print(f"{currTemp}°C is too cold according to WorkSafe!")
else: print(f"{currTemp} seems like a wrong value.")
