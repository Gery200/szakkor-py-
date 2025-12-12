try:
        with open('./adatok/kimenet3.txt' , 'r' , encoding='utf-8') as adatfolyam:
            tartalom = adatfolyam.read()

        szöveglista = list(map(float, tartalom.strip().split(";")))


        paros = []
        paratlan = []

        for x in szöveglista:
            if x % 2 == 0 : 
                paros.append(x)
        else:
                paratlan.append(x)



        with open('paros.txt' , 'w' , encoding='utf-8') as adatfolyam:
            print(f" {paros}" , file=adatfolyam)

        with open('paratlan.txt' , 'w' , encoding='utf-8') as adatfolyam:
            print(f" {paratlan}" , file=adatfolyam)
except FileNotFoundError:
    print(f"nem találhato fájl")

except ValueError:
     print(f"érték hiba")

finally:
     print(f"a txt-k létrehozva a program vége")

