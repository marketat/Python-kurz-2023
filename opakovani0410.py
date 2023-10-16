
## Načti od uživatele matematický operátor a 2 čísla a vypiš výsledek výpočtu. Program bude podporovat operátory +, -, / a *.
cislo_1 = int(input("zadejte cislo:"))
cislo_2 = int(input("zadejte druhe cislo:"))
znaminko = input("zadejte pozadovane znaminko:")

if znaminko == "+"
    print(cislo_1 + cislo_2)

if znaminko == "-"
    print(cislo_1 - cislo_2)

if znaminko == "*"
    print(cislo_1 * cislo_2)

if znaminko == "/"
    print(cislo_1 / cislo_2)

## ukol 2: Proměnná medal_table tentokrát obsahuje zisky jednotlivých druhů medailí států na olympiádě 2020

medal_table = {
    "Cuba": { "gold": 7, "silver": 3, "bronze": 5 },
    "Spain": { "gold": 3, "silver": 8, "bronze": 6 },
    "Uganda": { "gold": 2, "silver": 1, "bronze": 1 },
    "Bahamas": { "gold": 2, "silver": 0, "bronze": 0 },
    "Ukraine": { "gold": 1, "silver": 6, "bronze": 12 },
    "San Marino": { "gold": 0, "silver": 1, "bronze": 2 },
}

top_stat = ""
bronze = 0
for stat, medaile in medal_table.items():
    if medaile['bronze'] > bronze:
        bronze = medaile['bronze']
        top_stat = stat
print(stat)

## ukol 3: V seznamu people máme seznam lidí s jejich daty narození. Vypište jména lidí, kteří se narodili v sudý rok.

people = [
    ["Jeong-Hui Mun", "09/12/1984"],
    ["Cezário Torres", "31/08/1993"],
    ["Josefina Löwe", "03/11/1982"],
    ["Gavrilo Milojević", "28/03/2002"],
    ["Liidia Tamm", "10/07/1963"],
    ["Matxin Zubizarreta", "19/02/1956"],
    ["Mykhail Klymenko", "01/10/1988"],
    ["Bibek Joshi", "05/03/2007"],
    ["Jan Vlk", "26/09/1995"],
    ["Xuân Hoàng", "29/08/1974"]
]

for birth in people:
    x = int(birth[-1][-1])
    if x % == 0
print(x)


## bonusový úkol recept:
recept: {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}
for polozka in recept['ingredience']:
print(polozka[2].split()[0])
        

