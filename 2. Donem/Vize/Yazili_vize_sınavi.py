"""
#sınıf-nesne nedir?
#1. soru:
Sınıf (Class): Sınıfın herhangi bir nesnesini karakterize eden bir özellik kümesi tanımlayan bir nesne için kullanıcı tanımlı bir prototiptir. Sınıf özellikleri üyelere, değişkenlere ve metotlara sahiptir. İyi bir sınıf tasarımı için yazılımcının soyutlama (abstraction) işlemini çok iyi yapması gerekir.
Nesne (Object): Sınıfı tarafından tanımlanan bir veri yapısının benzersiz bir örneğidir. Bir nesne, hem veri üyelerini (sınıf değişkenleri ve örnek değişkenleri) ve yöntemleri içerir. Operatörlerin aşırı yüklenmesi (Operator overloading): Belirli bir operatöre birden fazla işlevin atanmasıdır.
"""


"""
giriş-çıkış parametreleri nedir?
#2. soru
Giriş parametresi: Fonksiyona tanımlanan parametredir. def ... (giriş paremetreleri): şeklinde () içerisine giriş paremetreleri yazılır.
Çıkış parametresi: Fonksiyondan çıkan parametredir. Genellikle return ile birlikte yazılır fakat return ile yazıldığında bazı idelerde (visual studio gibi) return sonucu kullanıcıya gösterilmez, buna ek olarak returndan önce print fonksiyonu eklenerek sonuç kullanıcıya gösterilebilir.

"""



"""
#Bir kenar parametresi verilen karenin alan ve çevresini hesaplayan AlanCevreBul() fonksiyonunu tamamlayınız.
#3. soru

def AlanCevreBul(kenar):
    alan = kenar**2
    cevre = kenar*4
    return alan,cevre
"""


"""
# x listesinde tanımlı öğrencilerden istenilen bir isimdeki öğrencinin listede kaç adet olduğunu bulmak
#4. soru
x = ["ali","ayşe","fatma","muhammet"] #kişiler arttırılabilir
y = input("Hangi öğrenciyi aratmak istersiniz: ")
sayac = 0
kisi = 0

try: 
    while True:
        if y == x[sayac]:
            kisi += 1
        sayac += 1
except:
    print("Sınıfta {} adında {} adet kişi bulunmaktadır.".format(y,kisi))
"""



"""
#5. soru
class Personal:
    def __init__(self,ad,gorev,maas):
        self.ad = ad
        self.gorev = gorev
        self.maas = maas
        Personal.BilgileriGoster(self)
        
        
    def BilgileriGoster(self):
        print("Çalışma")
        
    def maasaZamla(self,oran):
        oran = 10/100
        self.maas = self.maas + (self.maas*oran)
        print("Yeni maaş")
        
calisan1 = Personal("Oğuz Taşdemir","Öğrenci","25000")
#50 farklı kişinin nesneleştirildiğini farz edelim


x = []
x.append(calisan1)
#buraya 50 farklı kişinin listelendiğini farz edelim

gorev = 0
for i in x:
    if i.gorev == "Ogrenci":
        print(i)
        gorev += 1
        
print("Öğrenci görevine sahip {} adet kişi bulunmuştur.".format(gorev))
"""