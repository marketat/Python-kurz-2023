"""
Pomocí nástroje regex101 vymysli regulární výraz, který označí platná data a neoznačí neplatná data:
platná data:
2.2.2022
13. 8. 1999
4/5/2001

import re

regularni_vyraz = re.compile(r"((\d|\d\d)(\.|\/) ?){2}\d{4}")


neplatná data:
5.123.458.91
21.4
8./9

regularni_vyraz = re.compile(r"(\d{1,2}\./?\d{1,3}(\.\d{3}\.\d\d)?")
                             

Zkopíruj si obsah souboru posta.txt do regex101 jako testovací řetězec. Vymysli regulární výraz, který označí všechny 
"poslední řádky adresy" v textu. Poslední řádka adresy zpravidla obsahuje PSČ a název obce, například 190 16 PRAHA 916 
nebo 742 45 FULNEK. Celkem by jich mělo být 18.

regularni_vyraz = re.compile(r"(\d{3} \d\d  ?[\w]* ?([\w]* )?([\w]*)?")

"""
#bonus


import re

# uživatelské jméno smí obsahovat malá a velká písmena (nesmí obsahovat žádné jiné znaky), 
# jeho minimálná délka je 6 znaků a jeho maximální délka je 10 znaků.

regularni_vyraz = re.compile(r"([a-z]|[A-Z]){6,10}")

jmeno = input("Zadej své uživatelské jméno: ")
hledani = regularni_vyraz.fullmatch(jmeno)
if hledani:
    print("Uživatelské jméno je v pořádku!")
else:
    print("Nesprávné uživatelské jméno!")


#heslo smí obsahovat malá a velká písmena, číslice, a následující speciální znaky: _, -, ., +, =. 
# Jeho minimálná délka je 12 znaků a jeho maximální délka je 30 znaků.

regularni_vyraz = re.compile(r"(([a-z]|[A-Z]|[0-9])(\_|\-|\.|\+|\=)?){12,30}")
                             
heslo = input("Zadej své heslo: ")
hledani = regularni_vyraz.fullmatch(heslo)
if hledani:
    print("Heslo je v pořádku!")
else:
    print("Nesprávné heslo!")

# e-mail by měl být validním e-mailem

regularni_vyraz = re.compile(r"(\w+)?(\.|\+|\-)?\"?(\w+)\"?@\[?\w+(\.|\-)\w+\.?(\w+)?\.?(\w+)?\]?")

email = input("Zadej svou e-mailovou adresu: ")
hledani = regularni_vyraz.fullmatch(email)
if hledani:
    print("E-mail je v pořádku!")
else:
    print("Nesprávný e-mail!")





