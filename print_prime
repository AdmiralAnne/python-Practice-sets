# print all prime numbers in an interval
def print_prime():
    lower=int(input("Enter Lower Limit: "))
    upper=int(input("Enter Upper Limit: "))
    count = 0
    # check for prime number in specified range only
    for i in range(lower,upper+1):
        # since all prime nos are Greater than 1 
        if i > 1:
            # prime numbers cannot be divisible by any number between 2----to---"TestNumber-1"
            for j in range (2,i):
                # if i is completely divisible by sny number between 2 and (i-1), it is not a prime number
                if(i%j)==0:
                    break
            else:
                print(i)
                count +=1
    print(f"There are {count} prime Numbers between {lower} and {upper}")
print_prime()
