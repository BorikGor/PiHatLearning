#---------------------------------------------------------------------------#
#Write a python program that prints all the even numbers between 0 and 1000.#
#---------------------------------------------------------------------------#
MAX_NUM = 1000
print("Even numbers:"+ "\n".join(str(i)for i in range(0,MAX_NUM+1,2))  +"\n")
