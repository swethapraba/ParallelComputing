from sympy import *
def matrix_mod(M, m):
    return M.applyfunc(lambda x: Mod(x, m))

class Cryptoalpha:
    def __init__(self, alphabet):
        self.alphabet = alphabet.upper()
        self.m = len(self.alphabet)

    def getIndex(self, c):
        c = c.upper()
        return self.alphabet.index(c)

    def charNum(self, i):
        i = i % len(self.alphabet)
        return self.alphabet[i]

    def prepare(self, s):
        v = ""
        for c in s:
            if c in self.alphabet:
                v = v + c.upper()
        return v

    def digraphToInt(self, s):
        # return an int computed from the indices of s
        return self.getIndex(s[0]) * self.m + self.getIndex(s[1])

    def intToDigraph(self, i):
        # return a digraph computed from the integer i
        return self.charNum((i - i % self.m) / self.m) + self.charNum(i)

    def pad_s(self, s, padchar="X"):
        """ Add padchar (default 'X') to s if length of s is odd"""
        if (len(s) % 2) == 1: #if(s.len % 2) == 1:######
            s += padchar
        return s

    def pad_a(self, a, padchar="X"):
        """ Add the numerical value of padchar (default 'X') to list a if length of a is odd """
        # you may not need this function in your code
        pass

    def StoM(self, S):
        """ Return a 2 x C matrix formed from the even-length string S, where C = len(S)/2"""
        assert len(self.stoa(S)) % 2 == 0
        return Matrix(self.stoa(S)).reshape(len(self.stoa(S)) // 2, 2).transpose()
        #the matrix is returned as a matrix of numbers

    def MtoS(self, M):
        """ Turn a 2 x C matrix of numbers into a string S, where len(S) = C*2 """
        lists = []
        shaped = M.shape #(row, col): (tuple with 2 values)
        maxcol = shaped[1]
        #get to a list of numbers
        for c in range(maxcol): # 0 value to whatever max col value - 1
            lists.append(M[0,c])
            lists.append(M[1,c])
        #numbers list becomes a string
        stringNum = ""
        for i in range(len(lists)):
            tempstr = lists[i]
            stringNum+= (str)(tempstr)
        stringLet = self.atos(lists)
        return stringLet

    def stoa(self, s):
        list = []
        ###padding the string with an extra char at the end if necessary
        string = s
        self.pad_s(string, "X")
        ###Turn a string s into an (even-length) list of numbers, using getIndex()
        for letter in string:
            temp = self.getIndex(letter)
            list.append(temp)
        return list

    def atos(self, a):
        """ Turn a list of numbers into a string, using charNum(),
            does not assume len(a) is even """
        stringvalues = ""
        for number in a:
            temp = self.charNum(number)
            stringvalues += temp
        self.pad_a(stringvalues, "X")
        return stringvalues
#EXTRA AFFINE METHODS
    def mod_inverse(a,m):
        x = 1
        for i in range(0,m-1):
            if (a*i) % m == 1:
                x = i
            break
        return x  