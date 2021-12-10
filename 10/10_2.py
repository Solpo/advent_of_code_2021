with open("testi.txt") as f:
    rivit = []
    for rivi in f:
        rivit.append(rivi.rstrip())

sulut = {")": "(", "]": "[", "}": "{", ">": "<"}
sulut_sulkijalla = {"(": ")", "[": "]", "{": "}", "<": ">"}
def korvaa(sana: str, kohta: int, merkki: str) -> str:
    # if kohta == len(sana) - 1:
    if kohta >= len(sana) or len(merkki) != 1:
        raise
    palautettava = sana[:kohta] + merkki + sana[kohta + 1:]
    return palautettava


def perkaa(sana: str, alku: int =0, loppu: int =None) -> str:
    palautettava = sana
    for i in range(len(sana[alku:loppu])):
        if sana[i] in sulut.keys():
            sulkeva = sana[i]
            for j in range(i-1, alku -1, -1):
                if sana[j] in sulut.values() and sana[j] != sulut[sulkeva]:
                    print(f"Virheellinen sulku löytyi, pitäisi olla {sulut_sulkijalla[sana[j]]}")
                    print(f"Virheellinen sulku oli {sulkeva}")
                    return "rikki"
                elif sana[j] == sulut[sana[i]]:
                
                    palautettava = korvaa(palautettava, i, "_")
                    palautettava = korvaa(palautettava, j, "_")
                    return palautettava
                    # else:
                    #     return perkaa(sana, j + 1, i)
    else:
        # print("Rivi katkeaa kesken")
        return "katkesi"

rivinro = 0
for rivi in rivit:
    rivinro += 1
    print(f"Syötteen rivi {rivinro}")
    while True:
        rivi = perkaa(rivi)
        if rivi == "katkesi" or rivi == "rikki":
            # print("kokeillaan uudella rivillä")
            break