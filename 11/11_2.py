import sahko

with open("input.txt") as f:
    mustekalat = []
    for rivi in f:
        rivin_mustekalat = [int(mustekala) for mustekala in rivi.rstrip()]
        mustekalat.append(rivin_mustekalat)

print(mustekalat)
korkeus = len(mustekalat)
leveys = len(mustekalat[0])

kierroksia = 0
kaikkiaan_valahtaneita = 0
while True:
    valahtaneet = set()
    valautettavat = set()
    mustekalat = sahko.kasvata_kaikkia(mustekalat)
    while True:
        for y in range(len(mustekalat)):
            for x in range(len(mustekalat[y])):
                if mustekalat[y][x] > 9 and (x, y) not in valahtaneet:
                    valautettavat.add((x, y))
        if valautettavat == set():
            kaikkiaan_valahtaneita += len(valahtaneet)
            mustekalat = sahko.nollaa_valahtaneet(mustekalat)
            break
        for (x, y) in valautettavat:
            for naapurin_x, naapurin_y in sahko.naapurit(x, y, leveys, korkeus):
                mustekalat[naapurin_y][naapurin_x] += 1
            valahtaneet.add((x, y))
        valautettavat = set()

    print(f"kierroksella {kierroksia + 1} välähti {len(valahtaneet)} kalaa.\nKaikkiaan välähtäneitä kaloja on {kaikkiaan_valahtaneita}")
    if len(valahtaneet) == 100:
        print(f"Kaikki 100 kalaa välähtivät ensimmäistä kertaa kierroksella {kierroksia + 1}")
        break
    kierroksia += 1
