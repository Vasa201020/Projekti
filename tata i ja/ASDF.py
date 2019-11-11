'''
ime="Vasa"
ime2="Mita"
ime3="Mama"
ime4="Tata"
irko=[ime,ime2,ime3,ime4]
for f in irko:
    print(f)
'''

'''Dat je niz elemenata saberi svaki sa svkim i odstampaj rezultat'''
'''
niz=[1,2,3,4,5,6,7,8,9]
vicko=0
for v in niz:
    vicko=vicko+v
print(vicko)
'''

'''Date su promenljive, staviti ih u niz, potom izvesti osnovne racunske operacije sa svakim elementom u nizu,
potom rezultate dodate u novi niz koristeci append() funkciju, i u foreach petlji ispisati oba niza'''
'''
i=1
k=2
s=3
r=4
t=5
faci=[i,k,s,r,t]
vic=0
vuc=0
tuc=1
ruc=1
niz=[]
for v in faci:
    vic=vic+v
for c in faci:
    vuc=vuc-c
for d in faci:
    tuc=tuc*d
for z in faci:
    ruc=ruc/z
    
niz.append(vic)
niz.append(vuc)
niz.append(tuc)
niz.append(ruc)
for rj in niz:
    print(rj)
for tj in faci:
    print(tj)
'''

'''Dat je niz marki automobila. Prodji kroz niz i ako u nizu imas markku Honda, ispisi 1, u suprotnom, ispisi 0'''
'''
niz=["BMWV", "HONDA", "AUDI", "MERCEDES", "VOLVO"]
for n in niz:
    if n=="HONDA":
        print(1)
    else:
        print(0)
'''

'''Dat je niz brojeva. Ako je neki broj veci od 10 a manji od 50, napisi bravo, u suprotnom napisi Kakav je ovo niz?'''
brojevi=[1, 14, 45, 122, -1, 0, 18]
for g in brojevi:
    if g>10 and g<50:
      print("Bravo")
    else:
        print("Kakav je to niz?")























































    
