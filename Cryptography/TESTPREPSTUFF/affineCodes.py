from sympy import *
#from cryptomath import *
#import Cryptoalphabet as ca 
#alpha = ca.Cryptoalphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def affine_encode(plaintext, a, b):
	process = ""
	cipherFinal = ""
	modulusValue = len(alphabet)
	#removes punctuation from plaintext
	for s in plaintext:
		if s!= '.' and s!= ',' and s!= ' ' and s!= '!' and s!= '?' and s!= '\'':
			process+=s
	#converts to uppercase
	process = process.upper() 
	# converts each character using	y=ax+b(mod 26)
	for letter in process:
		ind = alphabet.index(letter)
		step1 = ind * a
		step2 = step1 + b
		step3 = step2 % modulusValue
		char = alphabet[step3]
		cipherFinal+= char
	# returns the ciphertext string
	return cipherFinal
def affine_decode(ciphertext, c, d):
	stringproc = ""
	plainFinal = ""
	modulusVal = len(alphabet)
	#return plainFinal
	# strip	punctuation	from ciphertext###
	#convert to	uppercase###
	for s in ciphertext:
		if s!= '.' and s!= ',' and s!= ' ' and s!= '!' and s!= '?' and s!= '\'':
			stringproc+=s
	stringproc = stringproc.upper()
	# converts each character using	x=cy+d (mod	26)
	for letters in stringproc:
		index = alphabet.index(letters)
		stepone = index * c
		steptwo = stepone + d
		stepthr = steptwo % modulusVal
		chars = alphabet[stepthr]
		plainFinal += chars
	# note the (c,d) pair are the inverse coefficients of
	#the(a,b) pair used to encode
	# returns the plaintext	string
	return plainFinal
def affine_crack(c1, p1, c2, p2):
	finalSolution = []
	alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #MODIFY THIS EACH TIME
	modulusValues = len(alphabets)
	# c1,p1,c2,p2 are characters
	# c1 is	the	encoded	char of	p1
	c1 = c1.upper()
	c1tol = alphabets.index(c1)
	print(c1tol)
	p1 = p1.upper()
	p1tol = alphabets.index(p1)
	print(p1tol)
	# c2 is	the	encoded	char of	p2
	c2 = c2.upper()
	c2tol = alphabets.index(c2)
	print(c2tol)
	p2 = p2.upper()
	p2tol = alphabets.index(p2)	
	print(p2tol)
	# solves a linear system
	cVal = None
	dVal = None
	# result:	p1	=	c	*	c1	+	d2	and	p2	=	c	*	c2	+	d2	(mod	26)
	# returns	the	pair	(c,	d)	or	None	if	no	solution	can	be	found
	# returns a	pair (c,d) to use in affine_decode
	finalSolution.append(cVal)
	finalSolution.append(dVal)
	return finalSolution

def mod_inverse(a,m):
	x = 1
	for i in range(0,m-1):
		if (a*i) % m == 1:
			x = i
			break
	return x  

#problemset1
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# #test the encode function:
# decrypted1 = "I KNOW' WHO.!?, PUT THE PUMPKIN ON THE CLOCK TOIQD"
# cd1 = 21
# dd1 = 8
# print(affine_encode(decrypted1, cd1, dd1))

# #decryptions:
# encrypted1 = "UKVQCCZQLMRRZOLMALKUVQVRZOYFQYKRQUGT"
# c1 = 5
# d1 = -14
# print(affine_decode(encrypted1, c1, d1))
# encrypted2 = "lqpfzfaifstqufqqjjtakfnvfqnjisvkk"
# c2 = -3
# d2 = 15
# print(affine_decode(encrypted2, c2, d2))
# encrypted3 = "qgxetvepjyleexlkxujyxlksfbrqboxk"
# c3 = 9
# d3 = -21
# print(affine_decode(encrypted3, c3, d3))
# encrypted4 = "cpvvkmtsbkmtkgqlcbsepsbueqlvzcll"
# c4 = 7
# d4 = -14
# print(affine_decode(encrypted4, c4, d4))
# encrypted5 = "axhugoabuzabrloeusbxalxfubudxorhag"
# c5 = 5
# d5 = -18
# print(affine_decode(encrypted5, c5, d5))
# encrypted6 = "lqqlshykibymgsnfskvqlkmdmbmpoxqfma"
# c6 = 21
# d6 = -10
# print(affine_decode(encrypted6, c6, d6))
# encrypted7 = "mxfpyxmxyfyyxqykliimxeymfpkrryxyb" #the one letter crib
# c7 = 17 #?????
# d7 = -14 #????
# print(affine_decode(encrypted7, c7, d7))

