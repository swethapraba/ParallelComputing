"""
You have breached security in the TJ syslab and acquired the passwords.txt file for the class of 2018. The format of the file is
userid   encPwd
where encPwd is an encryption of their password. You know that encPwd is always between 8-12 characters, the 
allowed alphabet is 61 characters long, beginning with ASC(33)=0 and ending with ASC(93)=60. You believe the passwords 
have all been encrypted with a 2x2 matrix transformation (e.g. a Hill Cipher) and hope that at least one person in the 
school was lazy enough to use one of the top 1,000 most common passwords (possibly padded with extra random letters).

Using your python libraries and the attached files, crack the code and determine
1) the encryption matrix
2) the userID of the person who used a common password and their password
3) the userID/password of one other person with a recognizable password (not on the top 1000 list)

handy code:
#### open a text file. read it line by line. strip the "\n" off each line. then split the line into three strings w1,w2,w3, separated by whitespace.
in = open("myFile","r")
for line in in.readlines():
      line = line.strip()
      (w1,w2,w3) = line.split()
in.close()
For this (improved?) version of the problem, there is a new password file to decrypt. This time you know that 3 people have 
selected passwords from the common list, and that you only need to worry about passwords on the common list of length > 5.
"""
from sympy import *
from MatrixCiphers import *
from Cryptoalpha import *
###""""new password hacking things"""
infile = open("passwords-v2.txt","r") #file open
for line in infile.readlines():
	###for loop going through the text file line by line
	line = line.strip() #get rid of the "\n"
	print(line) #print the line out
	#(w1,w2) = line.split()
	#print(w1 + "          " + w2)
infile.close() #file close

####The old lab (test to make sure you didn't break everything again)"""
print("-"*50)
print("Testing Hill Codes")
code1 = Cryptoalpha("ABCDEFGHIJKLMNOPQRSTUVWXYZ!' ")
plaintext = "Don't Mine at Night!"
E = Matrix([[4,19],[13,10]])
ciphertext = encrypt(E, plaintext, code1)
print("'%s' encodes as '%s'" % (plaintext, ciphertext))
print("  using encryption matrix")
pprint(E)
print("And %s decrypts to %s" % (ciphertext, decrypt(E.inv_mod(code1.m),
                                                     ciphertext, code1)))

print("-"*50)
print("Cracking a code using crib text")
ciphertext = "!NITFOITTFW!ITFULBAY"
answer = decrypt(get_decryption_matrix("ESAT", "EIZS", code1),
                 ciphertext, code1)
print("ciphertext %s is %s" % (ciphertext, answer))