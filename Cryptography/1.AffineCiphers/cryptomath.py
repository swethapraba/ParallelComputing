import math
def gcd(x,y):
	#returns the gcd of ints x and y (take abs val of input)
	return math.gcd(x,y)
def lcm(x,y):
	if x > y:
		greater = x
	else:
		greater = y
	while(True):
		if((greater % x == 0) and (greater % y == 0)):
			lcm = greater
			break
		greater += 1
	return lcm
	#returns lcm of ints (take abs val of input)
def mod_inverse(a,m):
	x = 1
	for i in range(0,m-1):
		if (a*i) % m == 1:
			x = i
			break
	return x   
    #returns 0<x<m such that a x =1 (mod m) if x exists and None otherwise
def lin_solve(a,b,c,m):
	return b
    #returns x such that a x + b = c (mod m), where 0 <=x < m, if exists; none otherwise
def lin_sys_solve(a,b,c,d,e,f,m):
	return c
    #solves the linear system ax + by = c; dx + ey = f (mod m) for x and y
    #returns a pair (x, y) if the pair exists and none otherwise
def lin_inverse(a,b,m):
	return m
    #returns (c,d) such that y=ax+b (mod m) implies x = cy+d (mod m)