def luo(leveys: int, korkeus: int) -> list:
    palautettava = []
    for _ in range(korkeus + 1):
        palautettava.append([0] * (leveys + 1))
    return palautettava

def lisaa_putki(matriisi: list, vektori: list) -> list:
    # vaakarivi
    if vektori[0] == vektori[2]:
        for i in range(min((vektori[1], vektori[3])), max(vektori[1], vektori[3]) + 1):
            matriisi[i][vektori[0]] += 1
    
    # pystyrivi
    elif vektori[1] == vektori[3]:
        for i in range(min((vektori[0], vektori[2])), max(vektori[0], vektori[2]) + 1):
            matriisi[vektori[1]][i] += 1
    
    # laskeva viistorivi (y kasvaa)
    elif vektori[2] - vektori[0] == vektori[3] - vektori[1]:
        for i in range(vektori[2] - vektori[0] + 1):
            matriisi[vektori[1]+i][vektori[0]+i] += 1
    
    # nouseva viistorivi (y pienenee)
    elif vektori[2] - vektori[0] == vektori[1] - vektori[3]:
        for i in range(vektori[2] - vektori[0] + 1):
            matriisi[vektori[1]-i][vektori[0]+i] += 1
    
    else:
        print("Mitäs")
        return

    return matriisi

def risteyksia(matriisi: list) -> int:
    palautettava = 0
    for vaakarivi in matriisi:
        for piste in vaakarivi:
            if piste >= 2:
                palautettava += 1
    return palautettava

def tulosta(matriisi: list):
    for vaakarivi in matriisi:
        for piste in vaakarivi:
            print(piste, end="")
        print()