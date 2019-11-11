'''
import random
print("Izaberite par ili nepar.")
par=str(input())
print("Unesite br. od 1 do 10.")
br=int(input())
komp=random.randint(1, 10)
zb=br+komp
print(komp)
if zb%2==0 and par=="par":
    print("Pobedio si.")
else:
    print("Izgubio si.")
'''''''binarna pretraga'''''
import random
zam=random.randint(1, 100)
br=0
while br<7:
    print("Unesite br.")
    covek=int(input())
    if zam==covek:
        print("Tacno")
        break
    elif zam<covek:
        print("Manje")
    else:
        print("Vece")
    br+=1
    print("Preostalo pokusaja "+str(7-br))
    
if br==7:
    print("Nemas vise pokusaja.")
    print("Zamislio sam "+str(zam))
else:
    print("Pogodio si u "+str(br+1)+" pokusaju")
