knihy = {
    "Nazev": "Ananas na pizu patří",
    "Cena": 0,
    "Skladem": True,
}

print(knihy)
print(knihy.keys())
print(knihy.values())
print(knihy["Nazev"])
print(f"Kniha {knihy['Nazev']}, cena: {knihy['Cena']}, skladem: {knihy['Skladem']}")

knihy["Cena"] = 100

print(f"Kniha {knihy['Nazev']}, cena: {knihy['Cena']}, skladem: {knihy['Skladem']}")


knihy["Autor"] = "Michal Kucera"
print(f"Kniha {knihy['Nazev']}, cena: {knihy['Cena']}, skladem: {knihy['Skladem']}, autor: {knihy['Autor']}")


if "Autor" in knihy:
    print(f"Kniha {knihy['Nazev']}, cena: {knihy['Cena']}, skladem: {knihy['Skladem']}, autor: {knihy['Autor']}")
else:
    print(f"Kniha {knihy['Nazev']}, cena: {knihy['Cena']}, skladem: {knihy['Skladem']}")
