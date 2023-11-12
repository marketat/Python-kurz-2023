class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = "True"

    def pujc_auto(self):
        if self.dostupne == "True":
            self.dostupne = "False"
            return f"Potvrzuji zapůjčení."
        else:
            return f"Vozidlo není k dispozici."
    
    def get_info(self):
        return f"Registrační značka vozidla: {self.registracni_znacka}, značka a typ vozidla: {self.typ_vozidla}."
    
    def vrat_auto(self, tachometr, pocet_dni):
        self.najete_km = tachometr
        self.dostupne = "True"
        if pocet_dni <= 7:
            return f"Celková cena za půjčení vozidla je {pocet_dni * 400} Kč."      
        if pocet_dni > 7:
            return f"Celková cena za půjčení vozidla je {pocet_dni * 300} Kč."


Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Skoda = Auto("1P3 4747", "Škoda Octavia", 41253)
    

znacka = ["Peugeot", "Škoda"]
rent = input("Jakou značku si přejete vypůjčit? ")

if rent == znacka[0]:           #if rent == "Peugeot/Škoda"
    print(Peugeot.pujc_auto())
    print(Peugeot.pujc_auto())
    print(Peugeot.vrat_auto(47550, 1))
    print(Peugeot.get_info())
    
else:
    print(Skoda.pujc_auto())
    print(Skoda.pujc_auto())
    print(Skoda.vrat_auto(41300, 2))
    print(Skoda.get_info())
    