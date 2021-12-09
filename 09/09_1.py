import merenpohja

with open("input.txt") as f:
    pohja = []
    for rivi in f:
        pohja.append([int(kirjain) for kirjain in rivi.rstrip()])
leveys = len(pohja[0])
korkeus = len(pohja)

riskipisteita = 0
for y in range(korkeus):
    for x in range(leveys):
        if merenpohja.matala_paikka(pohja, x, y):
            riskipisteita += pohja[y][x] + 1
print(f"Riskipisteitä: {riskipisteita}")

