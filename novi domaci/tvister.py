import random
br=0
while br<10:
    boja=["Crvena ","Zelena ","Plava ","Žuta "]
    udovi=["ruka ","noga "]
    strana=["levo ","desno "]
    tvist=random.choice(boja)
    trust=random.choice(udovi)
    eri=random.choice(strana)
    print(tvist+trust+eri)
    print()
    br+=1
