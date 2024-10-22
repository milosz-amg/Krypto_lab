import random
import gmpy2

# 1. losowy element zbioru Zn
def random_elem_zn(k):
    r_state = gmpy2.random_state(hash(gmpy2.random_state()))
    r = gmpy2.mpz_rrandomb(r_state, k)
    return r 
# ##############################################

#2. odwrotności w grupie Φ(n)
def xgcd(a: int, b: int):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return (b, x0, y0)


def reverse_elem_in_group(b,n):
    gcd, x, _ = xgcd(b, n)

    if gcd != 1:
        print("odwrotnosc nie istnieje")
        return

    return x%n
# ##############################################

#3. efektywne potęgowanie w zbiorze Zn
def effective_power(b,k,n):
    resoult = 1
    b = b % n
    while k>0:
        if k % 2 == 1:
            resoult = (resoult * b) % n
        k = k//2
        b = (b * b) % n
    return resoult
# ##############################################



#DEBUG
def debug():
    return 0

if __name__ == '__main__':

    #1
    # n=10
    # print(random_elem_zn(n))   

    #2
    # b=5
    # n=4096
    # print(reverse_elem_in_group(b,n))

    #3
    # n=12
    # k=16
    # b=219
    # print(effective_power(b,k,n))

    #4

