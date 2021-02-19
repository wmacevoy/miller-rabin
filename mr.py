from random import SystemRandom, randint


# https://crypto.stanford.edu/pbc/notes/numbertheory/millerrabin.html

# secure random number generator
rng = SystemRandom()

# number of attempts to test for primality
k = 20

def is_prime(n):
    if n <= 1:
        return False # integers <= 1 are not prime
    if n == 2 or n == 3:
        return True # 2 and 3 are primes
    if n % 2 == 0:
        return False # Even numbers >2 are not prime
    
    # Find l and m such that n-1 = 2^l * m :
    l = 0
    m = n-1
    while m % 2 == 0: # i.e. while m is even
        l = l+1
        m = m//2
       
    # Run (up to) k steps of Miller-Rabin:    
    for i in range(0,k):
        a = rng.randint(2,n-2) # Pick a random integer a in [2,n-2]
        b = pow(a,m,n) # First term of the sequence a^m, a^2m, a^4m, ...
        if b != 1 and b != n-1: #  Check the first term
            j = 0
            while b != n-1 and j < l: # Check the remaining l terms
                b = pow(b,2,n) # Compute the next term by squaring it predecessor
                j = j+1
            if j == l: # We reached the last term
                return False # i.e. n is composite
    return True # i.e. n is probably prime
