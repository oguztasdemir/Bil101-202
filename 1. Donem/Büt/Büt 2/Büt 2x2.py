
import random
import numpy as np
import matplotlib.pyplot as plt


n = 0
kazanan_strateji = []    #Stratejileri gösterir
strateji_sayı = []       #Strateji sayılarını listeye çevirir

#Oyuncu ekleme kısmı
while n < 1000:
 oyuncu_sayac = 0
 oyuncu_tur = 0
 oyuncu_puan = 0
 oyuncu_list = []         #Oyuncuların yazıldığı liste
 strateji_liste = []      #Stratejilerin yazıldığı liste
 puan_liste = []          #Puanların yazıldığı liste
 oyuncu_total_puan = []   #Tüm puanların yazıldığı liste
 tur= 0

 def OyuncuEkleme(oyuncu_sayac, oyuncu_list):
    sayac = 1
    while sayac <= 100:
        oyuncu_list.append("oyuncu_"+str(sayac))
        oyuncu_puan_ekle = 0
        oyuncu_total_puan.append(oyuncu_puan_ekle)
        sayac += 1
        #print(oyuncu_list)
    Stratejiler(oyuncu_list, strateji_liste)


#Stratejileri oyunculara yükleme kısmı
 def Stratejiler(oyuncu_list, strateji_liste):
    sayac = 0
    while sayac <= 99:
        #oyuncu_list[sayac] 
        stratejiler = random.randint(1,3)

        strateji_liste.append(stratejiler)
        #print("{} numaralı oyuncuya {} numaralı strateji uygulanmıştır".format(oyuncu_list[sayac], stratejiler))
        sayac += 1
    Zar(oyuncu_puan, oyuncu_tur, puan_liste, strateji_liste, oyuncu_list, oyuncu_total_puan, tur)



#Oyuna başlama kısmı
 def Zar(oyuncu_puan, oyuncu_tur, puan_liste,strateji_liste, oyuncu_list, oyuncu_total_puan, tur):
    a = 1
    sayac = 0
    
    #Tüm oyuncular için
    while a == 1:
        b = 1
        oyuncu_puan = 0

        #1 oyuncuya odaklanmak için
        #print("Sıra şu oyuncuda: ", int(sayac)+1)
        while b == 1:
            zar = random.randint(1,6)
            #print("Atılan zar",zar)
            if zar == 1:
                oyuncu_tur = 0
                oyuncu_puan += oyuncu_tur
                b = 0
            else: 
                b = 1
                oyuncu_tur += zar
                
                
                #1. strateji
                if strateji_liste[sayac] == 1:
                        if oyuncu_tur < 20:
                            b = 1
                        else:
                            oyuncu_puan += oyuncu_tur
                            oyuncu_total_puan[sayac] += oyuncu_puan
                            puan_liste.append(oyuncu_total_puan)
                            b = 0
                            #print("Bu tur kazandığı puan: ", oyuncu_puan)
                            #print("Bu tur kazandığı puan: ", oyuncu_puan, "Tüm turlar bazında kazandığı puan: ", oyuncu_total_puan[sayac])
                            
                            if int(oyuncu_total_puan[sayac]) < 100:
                                a = 1
                            else:
                                a = 0
                                print("Oyun bitti")
                                kazanan(sayac,oyuncu_puan, oyuncu_tur, puan_liste, strateji_liste, oyuncu_list, oyuncu_total_puan, tur)
                            
                #2. strateji
                elif strateji_liste[sayac] == 2:
                        if oyuncu_tur < 30:
                            b = 1                                
                        else:
                            oyuncu_puan += oyuncu_tur
                            oyuncu_total_puan[sayac] += oyuncu_puan
                            puan_liste.append(oyuncu_total_puan)
                            b = 0
                            #print("Bu tur kazandığı puan: ", oyuncu_puan, "Tüm turlar bazında kazandığı puan: ", oyuncu_total_puan[sayac])
                            #print("Sıra diğer oyuncuya geçiyor.\n")

                            if int(oyuncu_total_puan[sayac]) < 100:
                                a = 1
                            else:
                                a = 0
                                print("Oyun bitti")
                                kazanan(sayac,oyuncu_puan, oyuncu_tur, puan_liste, strateji_liste, oyuncu_list, oyuncu_total_puan, tur)

                #3. strateji
                elif strateji_liste[sayac] == 3:
                        if oyuncu_tur < (20 + int(max(oyuncu_total_puan))) / 6:
                            b = 1
                        else:
                            oyuncu_puan += oyuncu_tur
                            oyuncu_total_puan[sayac] += oyuncu_puan
                            puan_liste.append(oyuncu_total_puan)
                            b = 0
                            #print("Bu tur kazandığı puan: ", oyuncu_puan, "Tüm turlar bazında kazandığı puan: ", oyuncu_total_puan[sayac])
                            #print("Sıra diğer oyuncuya geçiyor.\n")

                            if int(oyuncu_total_puan[sayac]) < 100:
                                a = 1
                            else:
                                a = 0
                                print("Oyun bitti")
                                kazanan(sayac,oyuncu_puan, oyuncu_tur, puan_liste, strateji_liste, oyuncu_list, oyuncu_total_puan, tur)


#Tur yenileme                                
        sayac += 1
        if sayac < 100:
                sayac = sayac
        else:
                sayac = 0
                
    
 def kazanan(sayac,oyuncu_puan, oyuncu_tur, puan_liste, strateji_liste, oyuncu_list, oyuncu_total_puan, tur):
#Kazanan oyuncu kısmı                
    #print("Kazanan oyuncu: ", oyuncu_list[sayac])
    #print("Kazanan oyuncunun izlediği strateji: ", strateji_liste[sayac])  
    #print("Oyuncunun kazandığı puan: ", oyuncu_total_puan[sayac])
    kazanan_strateji.append(strateji_liste[sayac])
    


#Fonksiyonları çağırma kısmı
 n += 1
 OyuncuEkleme(oyuncu_sayac,oyuncu_list)
#print(kazanan_strateji)
n = 1000



#Histograma çevirme kısmı

strateji_sayı.append(kazanan_strateji.count(1))
strateji_sayı.append(kazanan_strateji.count(2))
strateji_sayı.append(kazanan_strateji.count(3))

plt.bar([1,2,3],strateji_sayı)
plt.show()







