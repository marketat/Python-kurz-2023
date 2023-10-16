Vysvedceni = {
    "cesky jazyk": 2,
    "matematika": 1,
    "dejepis": 1
}

print(Vysvedceni)
print(f"Na vysvědčení bylo {Vysvedceni}")


sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc která mě zabila"] = "0"
sales["Vrah zavolá v deset"] = sales["Vrah zavolá v deset" ] + 100
print(sales)


tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
listek = int(input("Napiš své číslo lístku: "))

if listek in tombola:
    print(f"Vyhráváte: {tombola[listek]}")
else:
    print("Bohužel nevyhráváš nic.")


passwords = {
    "Jiří": "tajne-heslo", 
    "Natálie": "jeste-tajnejsi-heslo", 
    "Klára": "nejtajnejsi-heslo"
}

jmeno = input("Napiš své jméno: ")

if jmeno in passwords:
    heslo = input("Napiš své heslo: ")
    if heslo in passwords:
        print("Smíš vstoupit")
    else:
        print("Přístup odepřen")