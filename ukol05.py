teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#průměrné teploty
import statistics

prumer = [statistics.mean(teplota) for teplota in teploty]
print(prumer)

#ranní teploty
ranni_t = [rano[0] for rano in teploty]
print(ranni_t)

#noční teploty
nocni_t = [noc[3] for noc in teploty]
print(nocni_t)

#polední a noční teploty
dve_teploty = [[teplota[1], teplota[3]] for teplota in teploty]
print(dve_teploty)

#bonus 
teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]


prumer = {}
import statistics

prumer = [{(h[0]): (statistics.mean(h[1:4]))} for h in teploty]          

print(prumer)
