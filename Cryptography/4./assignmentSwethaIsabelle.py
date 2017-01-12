import sympy
from sympy import *
import random

def choose_modulus(k,l,m):
	p1 = find_prime(k,l)
	p2 = find_prime(k,l)
	#while not (log(p1,2) + m < log(p2, 2)):
	#	p1 = find_prime(k,l)
	#	p2 = find_prime(k,l)
	#	print(p1, p2)
	#print(log(p1,2)+m < log(p2,2))
	#print("prime 1: ", p1)
	#print("prime 2: ", p2)
	return p1,p2

def choose_encryption_key_old(m):
	e = random.randrange(2,m)
	while not gcd(e, totient(m)) == 1:
		e = random.randrange(2,m)
	return e

def choose_encryption_key(p1,p2):
	m = p1*p2
	e = random.randrange(2, p1*p2)
	while not gcd(e, (p1-1)*(p2-1)) == 1:
		e = random.randrange(2, p1*p2)
	return e

def compute_decryption_key(e, p1, p2):
	# d = e inverse mod phi(m) m = p1*p2
	#phi(m) = (p1-1)*(p2-1)
	d = inv_mod(e, (p1-1)*(p2-1))
	return d

def RSA_encrypt(P, e, m):
	return power_mod(P,e,m)

def RSA_decrypt(C, d, m):
	return power_mod(C,d,m)

def RSA_crack(C, e, m):
	return power_mod(C, inv_mod(e,totient(m)), m)

def power_mod(a, b, m):
	#replace with better version for large numbers
	#return ((a%m)**(b%m))%m
	return pow(a,b,m)

def string_to_int(s):
	return int.from_bytes(s.encode(),'big')

def int_to_string(n):
	return n.to_bytes((n.bit_length()+7)//8,'big').decode()

def find_prime(k, l):
	x = random.randrange(2**k+2, 2**l-1)
	while (not isprime(x)):
		x = random.randrange(2**k+2, 2**l-1)
	return x

def mod_inv_old(a,m):
	#replace with euclid's algorithm - will be using large numbers
	for i in range(0,m):
		if (i*a)%m == 1:
			return i
	return -1

def xgcd(b, n):
    """ Return g, x0, y0
        such that x0*b + y0*n = g
        and g is the gcd of (b,n)"""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0

def inv_mod(b, n):
    """ Return the modular inverse of b mod n
     or None if gcd(b,n) > 1 """
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n

def unit_test1(kv, lv, dv, textv):
	(p1, p2) = choose_modulus(kv, lv, dv)
	m = p1 * p2
	e = choose_encryption_key(p1, p2)
	d = compute_decryption_key(e, p1, p2)
	plaintext = textv
	P = string_to_int(plaintext)
	print("Plaintext in bits = ", P)
	C = RSA_encrypt(P, e, m)
	print("Plaintext: ", plaintext)
	print("Text Len: ", 8*len(plaintext), "bits")
	print("Modulus len: ",  int(log(m)/log(2)), "bits")
	print("Ciphertext in bit format = ", C)
	D = RSA_decrypt(C, d, m)
	print("D (Decrypted text in bit format) = ", D)
	decoded_text = int_to_string(D)
	print("Decoded Text: ", decoded_text, "\n\n--------------\n")

def unit_test2(kv, lv, dv, textv):
	(p1, p2) = choose_modulus(kv, lv, dv)
	m = p1 * p2
	e = choose_encryption_key(p1, p2)
	d = compute_decryption_key(e, p1, p2)
	plaintext = textv
	P = string_to_int(plaintext)
	print("Plaintext in bits = ", P)
	C = RSA_encrypt(P, e, m)
	print("Plaintext: ", plaintext)
	print("Text Len: ", 8*len(plaintext), "bits")
	print("Modulus len: ",  int(log(m)/log(2)), "bits")
	print("C (Ciphertext in bit format) = ", C)
	D = RSA_crack(C, e, m)
	print("D (decrypted text in bit format) = ", D)
	decoded_text = int_to_string(D)
	print("Decoded Text: ", decoded_text, "\n\n--------------\n")

#unit_test1(10, 12, 1, "Hi")
#unit_test1(200, 201, 50, "YouUsedTheWrongFormulaButGotTheRightAnswer")
#unit_test1(200,201,50,"I've got the best RSA. Tremendous!")
#unit_test2(10, 12, 5, "Hi")

#################
"""
PART 1: OUR SCHEMES
"""
#find a modulus
p1,p2 = choose_modulus(198,202,1) #this has p1 and p2
modulus = p1*p2
print("Prime 1: ", p1)
print("Prime 2: ", p2)
#find an encryption key
encryptKey = choose_encryption_key(p1,p2)
print("Modulus: ", modulus)
print("Encryption Key: ", encryptKey) #post key and modulus value to new blackboard thread

print()
print("-------------------------------")
print()
##############
"""
PART 2: SENDING SOMEONE ELSE A MESSAGE WITH THEIR SCHEME
"""
theirEKey = encryptKey # this is where we add their e!!!!!!!!
theirMod = modulus #add their m !!!!!!
ourMessage = "YouUsedTheWrongFormulaButGotTheRightAnswer" #42 chars
byteMessage = string_to_int(ourMessage) #42 bytes long
encryptedText = RSA_encrypt(byteMessage, theirEKey, theirMod)
print("The Encrypted Text: ", encryptedText) #post this on that person's blackboard thread so they can crack it
print()
print("-------------------------------")
print()
#########
"""
PART 3: DECODING THE MESSAGE SENT TO US USING OUR SCHEME
"""
encryption = encryptKey
mod = modulus
byteReceived = encryptedText #7685639402658570041332092386730857722829508721500337074039018855544141530770944219201236076815619964810541252211564571230 #encryptedText 
#this is posted for us ^^
#stringReceived = int_to_string(byteReceived) #decrypt it
decryptKey = compute_decryption_key(encryption, p1, p2)
#print("1 ", decryptKey)
decryptedBytes = RSA_decrypt(byteReceived, decryptKey, mod)
#print("2 ", decryptedBytes)
decryptedString = int_to_string(decryptedBytes)
#print("3 ", decryptedString)
print("The Message received : ", decryptedString) #this was the message we got -> post to our blackboard thread
