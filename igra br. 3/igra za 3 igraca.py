import random
print("Unesi br. od 1 do 100.")
co=int(input())
print("Unesi br. od 1 do 100.")
cro=int(input())
komp=random.randint(1, 100)
print(komp)
r1=komp-co
r2=komp-cro
if co==cro:
    print("Jednako")
elif abs(komp-co)>abs(komp-cro):
    print("Blizi je player2")
else:
    print("Blizi je player1")
