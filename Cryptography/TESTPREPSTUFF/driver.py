from sympy import *
# import MatrixCiphers
from MatrixCiphers import *
from Cryptoalpha import *

#AFFINE CIPHERS PRACTICE
#from the test prep packet: to decrypt 'XMRPQ', but given the encryption equation of y = 3x-9 mod 26
alphabet = Cryptoalpha("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#find the inverse equation first
invThree = mod_inverse(3,26)
print(invThree) #spits out 9
#ok, so equation is now 9(x+9) = y
#equation is y = 9x + 81 mod 26
print(81 % 26) #because you're lazy = 3
#equation is y = 9x + 3 mod 26 for decryption
#ok back to the affineCodes file

# print("-"*50)
# print("Testing Hill Codes")
# code1 = Cryptoalpha("ABCDEFGHIJKLMNOPQRSTUVWXYZ!' ")
# plaintext = "Don't Mine at Night!"
# E = Matrix([[4,19],[13,10]])
# ciphertext = encrypt(E, plaintext, code1)
# print("'%s' encodes as '%s'" % (plaintext, ciphertext))
# print("  using encryption matrix")
# pprint(E)
# print("And %s decrypts to %s" % (ciphertext, decrypt(E.inv_mod(code1.m),ciphertext, code1)))

# print("-"*50)
# print("Cracking a code using crib text")
# ciphertext = "!NITFOITTFW!ITFULBAY"
# answer = decrypt(get_decryption_matrix("ESAT", "EIZS", code1),ciphertext, code1)
# print("ciphertext %s is %s" % (ciphertext, answer))
# print("-"*50)
# print("New messages")

# newEncryptMe = "Isabelle is weird!"
# encryptM = get_random_invertible_matrix(len(code1.alphabet))
# encryptedText = encrypt(encryptM, newEncryptMe, code1)
# print("'%s' encodes as '%s'" % (newEncryptMe, encryptedText))
# print(" using encryption matrix")
# pprint(encryptM)
# print("And %s decrypts to %s" % (encryptedText, decrypt(encryptM.inv_mod(code1.m),encryptedText, code1)))
# print("-"*50)