#test practice
print()
print("TEST PRACTICE")
newalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encryptMeString = "TABLE"
theAValue = 15
theBValue = 11
print(affine_encode(encryptMeString,theAValue,theBValue)) #encoded to KLAUT
print()
newalpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
decryptMeString = "XMRPQ"
theAValueE = 3
theBValueE = -9
#find C Value
theCValue = 9 #see the driver.py for the Cryptoalpha magic... but also same as below
#find D value
theDValue = 3
#use those in the method
print(affine_decode(decryptMeString,theCValue,theDValue)) #DECODES TO CHAIR

theList = []
theList = affine_crack('F','P','T','R') #c1,p1,c2,p2
print(theList)
#thing that is in the driver, for reference:
#alphabet = Cryptoalpha("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#find the inverse equation first
#invThree = mod_inverse(3,26)
#print(invThree) #spits out 9
#ok, so equation is now 9(x+9) = y
#equation is y = 9x + 81 mod 26
#print(81 % 26) #because you're lazy = 3
#equation is y = 9x + 3 mod 26 for decryption


#avals
# for a in range(1,26):
# 	#bvals
# 	for b in range(-26,1):
# 		string = affine_decode(encrypted7,a,b)
# 		print("A: ", a,"B: ", b, "String: " ,string)
#examples
#i = alpha.getIndex("H")
#c = alpha.charNum(i)
#d = alpha.charNum(100)
#print i + c + d
#print(gcd(124,296))
#print(lcm(148,2560))
#print(mod_inverse(13,142))
#print(mod_inverse(8,17)) #test modulus
# def affine_crack(c1, p1, c2, p2):
# 	finalSolution = []
# 	alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #MODIFY THIS EACH TIME
# 	modulusValues = len(alphabets)
# 	# c1,p1,c2,p2 are characters
# 	# c1 is	the	encoded	char of	p1
# 	c1 = c1.upper()
# 	c1tol = alphabets.index(c1)
# 	print(c1tol)
# 	p1 = p1.upper()
# 	p1tol = alphabets.index(p1)
# 	print(p1tol)
# 	# c2 is	the	encoded	char of	p2
# 	c2 = c2.upper()
# 	c2tol = alphabets.index(c2)
# 	print(c2tol)
# 	p2 = p2.upper()
# 	p2tol = alphabets.index(p2)	
# 	print(p2tol)
# 	# solves a linear system
# 	# c1 = p1*a + b
# 	# c2 = p2*a + b , find a and b
# 	print()
# 	#STEP 1 A:
# 	step1var = p1tol - p2tol
# 	print(step1var)
# 	step1ans = c1tol - c2tol
# 	print(step1ans)
# 	print()
# 	#make sure it is positive
# 	if step1var < 0:
# 		step1var = step1var + modulusValues
# 	if step1ans < 0:
# 		step1ans = step1ans + modulusValues
# 	print(step1var)
# 	print(step1ans)
# 	print()
# 	#STEP 2 A:
# 	inverse = mod_inverse(step1var,modulusValues)
# 	print(inverse)
# 	print()
# 	#STEP 3 A:
# 	almostDone = inverse * step1ans
# 	#STEP 4 A:
# 	aValue = almostDone % modulusValues
# 	#STEP 1 B:
# 	step1bvar1 = p1tol * aValue
# 	step1bvar2 = p2tol * aValue
# 	#STEP 2 B:
# 	step2bvar1 = c1tol - step1bvar1
# 	step2bvar2 = c2tol - step1bvar2
# 	#STEP 3 B:
# 	while (step2bvar1 < 0):
# 		step2bvar1 = step2bvar1 + modulusValues
# 	while (step2bvar2 < 0):
# 		step2bvar2 = step2bvar2 + modulusValues
# 	#STEP 4 B: fixing all the modulus values to be good
# 	if step2bvar1 >= modulusValues:
# 		step2bvar1 = (step2bvar1 % modulusValues)
# 	if step2bvar2 >= modulusValues:
# 		step2bvar2 = (step2bvar2 % modulusValues)
# 	# result:	p1	=	c	*	c1	+	d2	and	p2	=	c	*	c2	+	d2	(mod	26)
# 	#STEP 1 aggregation:
# 	print(step2bvar1)
# 	print(step2bvar2)
# 	if step2bvar1 == step2bvar2:
# 		cVal = aValue
# 		dVal = step2bvar1
# 		finalSolution.append(cVal)
# 		finalSolution.append(dVal)
# 		return finalSolution
# 	else:
# 		return None
# 	# returns	the	pair	(c,	d)	or	None	if	no	solution	can	be	found
# 	# returns a	pair (c,d) to use in affine_decode
