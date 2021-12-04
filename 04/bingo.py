def vaakabingo(ruudukko: list, voittonumerot: list):
    for rivi in ruudukko:
        for numero in rivi:
            if numero not in voittonumerot:
                break
        else:
            # print(f"Voittava ruudukko {ruudukko},\nVoittorivi {rivi}")
            # print(f"Tuorein voittonumero on {voittonumerot[-1]}")
            return (ruudukko, voittonumerot)
    else:
        # print(f"Ei vaakarivivoittoa tällä ruudukolla {ruudukko}")
        return False

def pystybingo(ruudukko: list, voittonumerot: list):
    for i in range(5):
        for rivi in ruudukko:
            if rivi[i] not in voittonumerot:
                break
        else:
            # print(f"Voittava ruudukko {ruudukko},\nVoittosarake {i}")
            # print(f"Tuorein voittonumero on {voittonumerot[-1]}")
            return (ruudukko, voittonumerot)
    else:
        # print(f"Ei pystyrivivoittoa tällä ruudukolla {ruudukko}")
        return False