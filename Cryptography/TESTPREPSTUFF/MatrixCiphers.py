from Cryptoalpha import *
from sympy import *
from random import randint

def encrypt(E,p,a):
    return a.MtoS(matrix_mod(E*a.StoM(p),len(a.alphabet)))
    """Apply matrix E to string p mod 26 and return an encrypted string, relative to Cryptoalpha a """
def decrypt(D,c,a):
    return a.MtoS(matrix_mod(D*a.StoM(c),len(a.alphabet)))
    ####"""Apply matrix D to string c mod 26 and return a decrypted string, relative to Cryptoalpha a """
def get_decryption_matrix(P,C,a):
    """ Knowing two digraphs in string P are encoded as string C, determine a unique decryption matrix, relative to Cryptoalpha a """
    pdione = P[:2] #first plain digraph - letters string
    pditwo = P[2:] #second plain digraph - letters string
    cdione = C[:2] #first cipher digraph - letters string
    cditwo = C[2:] #second cipher digraph - letters string
    pdioneN = a.stoa(pdione) #make letters into numbers list
    pditwoN = a.stoa(pditwo) #make letters into numbers list
    cdioneN = a.stoa(cdione) #make letters into numbers list
    cditwoN = a.stoa(cditwo) #make letters into numbers list
    #ROUND TWO CODE
    plainmatrixnums = Matrix([[pdioneN[0],pditwoN[0]],[pdioneN[1],pditwoN[1]]]) #plaintext number matrix P
    #print("plainmatrix: ")
    #pprint(plainmatrixnums)
    ciphermatrixnums = Matrix([[cdioneN[0],cditwoN[0]],[cdioneN[1],cditwoN[1]]])#ciphertext number matrix C
    #print("ciphermatrix: ")
    #pprint(ciphermatrixnums)
    #find inverse of the cipher matrix
    cipherinverse = ciphermatrixnums.inv_mod(len(a.alphabet))
    #print("CipherInv: ")
    #pprint(cipherinverse)
    d = plainmatrixnums*cipherinverse #multiply plain with the cipher inverse to get d
    #print("D")
    #pprint(d)
    dModed = Matrix([
        [(d[0,0]%len(a.alphabet)), (d[0,1]%len(a.alphabet))],
        [(d[1,0]%len(a.alphabet)), (d[1,1]%len(a.alphabet))]
    ])
    #pprint(dModed)
    return dModed
def get_random_invertible_matrix(m):
    """ return a random 2x2 matrix M with gcd(det(M),m)= 1 """
    d = 2
    M = Matrix([[0,0],[0,0]])
    while d>1:
        #make a random 2x2 matrix, M, and let d = gcd(M, m)
        M = Matrix([[randint(0,m),randint(0,m)],[randint(0,m),randint(0,m)]])
        #range is 1 to m-1 -> your modulus value is the top
        d = gcd(det(M),m)
        #this must be last line; if the gcd is not 1 then you don't have an invertible matrix
    return M