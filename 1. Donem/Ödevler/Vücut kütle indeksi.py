
kilo = float(input("Lütfen kilonuzu giriniz (Kg): "))
boy = float(input("Lütfen boyunuzu giriniz(M): "))

endeks = kilo / boy**2

if endeks < 20:
    print("Zayıfsınız. Kütle endeksiniz: ", endeks)


elif 20 < endeks < 25 :
    print("İdeal kilodasınız. Kütle endeksiniz: ", endeks)


elif 25 < endeks < 30:
    print("Kilolusunuz. Kütle endeksiniz: ", endeks)  


elif 30 < endeks:
    print("Obezsiniz. Kilo vermelisiniz. Kütle endeksiniz: ", endeks)          


