import random
br=0
while br<10:
    boja=["crveno ","zeleno ","plavo ","žuto "]
    udovi=["ruka ","noga "]
    strana=["Leva ","Desna "]
    tvist=random.choice(boja)
    trust=random.choice(udovi)
    eri=random.choice(strana)
    print(eri+trust+tvist)
    print()
    br+=1
