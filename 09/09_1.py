with open("testi.txt") as f:
    pohja = []
    for rivi in f:
        pohja.append([kirjain for kirjain in rivi.rstrip()])
        print(pohja)
leveys = len(pohja[0])
korkeus = len(pohja)

def naapurit(ruudukko: list, leveys: int, korkeus: int) -> list:
    palautettava = []
    for y in range(korkeus):
        for x in range(leveys):
            if y != 0:
                palautettava.append(ruudukko[y-1][x])
            if y != korkeus - 1:
                palautettava.append(ruudukko[y+1][x])
