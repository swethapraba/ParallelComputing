from sympy import *
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
	prime = "PRIME"
	composite = "COMPOSITE"
	decision = prime
	###write code here
	return decision

n = 23 #temp
print(methodOne(n))
print(millerRabinPrimality(n,3))