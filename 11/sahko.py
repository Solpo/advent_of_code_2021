def naapurit (annettu_x: int, annettu_y: int, leveys: int, korkeus: int) -> set:
    palautettava = {(x, y) for x in range(annettu_x-1, annettu_x+2) if x >= 0 and x < leveys \
        for y in range(annettu_y-1, annettu_y+2) if y >= 0 and y < korkeus}
    palautettava.remove((annettu_x, annettu_y))
    return palautettava

def kasvata_kaikkia(ruudukko: list) -> list:
    for y in range(len(ruudukko)):
        for x in range(len(ruudukko[y])):
            ruudukko[y][x] += 1
    return ruudukko

def nollaa_valahtaneet(ruudukko: list) -> list:
    for y in range(len(ruudukko)):
        for x in range(len(ruudukko[y])):
            if ruudukko[y][x] > 9:
                ruudukko[y][x] = 0
    return ruudukko