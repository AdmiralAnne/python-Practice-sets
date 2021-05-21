# same function using Functools module
#lru-----Least Recently Used cache
from functools import lru_cache

# stores Returned Values
@lru_cache(maxsize = 10000)

def fibonacci(n):
    # lets Check for argument input type
    if type(n) != int:
        raise TypeError("please pass a positive integers")
    if n < 0:
        raise TypeError("You entered a non positive integer")
    # compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

for n in range (1,1001):
    print(n, ':', fibonacci(n))
    # ratio between 2 conse cutive numbers converges to a number. Which is also called ~ the golden ratio
    print('ratio :',n, ':', fibonacci(n+1)/fibonacci(n))
