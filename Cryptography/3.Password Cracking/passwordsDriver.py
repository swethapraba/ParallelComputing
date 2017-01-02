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
import enchant
from sympy import *
from MatrixCiphers import *
from Cryptoalpha import *
#english library
dictionary = enchant.Dict("en_US")
#print(1)

crackAlpha = Cryptoalpha("!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]")#61 char alphabet
m = 61 #mod value

###""""new password hacking things"""
passwordFile = open("passwords-v2.txt","r") #encrypted passwords file open
commonFile = open("common-passwords.txt","r") #common passwords file open
encryptionMatrix = Matrix([[0,0],[0,0]]) #this is where the final matrix will be stored once we find it

sillyUser = "" #this is the user who used the commonPassword
sillyEncryptedPassword = ""
sillyPassword = "" #that person's password we were able to crack
hackedUser = "" #this is the user we were able to find
hackedPassword = "" #that person's password

#for now, a temporary extra tester
number = 0
tempU = ""
tempP = ""

for line in passwordFile.readlines():
	#for loop going through the text file line by line
	line = line.strip() #get rid of the "\n"
	#print(line) #print the line out
	(userid,encpwd) = line.split() #userid = string of username ; encpwd = encrypted password from that person
	#print(userid)
	if number == 0:
		tempU = userid #just grab the first user and password
		tempP = encpwd 
		number = 1
		#print(2)
	print(userid)
	#break
	#print(user + "          " + encpass) #just print stuff out (print the whole nonsplit line to get the nice formatting)
	if len(encpwd) > 5: #if it's longer than 5 characters
	 	cipher = encpwd #take the person's password -> this is the cipher text
 		#print(3)
 		print(cipher)
 		#go through each password in the commonFile
 		#for piece in range(0,10):
 		for piece in commonFile.readlines():
 			print()
 			potentialPlain = piece.strip() #get rid of the "\n"
 			print(potentialPlain)#we have our potential plaintext / the common password being considered
 			fourCharC = encpwd[:4] #these are going to be the first four characters of the encrypted Password
 			print(fourCharC)
 			fourCharP = potentialPlain[:4] #the first 4 characters of the possible common pass
 			print(fourCharP)
 			testMatrix = get_decryption_matrix(fourCharP, fourCharC , crackAlpha) #plain, cipher, alpha
 			#ok so now we have a matrix that makes these values true. we have no clue if it's good or not
 			#print(5) #test line
 			#print(text) #test line
 			#pprint(testMatrix) #test line

 			#we'll need some tests of if this matrix is legit
 			determinant = gcd(det(testMatrix),m)
 			#print(determinant)
 			if(determinant != 61): #if the determinant is 61 bad things happen?
 				if determinant == 1: #if the gcd is 1, we have an invertible matrix
 					#continue with the next test and keep going
 					#if this matrix passes those tests and we deem it legit
 					decrypted = decrypt(testMatrix,encpwd, crackAlpha) #apply the decryption matrix to the entire password
 					#print(decrypted)
 					#CHECK: does the entire decrypted string match the plain text common password being considered?
 					if decrypted == potentialPlain:
 						#yay we have our matching person
 						sillyUser = userid
 						sillyEncryptedPassword = encpwd
 						sillyPassword = decrypted
 						encryptionMatrix = testMatrix

 						#cool now we should decrypt another random person's stuff for fun
 						

	# 			decryptedText = decrypt(testMatrix,tempP,crackAlpha) #here's the decrypted password
	# 			#print(decryptedText)
	# 			#print("haha")
	# 			###########
	# 			#sillyUser = userid 
	# 			#sillyPassword = sillyDecrypted
	# 			#hackedUser = tempU #yay we're just about done
	# 			#hackedPassword = decryptedText
	# 			#encryptionMatrix = testMatrix
	# 			#print("boo")
	# 			checking = dictionary.check(decryptedText) #is this password a real English word
	# 			#print("Ladeedaa")
	# 			if checking is True:#true: #if our test password is real
	# 				sillyUser = userid 
	# 				sillyPassword = sillyDecrypted
	# 				hackedUser = tempU #yay we're just about done
	# 				hackedPassword = decryptedText
	# 				encryptionMatrix = testMatrix
	# 				print("this test works")
	# 				break
	# 		#else:
	# 			#do nothing, just go to the next password in the commonPass file
	# 			#print()
	# #else:
	# 	#do nothing, go to next user in the file
	# 	#print()
	# print()

passwordFile.close() #file close
commonFile.close()
#print: encryption matrix
pprint(encryptionMatrix)

####TEST SECTION DELETE SOON####
hackedUser = tempU #yay we're just about done
hackedPassword = tempP#decryptedText
#print user who has a common password, and the password
print("The Silly Junior: " + sillyUser)
print("Their crackable password: " + sillyPassword)
print()
#print the userID/password of one other person with a recognizable password (not on the top 1000 list)
print("Other hacked person: " + hackedUser)
print("Their password: " + hackedPassword)
print()
#print(1342)

####The old lab (test to make sure you didn't break everything again)"""
# print("-"*50)
# print("Testing Hill Codes")
# code1 = Cryptoalpha("ABCDEFGHIJKLMNOPQRSTUVWXYZ!' ")
# plaintext = "Don't Mine at Night!"
# E = Matrix([[4,19],[13,10]])
# ciphertext = encrypt(E, plaintext, code1)
# print("'%s' encodes as '%s'" % (plaintext, ciphertext))
# print("  using encryption matrix")
# pprint(E)
# print("And %s decrypts to %s" % (ciphertext, decrypt(E.inv_mod(code1.m),
#                                                      ciphertext, code1)))

# print("-"*50)
# print("Cracking a code using crib text")
# ciphertext = "!NITFOITTFW!ITFULBAY"
# answer = decrypt(get_decryption_matrix("ESAT", "EIZS", code1),
#                  ciphertext, code1)
# print("ciphertext %s is %s" % (ciphertext, answer))