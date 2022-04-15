
class Bilgisayar:
    def __init__(self,marka,yil,ram,harici,dxdiag):
        self.marka = marka
        self.yil = yil
        self.ram = ram
        self.harici = harici
        self.dxdiag = dxdiag


    def Yaz(self):
        print("Bilgisayarın markası: ",self.marka)
        print("Bilgisayarın üretiliş yılı: ",self.yil)
        print("Bilgisayarın ramı: ", self.ram)
        print("Bilgisayarın depolama alanı (GB): ",self.harici)
        print("Bilgisayarın ekran kartı (GB): ",self.dxdiag)
        Bilgisayar.Marka(self)
        
    def Marka(self):
        if self.marka ==("Macbook" or "macbook" or "mac"):
            print("macOS işletim sistemli bilgisayardır.")
        elif self.marka !=("Macbook" or "macbook" or "mac"):
            print("Bilgisayarınızın işletim sistemi Linux veya Windows'tur.")
        Bilgisayar.Yil(self)
    
    def Yil(self):
        if int(self.yil) > 2020:
            print("Bilgisayarınız yeni bir modeldir.")
        elif 2020 >= int(self.yil) > 2012:
            print("Bilgisayarınız orta eskilikte bir bilgisayardır.")
        else:
            print("Bilgisayarınızı değiştirmeyi düşünebilirsiniz.")
        Bilgisayar.Ram(self)
    
    def Ram(self):
        for i in range(0,1024,2**2):
            if self.ram == i:
                print("Bilgisayar raminiz (GB): ", self.ram)
                break
            else:
                pass
        Bilgisayar.Depolama(self)
        
    def Depolama(self): 
        for i in range(0,2048,2**2):
            if self.harici == i:
                print("Bilgisayarınızın depolama alanı (GB): ", self.harici)
                if self.harici <= 256:
                    print("Depolama alanınız 256GB'den düşüktür. SSD alıp bilgisayarınızı daha rahat kullanabilirsiniz.")
                elif 256 < self.harici <= 512:
                    print("Depolama alanınız ideal bir boyuttadır. Bilgisayarınızdaki çerezleri düzenli olarak temizlerseniz sorun yaşamazsınız.")
                else:
                    print("Bilgisayarınızın depolama alanı oldukça yeterli. Ek bir donanıma ihtiyacınız yok.")
                break
            else:
                pass
        Bilgisayar.dxdiag(self)    
    
    def dxdiag(self):
        if self.dxdiag <= 1:
            print("Bilgisayarınızın ekran kartı oldukça düşük. Ek donanım kullanmanız gerekebilir.")
        elif 1 < int(self.dxdiag) <= 2:
            print("Bilgisayarınızın ekran kartı düşük grafikli oyunlar oynamanız için yeterlidir fakat bilgisayarınız gerekenden çok fazla ısınabilir.")
        elif 2 < int(self.dxdiag) <= 6:
            print("Bilgisayarınızın ekran kartı iyi seviyededir. Bilgisayarınızı çok zorlamadığınız sürece bir sorun yaşamazsınız.")
        elif 6 < int(self.dxdiag) <= 32:
            print("Bilgisayarınızda kripto para kazımı dışında her şeyi yapabilirsiniz.")
        elif 32 < int(self.dxdiag):
            print("Bilgisayarınızda her işi yapabilirsiniz.")
            
            
pc1 = Bilgisayar("Macbook",2021,8,256,1)
pc2 = Bilgisayar("HP",2010,2,128,7)
pc3 = Bilgisayar("Monster",2022,32,1024,32)
pc1.Yaz()
print("")
pc2.Yaz()
print("")
pc3.Yaz()

