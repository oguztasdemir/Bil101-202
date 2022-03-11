"""
#1. uygulama

isim = input("İsminizi giriniz: ")
maaş = int(input("Maaşınızı giriniz: "))
yıl = int(input("Şirkette kaç yıldır çalışıyorsunuz: "))

if 0 < yıl <= 5:
    zam = maaş*(13/100)
    maaş += zam
    print("Sayın {}, zamlı maaşınız {} TL".format(isim,maaş))
    
if 6 <= yıl <= 10:
    zam = maaş*(20/100)
    maaş += zam
    print("Sayın {}, zamlı maaşınız {} TL".format(isim,maaş))
    
if 11 < yıl:
    zam = maaş*(30/100)
    maaş += zam
    print("Sayın {}, zamlı maaşınız {} TL".format(isim,maaş))
    """
    

"""
#2. uygulama

kenar1 = int(input("Bir kenarı giriniz: "))
kenar2 = int(input("Bir kenarı giriniz: "))
kenar3 = int(input("Bir kenarı giriniz: "))

if kenar1 == kenar2 == kenar3:
    print("Bu girilen üçgen eş kenar üçgendir.")
    
elif kenar1 == kenar2 or kenar2 == kenar3 or kenar1 == kenar3:
    print("Bu girilen üçgen ikiz kenar üçgendir.")

elif kenar1 != kenar2 != kenar3:
    print("Bu girilen üçgen çeşitkenar üçgendir.")
    """
