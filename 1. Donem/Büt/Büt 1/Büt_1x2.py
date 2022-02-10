import random

oyunsayisi = 0
ks = []
ss = []

while oyunsayisi < 1000:
 op = 0
 op1 = []
 pl = []
 ot = 0
 oyun = 1

 #100 gamer datas
 os = 0
 ol = []
 for i in range(100):
    os += 1
    ol.append(os)

 op1 = []
 for i in range(100):
    op1.append(0)

 sl = []
 for i in range(100):
    strateji = random.randint(1,3)
    sl.append(strateji)
    
    
 #Game
 x = 0
 while oyun == 1:
    geçiş = 1
    op = 0
    while geçiş == 1:
        zar = random.randint(1,6)
        if zar != 1:
            ot += zar
            if sl[x] == 1:
                if ot < 20:
                    geçiş = 1
                else:
                    op += ot
                    op1[x] += op
                    pl.append(op1)
                    geçiş = 0

                    if int(op1[x]) < 100:
                        oyun = 1
                    else:
                        oyun = 0
        if sl[x] == 2:
            if ot < 30:
                geçiş = 1
            else:
                op += ot
                op1[x] += op
                pl.append(op1)
                geçiş = 0

                if int(op1[x]) < 100:
                    oyun = 1
                else:
                    oyun = 0
                    
        if sl[x] == 3:
            if ot < 40:
                geçiş = 1
            else:
                op += ot
                op1[x] += op
                pl.append(op1)
                geçiş = 0

                if int(op1[x]) < 100:
                    oyun = 1
                else:
                    oyun = 0     
                    
                    
        else:
            ot = 0
            op += ot
            geçiş = 0
            
    if x < 99:
        x += 1
    else:
        x = 0                     
                            
    
 #print("Winnger ", ol[x-1])
 #print("Strategy ", sl[x-1])  
 #print("Point ", op1[x-1])
 #print(op1)

 oyunsayisi += 1
 print(oyunsayisi)
 ks.append(sl[x-1])
ss.append(ks.count(1))
ss.append(ks.count(2))
ss.append(ks.count(3))

plt.bar([1,2,3],ss)
plt.show()    
   
    
    
