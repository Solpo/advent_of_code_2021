def naapurit(ruudukko: list, x: int, y: int) -> set:
    palautettava = []
    korkeus = len(ruudukko)
    leveys = len(ruudukko[0])
    if y > 0:
        palautettava.append((x, y - 1))
    if y < korkeus - 1:
        palautettava.append((x, y + 1))
    if x > 0:
        palautettava.append((x - 1, y))
    if x < leveys - 1:
        palautettava.append((x + 1, y))
    return set(palautettava)

def naapurien_korkeudet(ruudukko: list, x: int, y: int) -> int:
    palautettava = 0
    for koordinaatit in naapurit(ruudukko, x, y):
        palautettava += ruudukko[koordinaatit[1]][koordinaatit[0]]
    return sum(palautettava)

def matala_paikka(ruudukko: list, oma_x: int, oma_y: int) -> bool:
    oma_korkeus = ruudukko[oma_y][oma_x]
    for koordinaatit in naapurit(ruudukko, oma_x, oma_y):
        if oma_korkeus >= ruudukko[koordinaatit[1]][koordinaatit[0]]:
            return False
    return True

def allas(ruudukko: list, oma_x: int, oma_y: int, tahanastinen: set =set()) -> set:
    if tahanastinen == set():
        tahanastinen = {(oma_x, oma_y)}
    if ruudukko[oma_y][oma_x] == 9:
        return set()
    for naapurin_koordinaatit in naapurit(ruudukko, oma_x, oma_y):
        if (naapurin_koordinaatit[0], naapurin_koordinaatit[1]) not in tahanastinen and ruudukko[naapurin_koordinaatit[1]][naapurin_koordinaatit[0]] != 9:
            tahanastinen = set.union(tahanastinen, {(naapurin_koordinaatit[0], naapurin_koordinaatit[1])})
            tahanastinen = set.union(tahanastinen, allas(ruudukko, naapurin_koordinaatit[0], naapurin_koordinaatit[1], tahanastinen))
    return tahanastinen