import random
def RANDOM(s1):
    seq=""
    seq="".join([random.choice("ATGC") for _ in range(10)])
    return seq

x=RANDOM("")
y=RANDOM("")

def match(s1,s2):
    if not len(s1)==len(s2):
        return False
    for i in range(len(s1)):
        if not s1[i]==s2[i]:
            return False
    return True

def LCS(s1,s2):
    i=0
    while i<len(s1) and i<len(s2) and s1[-i]==s2[-i]:
        i+=1
    print(s1[-i:])


def LCP(s1,s2):
    i=0
    while i<len(s1) and i<len(s2) and s1[i]==s2[i]:
        i+=1
    print(s1[:i])

def RevCom(s):
    complement = {"A": "T", "G": "C", "T": "A", "C": "G"}
    t = ''
    for base in s:
        t = complement[base] + t
    print("Reverse complement of", s, "is", t)

RevCom(x)
match(x,y)
LCP(x,y)
LCS(x,y)
    


