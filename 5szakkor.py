try:
    x = int(input("Adj meg egy számot"))
    print(f"A szám duplája" , x * 2)
except ValueError:
    print(f"hibás! száot kell megadni !")


#2

try:
    lista = [1,2,3,]
    print(lista[5])
    print(10/2)
except (IndexError, ZeroDivisionError) as hiba:
    print(f"Hiba történt" ,  hiba)

#3

try:
    a = int("abc")
except ValueError:
    print(f"Nem alakítható számmá !")
except TypeError:
    print(f"típushiba történt !")

#4 
try:
    file = open('adat.txt' , 'r')
    tartalom = file.read()
    print(tartalom)
except FileNotFoundError:
    print(f"A fájl nem található")
finally:
    print(f"program vége")

#5 

def ellenoriz_kor(kor):
    if kor < 0:
        raise ValueError("A kör nem lehet negatív !")
    return False


try:
    ellenoriz_kor(-5) 
except ValueError as h:
    print(f"hiba" , h)

#6 

try:
    with open('adatok.csv' , 'r' , encoding='utf-8') as f:
        for sor in f:
            print(sor.strip())
except FileNotFoundError:
    print(f"")