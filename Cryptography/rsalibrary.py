import sympy
from sympy import *
from sympy.ntheory import isprime
import random
def choose_modulus(k,l,m):
    p1 = find_prime(2**k,2**l)
    p2 = find_prime(2**k,2**l)
    while not(log(p1,2) + m < log(p2,2)):
        p1 = find_prime(2**k,2**l)
        p2 = find_prime(2**k,2**l)
    print(p1*p2)
    return p1*p2
def choose_encryption_key(m):
    e = random.randrange(1,m);
    while not(gcd(e,totient(m)) == 1):
        e = random.randrange(1,m);
    return e
def computer_decryption_key(e,p1,p2):
    return None

def rsa_encrypt(P,e,m):
    return None

def rsa_decrypt(C,d,m):
    return None

def rsa_crack(C,e,m):
    return None

def power_mod(a,b,m):
    x = a**b
    return x % m
def string_to_int(s):
    #returns an integer from the ASCII encoding of s
    return int.from_bytes(s.encode(),'big')
def int_to_string(n):
    #returns a string from the integer n
    return n.to_bytes((n.bit_length()+7)//8,'big').decode()
def find_prime(k,l):
    num = random.randrange(k,l)  #generate a random integer in the range
    # if it's even
    if(num % 2 == 0):
        num = num + 1;
    while not(isprime(num)):
        num = num + 2
        if(num > l):
            temp = num % k
            num = k + temp
    if(num >= k and num <= l):
        #print(num)
        return num

find_prime(37,40)
print()
choose_modulus(20,40,3)
print()
print(choose_encryption_key(choose_modulus(20,40,3)))
print()