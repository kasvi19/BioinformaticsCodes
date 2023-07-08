import random

# Creating a random sequence of 10 bp:
def RANDOM(s1):
    seq=""
    seq="".join([random.choice("ATGC") for _ in range(10)])
    return seq

x=RANDOM("")
y=RANDOM("")

# Checking whether the two sequences are identical:
def match(s1,s2):
    if not len(s1)==len(s2):
        return False
    for i in range(len(s1)):
        if not s1[i]==s2[i]:
            return False
    return True
    
# Function to find the longest common suffix:
def LCS(s1,s2):
    i=0
    while i<len(s1) and i<len(s2) and s1[-i]==s2[-i]:
        i+=1
    print(s1[-i:])

# Function to find the longest common prefix:
def LCP(s1,s2):
    i=0
    while i<len(s1) and i<len(s2) and s1[i]==s2[i]:
        i+=1
    print(s1[:i])
    
# Function to find the Reverse Complement of the string:
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
    


