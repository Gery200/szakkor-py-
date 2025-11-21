játékok = []
with open('./adatok/games.csv' , 'r' , encoding='utf-8') as adatfolyam:
    for sor in adatfolyam: 
        adatok = sor.strip().split(',')
        játék = {'id' : int(adatok[0]), 'nev' : (adatok[1]), 'fejleszto' : (adatok[2]), 'megjelenes eve' : int(adatok[3]), 'mufaj' : (adatok[4]), 'eladott peldanyszam' : (adatok[5]), 'osszbevetel' : int(adatok[6])}
        játékok.append(játék) 


#print(f"{játékok=} ")

print(f"{játékok[10:20]}")


for játék in játékok:
    print(f"játék neve: {játék['nev']}")
    print(f" \t Fejlesztő: {játék['fejleszto']}")

#print(f"{játékok['nev'][0]}")

#for játék in játékok:
 #   if játék['id'] == 34:
       # print(f"{játék['nev']}")

for játék in játékok:
    if játék['megjelenes eve'] == 2015:
        print(F"{játék['nev']}")
