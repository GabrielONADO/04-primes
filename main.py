"""fonction de math"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    return if p is a prime number or not (boolean)

    Args:
        p: positive integer

    Returns:
        isprime(p) : p = i*a : false

        or 

        isprime(p) : p : true

    >>>isprime(5)
    5 : true    
    >>>isprime(10)
    10 = 2 * 5 : false


    """
    ispprime = True
    if p == 1:
        print("1 : false")
        return False
    if p == 0:
        print("0 : false")
        return False

    for i in range(2,  round(sqrt(p))+1):
        if p % i == 0 :
            ispprime = False
            print(f"{p} = {i} * {p//i} : false")
            return False
    if ispprime:
        print(f"{p} : true")
        return True
    return ispprime

#### Fonction principale


def main():
    """
    main fonction
    """

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")



if __name__ == "__main__":
    main()
