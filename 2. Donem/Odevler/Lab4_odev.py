"""
#1. soru
import matplotlib.pyplot as plt
x = []
for i in range(-10,11): 
    x.append(i)
y = []
for j in range(-10,11):
    j = j**3
    y.append(j) 
plt.plot(x , y , color = "r" ) 
plt.title("$y=x^3$ Grafiği") 
plt.xlabel("x ekseni") 
plt.ylabel("y ekseni") 
plt.show()
"""

"""
#2. soru
x = int(input("Bir sayı giriniz"))

def Satır(x):
    for i in range(x+1):
        print("*"*i)

Satır(x)

"""


"""
#3. soru

print("İstanbul Medeniyet Üniversitesi Not Hesaplama Algoritması")

vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))

def Ortalama(vize,final):
    return vize*(40/100) + final*(60/100)

Ortalama(vize,final)
"""
    

