sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

soucastka = input("Vlož kód součástky: ")

if soucastka not in sklad:
    print("Součástka není skladem.")

elif soucastka in sklad:
    mnozstvi = int(input("Požadovaný počet kusů: "))

    if mnozstvi > sklad[soucastka]:
        hodnota = sklad[soucastka]
        print(f"Lze prodat pouze {hodnota}.")
        sklad.pop(soucastka)
    else:
        print(f"Poptávku lze uspokojit v plné výši.")
        sklad[soucastka] = sklad[soucastka] - mnozstvi
    