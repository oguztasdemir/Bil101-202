sayi = int(input("Lütfen kaça kadar yazılmasını istiyorsanız o sayıyı giriniz: "))

def listeOlustur(sayi):
    ls = []
    for i in range(0,sayi):
        ls.append(i)
        
    return ls

listeOlustur(sayi)
