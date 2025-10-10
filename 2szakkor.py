gyumolcsok = [] # lista létrehozása
#open - fájl megnyitása az 'r' kapcsolóval, utf-8 kódolással
#as forrasfajl az adatfolyam neve 
# ezzel beolvassa sor onként a fájlt és eltárolja
with open('áruház.csv' , 'r' , encoding='utf-8') as forrasfajl:
    for sor in forrasfajl: # ez és a következő 3 sor csak egyszer fut le , ezután pontosan annyiszor fog ujra lfutni amennyi sor van
        adatok = sor.strip().split(',') # vessző mentén darbokra szedi a sort , a strip parancs szoveges függvény = eltunteti előlről és hátulról a felesleges szóközöket , a split szööveges függvény = a megadott karakter mentén darbaol 
        termék = {'termeknev' : adatok[0], 'egysegar' : int(adatok[1]), 'raktarkeszlet' : int(adatok[2]), 'kategoria' : adatok[3]}
        gyumolcsok.append(termék) #kulcs érték hozzáadása a listához


print(f"{gyumolcsok=} \n")
print(f"{gyumolcsok[:5]}")

