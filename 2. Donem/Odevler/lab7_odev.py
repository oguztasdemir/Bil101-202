class Bilgisayar:
    def __init__(self,depolama,ram,sistem):
        self.depolama = depolama
        self.ram = ram
        self.sistem = sistem
        Bilgisayar.BilgileriGoster()
        
        
    def BilgileriGoster(self):
        print("Bilgisayarın özellikleri:\nDepolama alanı: {}\nRam: {}\nİşletim Sistemi: {}".format(self.depolama,self.ram,self.sistem))
        
        
        
class Macbook(Bilgisayar):
    pass
class Monster(Bilgisayar):
    pass
class Lenovo(Bilgisayar):
      pass  
        