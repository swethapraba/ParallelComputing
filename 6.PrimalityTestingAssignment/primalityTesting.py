from sympy import *
from numb
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
	prime = "Probably PRIME" #true
	composite = "COMPOSITE" #false
	###write code here
	if n == 3:
		return True
	else if n == 2:
		return False
	else if n == 1:
		return True
	else if n <= 1:
		return False
	else if (n % 2) == 0:
		return False #number is even we are done
	else:
		r,d = factor(n-1) #must start with an even number!
		for i in range(k):
			#the loop thing
			a = random.randrange(2, n-1)
			x = pow(a,d,n)
			if x==1 or x== (n-1):
				continue
			done = False
			while r > 0 and not done:
				x = pow(x,2,n)
				if x ==1:
					return False
				if x== n-1:
					done = True
				r = r-1
			if not done:
				return False
	return True

def factor(n):
	#r is the number of steps
	#d is that odd number
	r = 0
	d = n
	if d % 2 == 0:
		r = r+1
		d = d//2
	else:
		r = r
		d = d
		return r, d
	return r, d
		'''
		write n − 1 as 2^r(·d, not in the variable) with d odd by factoring powers of 2 from n − 1
		WitnessLoop: repeat k times:
  		pick a random integer a in the range [2, n − 2]
   		x ← ad mod n
   		if x = 1 or x = n − 1 then
    	continue WitnessLoop
   		repeat r − 1 times:
      	x ← x2 mod n
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