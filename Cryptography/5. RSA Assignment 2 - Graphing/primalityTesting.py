#https://www.youtube.com/watch?t=2&v=W4UgfGu7cbM <- champs of change link don't lose this
from sympy import *
from random import randint
def methodOne(n):
	prime = "PRIME"
	composite = "COMPOSITE"
	decision = composite
	binaryDecision = True
	number = 2
	while (binaryDecision) and (number < n):
		if n%number == 0:
			binaryDecision = False
			decision = composite
			print("%s : NO"%number)
		else:
			binaryDecision = True
			decision = prime
			print("%s : YES"%number)
			number+=1
	return decision

def millerRabinPrimality(n,k):
	prime = "Probably PRIME"
	composite = "COMPOSITE"
	decision = prime
	###write code here
	if n == 3:
		decision = prime
		break
	else if n == 2:
		decision = composite
		break
	else if n == 1:
		decision = prime
		break
	else if n <= 1:
		decision = "not doable. must be greater than 3"
	else if (n % 2) == 0:
		decision = composite #number is even we are done
		break
	else:
		variable = 2 ** n-1 #this is obviously wrong
		d = 0 #because I don't know what d is yet
		r = 10 #don't know what r is though ngl
		for i in k:
			#the loop thing
			a = randint(2,n-2)
			x = (a ** d ) % n
			if x == 1 or x == (n-1):
				#continue with the algorithm
				for thing in xrange(0,r-1):
					x = (x**2) % n
					if x == 1:
						decision = composite
					else if x = (n-1):
						pass
					else:
						decision = prime #i think??
						#idk what I'm doing

			else:
				decision = prime #i think? or is this composite? What is actually going on??
		'''
		write n − 1 as 2^r(·d, not in the variable) with d odd by factoring powers of 2 from n − 1
		WitnessLoop: repeat k times:
  		pick a random integer a in the range [2, n − 2]
   		x ← ad mod n
   		if x = 1 or x = n − 1 then
    		continue WitnessLoop
   		repeat r − 1 times:
      		x ← x squared mod n
      		if x = 1 then
        		return composite
      		if x = n − 1 then
        		continue WitnessLoop
   		
   		return composite
		return probably prime
		'''
	return decision

n = 23 #temp
print(methodOne(n))
print(millerRabinPrimality(n,3))