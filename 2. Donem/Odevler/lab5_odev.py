#çamaşır makinesi - 20 yıllık - beko
#bulaşık makinesi - 10 yıllık - arçelik
#buzdolabı - 6 yıllık - bosch
#tespitEt() ile >10 yıllık ürün bilgilerini ekrana yazdıracağım

class BeyazEsya():
    def __init__(self,urun,yil,marka):
        self.urun = urun
        self.yil = yil
        self.marka = marka
      

    def Bilgiler(self):
        print("""10 yıldan yaşlı olan ürünler
Ürün: {}, Yılı {}, Marka{}""".format(self.urun,self.yil,self.marka))
                    
    def TespitEt(kontrol):
        for i in kontrol:
            if int(i.yil) > 10:
                i.Bilgiler()


urunler = []
camasir_makinesi = BeyazEsya("Çamaşır Makinesi","20","Beko")
bulasik_makinesi = BeyazEsya("Bulaşık Makinesi","10","Arçelik")
buzdolabi = BeyazEsya("ÇBuzdolabı","6","Bosch")
urunler.append(camasir_makinesi)
urunler.append(bulasik_makinesi)
urunler.append(buzdolabi)

BeyazEsya.TespitEt(urunler)