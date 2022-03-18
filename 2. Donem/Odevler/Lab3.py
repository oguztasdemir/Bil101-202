"""
#1. soru - Çarpım Tablosu
for x in range(1,11):
    print()
    for y in range(1,11):
        print(x,"x",y,"=",x*y)
        
"""

"""
#2. soru - Hocanın istediği düzende borç hesaplama

yil = int(input("Kaç yıl boyunca ödemek istiyorsunuz: "))
geri_odeme = int(input("Her yıl ne kadar geri ödeme verilecek: "))
faiz = 20/100
toplam_faiz = 0
tutar = int(input("Ne kadar borç istiyorsunuz: "))
tutar = tutar + tutar*faiz
sayac = 1

for i in range(1,yil):
    tutar = tutar-geri_odeme
    tutar = tutar + (tutar*faiz)
    toplam_faiz += tutar*faiz
    sayac += 1
    print("{}. ayın faturası ödenmiştir. Kalan toplam borç {} TL'dir.".format(sayac,tutar))
print("Toplam faiz: ",toplam_faiz)
    

"""




