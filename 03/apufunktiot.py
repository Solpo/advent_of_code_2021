def enemman(vertailtava: dict) -> int:
    suurin = (0, 0)
    for avain in vertailtava.keys():
        if vertailtava[avain] > suurin[1]:
            suurin = (avain, vertailtava[avain])
    return suurin[0]

def binaaristr_intiksi(yxnol: str) -> int:
    palautettava = 0
    for i in range(len(yxnol)):
        palautettava += (2 ** i) * int(yxnol[(-1 - i)])
    return palautettava

def kaanna_binaaristr(yxnol: str) -> str:
    palautettava = ""
    for i in range(len(yxnol)):
        if yxnol[i] == "0":
            palautettava += "1"
        elif yxnol[i] == "1":
            palautettava += "0"
        else:
            print
            raise ValueError("Tuli vastaan muu kuin 1 tai 0")
    return palautettava

def kumpaa_enemman_kohdassa(lista: list, kohta: int) -> int:
    ykkosia = 0
    nollia = 0
    for luku in lista:
        if luku[kohta] == "1":
            ykkosia += 1
        elif luku[kohta] == "0":
            nollia += 1
        else:
            raise ValueError("Nyt tuli jotain muuta kuin ykkönen tai nolla")
    if ykkosia > nollia:
        return 1
    elif nollia > ykkosia:
        return 0
    else:
        return 2