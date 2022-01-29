# check wheter a number is prime or not
# prime_number --- divisible only by 1 and the number itself
# imp: not divisible by any number between 2 --- "num" (it is a prime number)

def prime():
    num=int(input("Enter the number you want to check: "))
    val=True
    if num>1:
        for i in range(2,num):
            if(num % i)==0:
                val=False
                break
    else:
        val=False
    if val==True:
        print("It is a prime number")
    elif val==False:
        print("It is not a prime number")
    prime()
prime()
