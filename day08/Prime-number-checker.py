#Write your code below this line 👇


def prime_checker(number):
    isPrime = True
    for n in range(1,number ):
        modulus = number % n
        if n != 1:
            print(n)
            if modulus == 0:
                isPrime = False
                

    if not isPrime:
        print(f'{number} is not Prime')
    else:
        print(f'{number} is Prime') 
             
    




            
    


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)