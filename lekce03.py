import json

with open ("pizza.json", mode="r", encoding="utf-8") as soubor:
      pizzy = json.load(soubor)
    
print(pizzy)
print(pizzy["ingredience"][-1])
print(pizzy["ingredience"][3])


# při vytváření nového json v základu python neumí diakritiku, proto se musí přidat "ensure_ascii=False"? pokud do dat připíšu další položku, mod write přepíše původní soubor
data = {
      "1. místo": "Olga",
      "2. místo": "Zanet",
      "3. místo": "Andy"
}

with open("vyherci.json", mode="w", encoding="utf-8") as soubor:
      json.dump(data, soubor, ensure_ascii=False)

with open("vyherci.json", mode="r", encoding="utf-8") as soubor:
      vyherci = json.load(soubor)

print(vyherci)
