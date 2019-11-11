import random
br=0
while br<3:
        lista=["1","2","3","4","5","6","7","8","9"]
        komip=random.choice(lista)
        print(komip)
        komp=random.choice(lista)
        print(komp)
        print(int(komp)+int(komip))
        puc=(int(komp)+int(komip))
        if puc>10:
                print("POBEDA RACUNARA")
        else:
            print("POBEDA COVEKA")
        print("--------------------")
        br+=1
