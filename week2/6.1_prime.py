#---------------------------------------------------------------------------#
#  A program, which takes a command line argument and prints all the prime  #
#   numbers between from 1 up to the entered number                         #
#---------------------------------------------------------------------------#

import sys

def sieve(limit):
    if limit <2:
        return []
    
    is_prime = [True]* (limit+1)
    is_prime[0] = is_prime[1] = False #0 and 1 are not prime numbers

    for num in range(2, int(limit ** 0.5)+1):
        if is_prime[num]:
            for multiple in range(num*num, limit+1, num):
                is_prime[multiple] = False

    # Extract prime numbers:
    primes = (i for i, prime in enumerate(is_prime) if prime)
    return primes

if len(sys.argv) != 2:
    print("Correct usage is:\npython3 prime.py <number>")
    sys.exit(1)

try:
    limit = int(sys.argv[1])
except ValueError:
    print("Please enter a valid integer!")
    sys.exit(1)

primes = sieve(limit)
print("Pime numbers up to ", limit," are:\n")
print(list(primes))
