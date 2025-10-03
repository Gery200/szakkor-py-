a = int(5)
b = str("alma")
c = bool(True)
d = 12

szamlista = [5 , 23, 29 ,56, 78,]
szöveglista = ["alma", "körte" , "szilva", 1 ,5 ,7]

import random
sorsol_szlista = []
gyumolcs_lista = ["alma" , "korte" , "szilva" , "eper", "paradicsom" , "karfiol" , "mango", "dinnye", "áfonya" , "kivi"]
atalakitott = []


for x in range (100):
    sorsol_szlista.append(random.randint(0,9))




for x in sorsol_szlista:
    if x == 0:
        atalakitott.append(gyumolcs_lista[0])
    elif x == 1:
        atalakitott.append(gyumolcs_lista[1])
    elif x == 2:
        atalakitott.append(gyumolcs_lista[2])
    elif x == 3: 
        atalakitott.append(gyumolcs_lista[3])
    elif x == 4: 
        atalakitott.append(gyumolcs_lista[4])
    elif x == 5:
        atalakitott.append(gyumolcs_lista[5])
    elif x == 6:
        atalakitott.append(gyumolcs_lista[6])
    elif x == 7:
        atalakitott.append(gyumolcs_lista[7])
    elif x == 8:
        atalakitott.append(gyumolcs_lista[8])
    elif x == 9:
        atalakitott.append(gyumolcs_lista[9])


print(f"lista elmeinek száma: {len(atalakitott)}")
print(f"{atalakitott}")

if "eper" in atalakitott:
    print("van eper a listaban!")
else: 
    print("nincs eper a listaban")

eperszama = 0
korteszama = 0
szilvasz = 0

for x in atalakitott:
   if x == "eper":
       eperszama += 1

print(f"az eper ennyiszer szerepel a listaban: {eperszama}")
print(f"az eper ennyiszer szerepel a listaban: {korteszama}")
print(f"az eper ennyiszer szerepel a listaban: {szilvasz}")