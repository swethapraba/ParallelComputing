import enchant #import dictionary library
from sympy import * #our buddy sympy
from MatrixCiphers import * #helper matrix methods
from Cryptoalpha import * #helper cryptoalphabet methods

dictionary = enchant.Dict("en_US") #english library

alphabet = Cryptoalpha("!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]")#61 char alphabet
m = 61 #mod value

passwordsFile = open("passwords-v2.txt","r") #encrypted passwords file open
allUsersList = []
allUserPassList = []

sizedUserList = []
sizedUserPassList = []

commonPassFile = open("common-passwords.txt","r") #common passwords file open
commonPasswordList = []

encryptionMatrix = Matrix([[0,0],[0,0]]) #this is where the final matrix will be stored once we find it
sillyUser = "" #this is the user who used the commonPassword
sillyEncryptedPassword = "" #this is that user's encrypted password that's in the file
sillyPassword = "" #that person's decrypted password we were able to crack

hackedUser = "" #this is the user we were able to find
hackedEncryptedPassword = "" #that person's encrypted password from the file
hackedPassword = "" #that person's decrypted password

#read in all the common passwords into a list
for common in commonPassFile.readlines():
	common = common.strip() #get rid of the "\n"
	commonPasswordList.append(common) #add it to our list
	print(common)

#for loop going through the logins file line by line
for logins in passwordsFile.readlines():
	logins = logins.strip() #get rid of the "\n"
	(userid, encpwd) = logins.split() #userid = string of username ; encpwd = encrypted password from that person
	allUsersList.append(userid) #add all the userids to a list
	allUserPassList.append(encpwd) #add all the passwords encrypted to a list
	#print(userid + "       " + encpwd)

	if len(encpwd) > 5: #if the password length is more than 5
		sizedUserList.append(userid) #add the username to a separate list
		sizedUserPassList.append(encpwd) #add the password to a separate list
		#print(encpwd)

index = 0 #index of the sized user/sized password
counter = 0 #counter for number of elements
totalCombos = 0
for users in allUsersList:
 	counter += 1 #yay another element has been counted
 	if index < len(allUsersList): #if the index is less than the size of the list of usernames (just a bounds check)
 		thisUserPassword = allUserPassList[index] #pull the password for convenience
 		if len(thisUserPassword) > 5: #is it long enough for us to use?
 			for commonPass in commonPasswordList:
 				totalCombos += 1
 				consideration = commonPass #we have our potential plaintext / the common password being considered
 				#print(users + "    " + thisUserPassword + "     " + consideration)
 				fourCharC = thisUserPassword[:4] #first four characters of the encrypted Password
 				print(fourCharC)
 				fourCharP = consideration[:4] #first 4 characters of the possible common password
 				print(fourCharP)
 		index += 1 #go to the next ones
			
	# 		testMatrix = get_decryption_matrix(fourCharP, fourCharC , alphabet) #plaintext, ciphertext, alphabet
	# 		pprint(testMatrix) #print the test matrix
			
	# 		#testMatrix = get_decryption_matrix(fourCharP, fourCharC, alphabet) #plaintext, ciphertext, alphabet
	# 		#pprint(testMatrix) #print the test matrix
			
	# 		#ok so now to test the matrix to see if it' a good one:

	# 		#determinant = gcd(det(testMatrix),m) #find determinant using the matrixCiphers methods
	# 		#if determinant == 1: #if the gcd is 1, we have an invertible matrix
	# 		#	print(determinant) #just a print statement
	# 		print("end of:    " + common)	
	#index += 1 #go to the next one
print(counter)
print(index)
print(totalCombos)

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

"""
#ok so now we have a matrix that makes these values true. we have no clue if it's good or not
 			if(determinant != 61): #if the determinant is 61 bad things happen?
 				
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
 						

"""

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