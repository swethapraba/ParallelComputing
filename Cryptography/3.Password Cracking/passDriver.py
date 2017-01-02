import enchant #import dictionary library
from sympy import * #our buddy sympy
from MatrixCiphers import * #helper matrix methods
from Cryptoalpha import * #helper cryptoalphabet methods

dictionary = enchant.Dict("en_US") #english library

alphabet = Cryptoalpha("!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]")#61 char alphabet
m = 61 #mod value

passwordsFile = open("passwords-v2.txt","r") #encrypted passwords file open
commonPassFile = open("common-passwords.txt","r") #common passwords file open

encryptionMatrix = Matrix([[0,0],[0,0]]) #this is where the final matrix will be stored once we find it
sillyUser = "" #this is the user who used the commonPassword
sillyEncryptedPassword = "" #this is that user's encrypted password that's in the file
sillyPassword = "" #that person's decrypted password we were able to crack

hackedUser = "" #this is the user we were able to find
hackedEncryptedPassword = "" #that person's encrypted password from the file
hackedPassword = "" #that person's decrypted password


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