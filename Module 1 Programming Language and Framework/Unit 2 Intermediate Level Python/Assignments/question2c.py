
import math 
'''
Implement a function called filter_prime_numbers that takes a list of
integers as input and uses the filter function to return a new list containing only the
prime numbers.

'''


'''

Filter Blue prints 
filter(func, iteratables )

'''
def isprime(n): 
    """Function that checks whether a numbers is prime or not 

    Args:
        n (int): number

    Returns:
        bool: True if number is prime and False Other wise 
    """
    '''
    if a number n is divisible by any number greater than its square root, it must also be divisible by a number smaller than or equal to its square root.
    
    '''
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
# print(isprime(5303))
def filter_prime_number(nums): 
    """Returns the prime numbers among the list of numbers provided

    Args:
        nums (list): list of numbers

    Returns:
        result(list): list of prime numbers from the nums 
    """

    result = list(filter(isprime, nums))
    return result 
print(filter_prime_number([3,4,5,7,8,9,11]))