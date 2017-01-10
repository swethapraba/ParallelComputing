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
def compute_decryption_key(e,p1,p2):
	#d = e inverse mod phi(m) m = p1*p2
	mathStuff = (p1-1)*(p2-1) #they're prime numbers so magic, no pphi things
	d = mod_inverse(e,mathStuff)
	return d

def rsa_encrypt(P,e,m):
	return power_mod(P, e, m)

def rsa_decrypt(C,d,m): ####
	return power_mod(C,d,m)

def rsa_crack(C,e,m):
	phiModulusValue = totient(m) #magic
	decryptionKey = mod_inverse(e, phiModulusValue)
	return rsa_decrypt(C, decryptionKey, m)

def power_mod(a,b,m):
	#x = (a%m)**(b%m) #mod each before power it also works
	#return x % m
	
	return pow(a,b,m)
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

def mod_inverse(b, n):
	""" Return the modular inverse of b mod n
	 or None if gcd(b,n) > 1 """
	g, x, _ = xgcd(b, n)
	if g == 1:
		return x % n


modulus = (17*19)
encryptionKey = 23
number = 2

#d = e inverse mod phi (15) - 5 * 3, so we can find phi(15), (4*2) = 8
#d = mod_inverse(encryptionKey, totient(modulus))
d = compute_decryption_key(encryptionKey, 17, 19)
string1 = rsa_encrypt(number, encryptionKey, modulus)
print(string1)
string2 = rsa_decrypt(string1, d, modulus)
print(string2)
decryptMe = rsa_crack(string1, encryptionKey, modulus)
print(decryptMe)