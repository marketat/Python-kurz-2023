def get_number ():
    number = (input("Zadej své telefonní číslo: "))
    if len(number) == 9:
        print("True")
    elif len(number) == 13:
        predvolba = '+420'
        predvolba_number = number[:4]
        if predvolba_number == predvolba:
            print("True")
    else:
        print("False")
    

def text_price ():
        text = input("Napiš svou zprávu: ")
        if len(text) < 180:
            price = 3
        elif len(text) >= 180:
            price = (len(text) // 180) * 3
        print(f"Tvá zpráva stojí {price} Kč.")

get_number()
text_price()

