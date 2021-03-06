with open("input.txt") as f:
    asemat = [int(asema) for asema in f.readline().split(",")]
print(asemat)

pienin_bensankulutus = (-1, -1)
for i in range(min(asemat), max(asemat) + 1):
    bensankulutus = 0
    for rapu in asemat:
        bensankulutus += abs(rapu - i)
    print(f"Asemaan {i} siirtymällä kuluu bensaa yhteensä {bensankulutus} yksikköä")
    if bensankulutus < pienin_bensankulutus[1] or pienin_bensankulutus == (-1, -1):
        pienin_bensankulutus = (i, bensankulutus)
print(pienin_bensankulutus)
print(f"Pienimmällä bensankulutuksella {pienin_bensankulutus[1]} selvitään kun ravut siirtyvät asemaan {pienin_bensankulutus[0]}")

