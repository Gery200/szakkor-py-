class auto:
    def __init__(self , markanev , modell , gyartasi_ev):
        self.markanev = markanev
        self.modell = modell
        self.gyartasi_ev = gyartasi_ev
        self.sebesseg = 0
        self.motor_bekapcsolva = False
        self.uzemanyag_szint = 50.0
        self.kilometer_ora = 0


    def kiir_auto_adatok(self):
        return(f"Márka: {self.markanev} , Modell: {self.modell} , gyártási_év: {self.gyartasi_ev} , Sebesség: {self.sebesseg} km/h , Motor állapot: {'bekapcsolva' if self.motor_bekapcsolva else 'kikapcsolva'}"
        f"Üzemanyag szint: {self.uzemanyag_szint} liter , kilóméter óra állása: {self.kilometer_ora}")
    
    def motor_indit(self):
        if not self.motor_bekapcsolva and self.uzemanyag_szint > 0:
            self.motor_bekapcsolva = True
            return "A motor beindult"
        elif self.uzemanyag_szint <= 0:
            return "ninicsen elég üzemanyag a tankban"
        return "A motor már be van indítva"
    
    def motorleall (self):
        if self.motor_bekapcsolva:
            self.motor_bekapcsolva = False
            self.sebesseg = 0
            return " a mototr leállít"
        return "A motor be cvan indítva"
    
    def gyorsit (self , novekedes):
        if self.motor_bekapcsolva:
            self.sebesseg += novekedes
            return f"Gyorsítás: autó sebessége most {self.sebesseg} km/h"
        return " Nem lehet gyorsítani , mert a motor le van állítva"

    def fekez (self , csokkenes) :
        if self.motor_bekapcsolva and self.sebesseg > 0 :
            self.sebesseg = max(0 , self.sebesseg - csokkenes)
            return f"Fékezés: az autó sebessége most : {self.sebesseg} km/h"
        return f"Nem lehet fékezni vagy az autó áll"       
    
    def tankol (self , mennyiseg):
        self.uzemanyag_szint += mennyiseg
        return f"{mennyiseg} liter üzemanyag van hozzáadva . uzemanyag szint : {self.uzemanyag_szint}"
    

    def fogyaszt (self , kilometer):
        fogyasztas = kilometer * 0.1
        self.uzemanyag_szint -= fogyasztas
        if self.uzemanyag_szint <  0 :   
            self.uzemanyag_szint =  0
            self.kilometer_ora += kilometer
        uzenet = f"Megtett távolság: {kilometer} km , fogyasztott üzemanyag: {fogyasztas} liter"
        if self.uzemanyag_szint == 0 :
            uzenet += "elfogyott az üzemanyag"
            self.motorleall()     
        return uzenet   