#my alphabet
myalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def getIndex(c):
	c = c.upper()
	return myalphabet.index(c)
def charNum(i):
	i = i % len(myalphabet)
	return myalphabet[i]
def prepareText(text):
	processes = ""
	#removes punctuation from plaintext
	for s in text:
		if s!= '.' and s!= ',' and s!= ' ' and s!= '!' and s!= '?' and s!= '\'':
			processes = processes + s.upper()
	#converts to uppercase
	#processes = processes.upper() 
	return processes
def affine_encode(plaintext, a, b):
	process = ""
	cipherFinal = ""
	modulusValue = len(myalphabet)
	#removes punctuation from plaintext
	for s in plaintext:
		if s!= '.' and s!= ',' and s!= ' ' and s!= '!' and s!= '?' and s!= '\'':
			process+=s
	#converts to uppercase
	process = process.upper() 
	# converts each character using	y=ax+b(mod 26)
	for letter in process:
		ind = myalphabet.index(letter)
		step1 = ind * a
		step2 = step1 + b
		step3 = step2 % modulusValue
		char = myalphabet[step3]
		cipherFinal+= char
	# returns the ciphertext string
	return cipherFinal
def affine_decode(ciphertext, c, d):
	stringproc = ""
	plainFinal = ""
	modulusVal = len(myalphabet)
	#return plainFinal
	# strip	punctuation	from ciphertext###
	#convert to	uppercase###
	for s in ciphertext:
		if s!= '.' and s!= ',' and s!= ' ' and s!= '!' and s!= '?' and s!= '\'':
			stringproc+=s
	stringproc = stringproc.upper()
	# converts each character using	x=cy+d (mod	26)
	for letters in stringproc:
		index = myalphabet.index(letters)
		stepone = index * c
		steptwo = stepone + d
		stepthr = steptwo % modulusVal
		chars = myalphabet[stepthr]
		plainFinal += chars
	# note the (c,d) pair are the inverse coefficients of
	#the(a,b) pair used to encode
	# returns the plaintext	string
	return plainFinal
def affine_crack(c1, p1, c2, p2):
	return c2
	#o c1,p1,c2,p2	are	characters	
	# c1	is	the	encoded	char	of	p1
	# c2	is	the	encoded	char	of	p2
	# returns	a	pair	(c,d)	to	use	in	affine_decode
	# solves	a	linear	system
	# result:	p1	=	c	*	c1	+	d2	and	p2	=	c	*	c2	+	d2	(mod	26)
	# returns	the	pair	(c,	d)	or	None	if	no	solution	can	be	found
def mod_inverse(a,m):
	x = 1
	for i in range(0,m-1):
		if (a*i) % m == 1:
			x = i
			break
	return x  
def affine_encode_digraph(plaintext, a, b):
	modulusValue = len(myalphabet)
	plaint = prepareText(plaintext)
	ciphertext = ""
	if len(plaint)%2 == 1:
		plaint += "X"
	for i in range(0, len(plaint)//2):
		ciphertext += intToDigraph(((digraphToInt(plaint[2*i] + plaint[2*i+1])*a)+b)%(26**2))
	return ciphertext #####
def affine_decode_digraph(ciphertext, c, d):
	ciphert = prepareText(ciphertext)
	if len(ciphert) % 2 == 1:
		ciphert += "X"
	plaintext = ""
	for i in range (0,len(ciphert)//2):
		plaintext += intToDigraph(((digraphToInt(ciphert[2*i]+ciphert[2*i+1])*c)+d)%(26**2))
	return plaintext
def digraphToInt(s):
    one = myalphabet.index(s[0])*26
    two = myalphabet.index(s[1])
    return one + two ####
def intToDigraph(i):
    thingone = charNum((i-i%26)//26)
    thingtwo = charNum(i)
    return thingone + thingtwo ####
    #return a digraph computer from the integer i

#problem set 2
#last few questions
#messageToCode1 = "HELLO"
messageToCode = "I can use modular equations to encode messages"
a = 5
b = 10
ciphered = affine_encode_digraph(messageToCode,a,b)
print(ciphered)
print(mod_inverse(5,676))
print(5410 % 676)

c = 541
d = -2
decrypted = affine_decode_digraph(ciphered,c,d)
print(decrypted)

print()
print()
myMessage = "baby"
myA = 117
myB = -35
print(affine_encode_digraph(myMessage,myA,myB))
print()
theMessage = "MQQO"
theA = 31 # mod 5...
theB = 29 # mod 3...

theC = 21
theD = -11
print(affine_decode_digraph(theMessage,theC,theD))
#encodeMe = "On November 15th I will be 17"
#encodeMe = "my name is Swetha"
#cipher = affine_encode(encodeMe,a,b)
#print(cipher)

#print(mod_inverse(5,36)) #29
#print(290 % 36) #2

#c = 29 #inverses
#d = -2
#decoded = affine_decode(cipher,c,d)
#print(decoded)

#the table
#for i in range(26,40):
#	print(i*2, '|', ((i*2)+1), '|', ((i*2)+1)*(i*2))
