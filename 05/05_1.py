from abc import abstractproperty
import matriisi

with open("input.txt") as f:
    koordinaatit = []
    for rivi in f:
        koordinaatit.append([int(luku) for luku in rivi.rstrip().replace(" -> ", ",").split(",")])

oikaistut_koordinaatit = []
for vektori in koordinaatit:
    if vektori[2] < vektori[0]:
        oikaistut_koordinaatit.append([vektori[2], vektori[3], vektori[0], vektori[1]])
    else:
        oikaistut_koordinaatit.append(vektori)
koordinaatit = oikaistut_koordinaatit

# print(koordinaatit)

leveys = max([x for koordinaatti in koordinaatit for x in [koordinaatti[0], koordinaatti[2]]])
syvyys = max([y for koordinaatti in koordinaatit for y in [koordinaatti[1], koordinaatti[3]]])

meri = matriisi.luo(leveys, syvyys)

for vektori in koordinaatit:
    meri = matriisi.lisaa_putki(meri, vektori)

print(matriisi.risteyksia(meri), end="\n\n")

# matriisi.tulosta(meri)