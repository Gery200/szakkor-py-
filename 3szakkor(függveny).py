import random
szamlista = []
kerekített = []

for x in range(200):
    szamlista.append(random.random())

for x in szamlista:
    kerekített.append(round(x , 0 ))
    print(f"{kerekített}")

#####################################################################

db = 0 
for i in range(len (kerekített) -2):
    if kerekített[i] == 1 and kerekített[i+1] == 1 and kerekített[i+2]==1:
        db +=1

print(f"A 111 szamsofr ennyiszer szerepel a listaban {db}")


################################################################xx

szamlista2 = []

for x in range(1000):
    szamlista2.append(random.randint(1,10))

print(f"{szamlista2}")

cd = 0 
for i in range(len(szamlista2) -2):
    if szamlista2[i] == 1 and szamlista2[i + 1] == 2 and szamlista2[i + 2] == 1:
        cd +=1


print(f"ennyiszer van a szovegben 721 {cd}")

#####################################

szamlista3 = []

for x in range(2000):
    szamlista3.append(random.randint(0 , 500))

dd = 0 

for i in range(len(szamlista3) -2):
    if szamlista3[i] == 4 and szamlista3[i + 1 ] == 2 and szamlista3 [i + 2] == 7:
        dd +=1

print(f"ennyiszer szerepel 427 szamsor {dd} ")

####################################################################

szöveglista = []

for x in range(2500):
    sorsolt = random.randint(0, 1)
    if sorsolt == 0 :
        szöveglista.append("a")
    else:
        szöveglista.append("b")

print(f"{szöveglista}")

bb = 0 

for i in range(len(szöveglista) -2):
    if szöveglista[i] == "a" and szöveglista[i + 1] == "b" and szöveglista[i + 2] == "b" and szöveglista[i + 3] == "a":
        bb += 1


print(f"Az abba ennyiszer szerepel: {bb}")