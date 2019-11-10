
import random
pobede=0
pobede_komp=0
ne=0
br=0
while br<3:
    print("igraj papir-kamen-makaze.")
    pkm=str(input())
    print (pkm.upper())
    pkmm=["papir","kamen","makaze"]
    komp=random.choice(pkmm)
    print(komp)
    if pkm==komp:
        print("Izjednaceno.")
        ne+=1
    elif pkm=="kamen" and komp=="makaze":
        print("pobedio si.")
        pobede+=1
    elif pkm=="papir" and komp=="kamen":
        print("Pobedio si.")
        pobede+=1
    elif pkm=="makaze" and komp=="papir":
        print("Pobedio si.")
        pobede+=1
    else:
        print("Izgubio si.")
        pobede_komp+=1
        ne+1
    print()
    print("nereseno "+str(ne))
    print()
    print("Pobedio si ."+str(pobede))
    print()
    print("Izgubio si ."+str(pobede_komp))
    br+=1
    print()
    print("Super hajde opet.")
    print("--------------")
    
