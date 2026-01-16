with open('forrae.txt' , "r" , encoding='utf-8') as fajl:
    szoveg = fajl.read()


#1 megoldas
#szoveg = szoveg.replace("," , " ")
#szoveg = szoveg.replace("." , " ")

#2 megoldas

elvalasztok = ["," , "?" , "!" , "." , "-"]

for jel in elvalasztok:
    szoveg = szoveg.replace(jel, " ")


szoveg = szoveg.lower()
# szavak listába tétele szóközök alapján
szavak = szoveg.split()

# csak kisbetu
szoveg = szoveg.lower()

# ell 1 
print(f"Szavak száma: {len(szavak)}")

# ell2
tisztott = []

for szo in szavak:
    if szo != "":
        tisztott.append(szo)

szavak = tisztott

'''
for x in tisztott:
    print(x)
'''

alista = []

for x in tisztott:
    if x[0] == "a":
        alista.append(x)

alista.sort()

print(f"\nAz a betus szavak listája:{alista}")
print(f" \nEnnyi a betus szo van : {len(alista)}")


with open('kimenet6.txt' , 'a' , encoding='utf8') as forras:
    print(f"Az a betus szavak: {alista}" , file=forras)


tisztott.count('török')

torok = []
for x in tisztott:
    if 'török' == x :
        torok.append(x)


print(f"A török szó ennyiszer szerepel:{len(torok)}")     

abc = []

for x in tisztott:
    if x[0] == "a" or x[0] == "b" or x[0] == "d":
        abc.append(x)



print(f"Ennyi a , b  vagy cvel kezodo szo van: {len(abc)}")



with open('abckimenet.txt' , 'a' , encoding='utf-8') as abcd :
    print(f"Az abc betus szavak: {abc}" , file=abcd)