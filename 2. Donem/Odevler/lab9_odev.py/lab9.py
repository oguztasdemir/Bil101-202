class Dosya():
    def __init__(self,dosya_adi):
        #Dosya sınıfının yapıcı fonksiyonudur.
        self.dosya=dosya_adi
        Dosya.dosya_boyut(self)
    
    def dosya_boyut(self):
        #dosyanın kaç satırdan oluştuğu bilgisini return edecek. Ekrana birşey yazdırmayacak.
        global sayac
        sayac = 0
        dosya_satir = open(self.dosya,"r",encoding="utf-8").readlines()
        for i in dosya_satir:
            sayac += 1
        return sayac
        Dosya.dosya_icerik(self)

    def dosya_icerik(self):
        #Dosyanın içeriğini okuyup ekrana yazdıracak. Dosyayı okurken try except yapısını kullanmak zorundasınız
        global oku
        dosya_satir = open(self.dosya,"r",encoding="utf-8")
        try:
            oku = dosya_satir.read()
            print(oku)
        except:
            print("Belirlenemeyen bir nedenden dolayı dosya içeriği ekrana yazdırılamamıştır.")
        finally:
            Dosya.dosya_baslik(self)
        


    def dosya_baslik(self):
        #Dosyanın ilk satırını okuyacak. İlk satır başlıktır.
        # Bunu return ile verecek. Ekrana birşey yazdırılmayacak.
        dosya_baslik = open(self.dosya,"r",encoding="utf-8")
        Dosya.dosya_yaz(self,yazilacak)
        return dosya_baslik.read()
        


    def dosya_yaz(self,yazilacak): ###bu kısıma global yazilacak ekleyip giriş parametlerinden yazilacak kısmını silebilirdim
        #yazılacak parametresi ile verilenleri dosyanın sonuna yazacak.
        dosya_yazi = open(self.dosya,"a",encoding="utf-8")
        yazilacak = str(input("Lütfen dosya sonuna ne yazmak istiyorsanız o metini giriniz."))
        dosya_yazi.write("\n{}".format(yazilacak)) ### Direkt en alt satırda yazmasını istediğim için \n komutunu kullandım.
        dosya_yazi.close()
        Dosya.dosya_bul(self,aranan)


    def dosya_bul(self,aranan):
        #Aranan ile verilecek olan ifade dosya içinde aranacak. Eğer dosyada var ise true dosyada yok ise false değerini döndürecek.
        dosya_baslik = open(self.dosya,"r",encoding="utf-8")
        arama = dosya_baslik.read().find(aranan)

        if arama != -1: ### -1 yazma nedenim eğer find kısmında aradığımız metin yoksa sonuç -1 çıkmaktadır.
            print("Dosya içerisinde {} ifade bulunmamaktadır.".format(aranan))
        else:
            print("Dosya içerisinde {} ifadesi bulunmaktadır.".format(aranan))
        Dosya.dosya_yolu(self,dosya)


    def dosya_yolu(self,dosya):
        #Dosyayı ayrıştırarak dosyanın yolunu ekrana yazdıracak.        
        print("Açtığınız dosya {} adlı uzantı üzerinden açılmıştır.".format(dosya))
        print("_________________")
        pass
    

###kod için gerekli bilgiler
yazilacak = 0
aranan = "Lütfen"
dosya = "/Users/yarentasdemir/Desktop/odev/Yazilim/Lab10.txt"  ###Macbook kullanıyorum o yüzden uzantı bu şekilde olmaktadır. Windows/Linux için kendi uzantı şeklinizde yazmanız gerekmektedir.
dosya_nesnem=Dosya(dosya)


###Dosya ile alakalı returnlu fonksiyonların printlerini bu kısıma kodum doğru mu diye test etmek amacıyla yazıyorum
print("Dosyanın satır sayısı: ",sayac)
print('Dosyanın başlığı: ',dosya_nesnem.dosya_baslik())






###hocam bu kısmı siz göndermişsiniz, ben direkt kod içerisinde gerekli yerlerde bu kodları belirttim o yüzden görünmez metine alıyorum
"""
if __name__ == "__main__":
# Tanımladığımız Dosya sınıfını test etmek için kodlarımızı bu bölüme yazacağız. Bazılarının örneği aşağıdaki gibi yazılmıştır.
#Üzerinde işlem yapılan dosya tüm dizini ile birlikte dosya değişkenine aktarılmıştır.dosya="D:/python örnekler/test doyam.txt"
#Dosya sınıfından bir nesne oluşturmak için yapıcı fonksiyonunda tanımlandığı gibi bir dosya belirtmemiz gerekir.


if dosya_nesnem.dosya_bul(aranan):
    print("Aranan kelime dosya içerisinde bulunmuştur")
else:
    print("Aranan kelime dosya içerisinde bulunamamıştır.")
"""
