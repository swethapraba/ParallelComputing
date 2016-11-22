class Cryptoalphabet:
def _init_(self, alphabet):
    self.alphabet = alphabet.upper()
def getIndex(self, c):
    c = c.upper()
    return self.alphabet.index(c)
def charNum(self, i):
    i = i % len(self.alphabet)
    return self.alphabet.charAt(i)
def prepare(self,s):
    v = ""
    for c in s:
        if c.isalpha():
            v = v + c.upper()
    return v
def digraphToInt(self, s):
    print "hi" #return an int computed from the indices of s
def intToDigraph(self, i):
    print "please stop crashing please"
    #return a digraph computer from the integer i