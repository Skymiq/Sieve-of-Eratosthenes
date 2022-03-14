"""
Description:

The method of Eratosthenes Sieve.
From the set of natural numbers in the interval [2, n], we choose the smallest,
that is, 2, and we plot all its multiples greater than itself. From the rest of the numbers
we choose the smallest number (3) and remove all its multiples greater than
the same. We follow the same procedure for subsequent numbers.
The process leaves only prime numbers undeleted.

It is a algorithm that looks up prime numbers in given range.
"""

from math import isqrt


# Function that checks a prime numbers in user-defined range
def primes_less_than(n: int) -> list[int]:
    if n <= 2:
        return []
    # Declaration of a Boolean array used to plot non-prime numbers
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    # Plotting non-prime numbers from a boolean table
    for i in range(2, isqrt(n)+1):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False

    # Return the numbers that remain in the boolean array after the for loop has completed
    return [i for i in range(n) if is_prime[i]]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Welcome prompt
    print("\nPrimes Erastosthenes Finder v1.0\n")

    # Lower and upper bound of range from user
    upper = int(input("Please enter the upper limit: "))
    print("\nSearch for prime numbers in range 0 to {}\n".format(upper))

    # Checking the speed of the program
    import time
    start = time.perf_counter()

    result = primes_less_than(upper)
    print("In the range 0 to {} were found {} prime number(s)".format(upper, len(result)))
    print(result)

    # Display of program execution time
    elapsed = time.perf_counter() - start
    print("\nIt took {:.2f}s". format(elapsed))

"""
Result:

Primes Erastosthenes Finder v1.0

Please enter the upper limit: 1000

Search for prime numbers in range 0 to 1000

In the range 0 to 1000 were found 168 prime number(s)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 
 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 
 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 
 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 
 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 
 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 
 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 
 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 
 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 
 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 
 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 
 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 
 953, 967, 971, 977, 983, 991, 997]

It took 0.00s
"""