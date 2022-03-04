
"""
#1. soru

import math


x = 10

while x < 500:
    f = ((math.log(x**2)) * 3*x) / math.sqrt(x-2)
    print(f)
    x += 1
    
"""






#2. soru    
    
def alan_hesapla(x ,y):
    i = 1
    e = 1
    while (i <= x and i <= y):
        if (not x % i) and (not y % i) :
            e = i
        i += 1

    print("Girilen dikdörtgenden çıkarabilecek en büyük karenin alanı {} cm karedir".format(e**2))
    
    
 
x = int(input("Lütfen bir kenarın boyunu  giriniz: (cm cinsinden)"))
y = int(input("Lütfen diğer kenarın boyunu giriniz: (cm cinsinden"))

if (x > 0) and (y > 0):
    alan_hesapla(x,y)

else:
    print("Girdiğiniz değerler negatiftir. Pozitif değer almanız gerekmektedir.")
    
    

    
    
    