import merenpohja, math

with open("input.txt") as f:
    pohja = []
    for rivi in f:
        pohja.append([int(kirjain) for kirjain in rivi.rstrip()])
leveys = len(pohja[0])
korkeus = len(pohja)

altaat = []
kaytetyt = set()
for y in range(korkeus):
    for x in range(leveys):
        if (x, y) not in kaytetyt:
            if pohja[y][x] == 9:
                kaytetyt = set.union(kaytetyt, (x, y))
                continue
            uudet = merenpohja.allas(pohja, x, y)
            if uudet != set():
                altaat.append(uudet)
            kaytetyt = set.union(kaytetyt, set({koordinaatit for allas in altaat for koordinaatit in allas}), (x, y))


# print(kaytetyt)
# print(len(kaytetyt))

altaiden_koot = sorted([len(allas) for allas in altaat], reverse=True)
print(f"Altaiden koot = {altaiden_koot}")
print(f"Kolme suurinta allasta = {sorted([allas for allas in altaat], reverse=True)}")
print(f"Kolmen suurimman altaan koot: {sorted([len(allas) for allas in altaat], reverse=True)[0:3]}")
print(f"Kolmen suurimman altaan kokojen tulo: {math.prod(altaiden_koot[0:3])}")