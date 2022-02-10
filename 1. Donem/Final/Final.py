"""
#1. soru
def reverseList(L):
    new_L=[]
    for i in range(len(L)-1,-1,-1):
        new_L.append(L[i])
    return new_L
"""


"""
#1. soru (deneme)
def reverseList(L): 
    L.reverse() 
    return L
      
L = [1, "aa", 3, 2, 4, 5] 
print(L)
print(reverseList(L))
"""



"""
#2. soru
def elemanSayisi(L,element):
    i=0
    for e in L:
        if e==element:
            i+=1
    return i 
"""




"""
#3. soru
def paraAt(P):
    prob=random.randint(1,100)
    if prob<=P[0]*100:
        return 0
    else: 
        return 1

import random
print(paraAt([0.6,0.4]))
"""




"""
#4. soru
def maliyet(S,i):
    M = [[10,36,22,15,62],
        [12,35,20,12,66],
        [13,37,21,16,59]]
    sum=0
    for j in range (0,len(M[i])):
        sum+=S[j]*M[i][j]
    return sum
"""




"""
#4. soru (deneme)
def maliyet(S,i):
    M = [[10,36,22,15,62],
        [12,35,20,12,66],
        [13,37,21,16,59]]
    sum=0
    for j in range (0,len(M[i])):
        sum+=S[j]*M[i][j]
    return sum

S = [1,1,4,2,3]
print(maliyet(S,2))
"""




"""
#5. soru

def tepeNoktalari(L):
    liste=[]
    if len(L)==1:
        return L
    for i in range(0,len(L)):
        if i==0 and L[i]>=L[i+1]:#ilk eleman
            liste.append(L[i])
        elif i==len(L)-1 and L[i]>=L[i-1]:#son eleman
            liste.append(L[i])
        else:#diğer elemanlar
            if L[i]>=L[i-1] and L[i]>=L[i+1]:
                liste.append(L[i])
    return liste
print(tepeNoktalari([3,2,4,5,4,3,2,2]))
"""