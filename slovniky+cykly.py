seznam = [100, 200, 300, 400]
soucet = 0

for polozka in seznam: #polozka vzniká s cyklem, i když není definovaná
    soucet += polozka #soucet = soucet + polozka (prochází cyklus a vždy přičte další položku ze seznamu)

print(soucet)


sales = { 
    "Zkus mě chytit": 4165,       #název knihy a počet prodaných kusů
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

for klic in sales:
    print(sales[klic]) #vypíše hodnotu na konkrétnm klíči

for klic, hodnota in sales.items():   #i když klic a hodnota nejsou definované, python si automaticky odvodí, že klíč je první položka a hodnota je ta druhá. Fce itmes zajistí, že dostanu obě dvě
    print(f"nazev: {klic}, pocet prodaných kusů: {hodnota}")

for value in sales.values(): #vypíšou se jenom hodnoty
    print(value)


#dvourozměrné tabulky

hodnoceni = ["Kniha 1", 4, "Kniha 2", 5, "Kniha 3", 3]
hodnoceni1 = [["Kniha 1", 4], ["Kniha 2", 5], ["Kniha 3", 3]] # totožný zázpis, ale přehlednější (lepší by bylo udělat z toho slovník)

print(hodnoceni1[0][1]) #vypíše hodnocení u Knihy 1
print(hodnoceni1[0][0]) #vypíše slovo Kniha 1
print(hodnoceni1[0][0][0]) #vypíše první písmeno slova Kniha 1

for polozka in hodnoceni1:
    print(polozka[0] + " " + str(polozka[1]))


books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

print(books[2])
print(books[0])
print(books[1]["title"]) #vybírá 2 pozici ze slovníku a vypíšu klíč
