#####
#
# add the following to your rsa file
# this algorithm computes the gcd by using extended Euclid
#
#####

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

##############
#save the following as rsa-shell.py

from rsalibrary.py import *

def unit_test1(kv, lv, dv, textv):
	(p1, p2) = choose_modulus(kv, lv, dv)
	m = p1 * p2
	e = choose_encryption_key(p1, p2)
	d = compute_decryption_key(e, p1, p2)
	plaintext = textv
	P = string_to_int(plaintext)
	print("P = ", P)
	C = RSA_encrypt(P, e, m)
	print("Plaintext: ", plaintext)
	print("Text Len: ", 8*len(plaintext), "bits")
	print("Modulus len: ",  int(log(m)/log(2)), "bits")
	print("C = ", C)
	D = RSA_decrypt(C, d, m)
	print("D = ", D)
	decoded_text = int_to_string(D)
	print("Decoded Text: ", decoded_text, "\n\n--------------\n")

def unit_test2(kv, lv, dv, textv):
	(p1, p2) = choose_modulus(kv, lv, dv)
	m = p1 * p2
	e = choose_encryption_key(p1, p2)
	d = compute_decryption_key(e, p1, p2)
	plaintext = textv
	P = string_to_int(plaintext)
	print("P = ", P)
	C = RSA_encrypt(P, e, m)
	print("Plaintext: ", plaintext)
	print("Text Len: ", 8*len(plaintext), "bits")
	print("Modulus len: ",  int(log(m)/log(2)), "bits")
	print("C = ", C)
	D = RSA_crack(C, e, m)
	print("D = ", D)
	decoded_text = int_to_string(D)
	print("Decoded Text: ", decoded_text, "\n\n--------------\n")

if __name__ == "__main__":
	unit_test1(10, 12, 1, "Hi")
	unit_test1(200,201,50,"I've got the best RSA. Tremendous!")
	unit_test2(10, 12, 5, "Hi")