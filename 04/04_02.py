import time, bingo

with open("input.txt") as f:
    voittava = [int(voittonumero) for voittonumero in f.readline().split(",")]
    f.readline()

    ruudukot = []
    tyoruudukko = []

    for rivi in f:
        if rivi == "\n":
            pass
        else:
            bingorivi = [int(numero) for numero in rivi.split(" ") if numero != ""]
            tyoruudukko.append(bingorivi.copy())
            if len(tyoruudukko) == 5:
                ruudukot.append(tyoruudukko.copy())
                tyoruudukko = []

# print(ruudukot)
# print(voittava)

while len(ruudukot) > 1:
    voitettu = False
    for i in range(len(voittava)):
        if not voitettu:
            for ruudukko in ruudukot:
                if bingo.vaakabingo(ruudukko, voittava[:i+1]) != False:
                    voittoruudukko, kaytetyt_voitonumerot = bingo.vaakabingo(ruudukko, voittava[:i+1])
                    voitettu = True
                    break
                if bingo.pystybingo(ruudukko, voittava[:i+1]) != False:
                    voittoruudukko, kaytetyt_voitonumerot = bingo.pystybingo(ruudukko, voittava[:i+1])
                    voitettu = True
                    break
    litistetty_voittoruudukko = [numero for rivi in voittoruudukko for numero in rivi]

    for numero in kaytetyt_voitonumerot:
        if numero in litistetty_voittoruudukko:
            litistetty_voittoruudukko.remove(numero)

    print(f"Jäljelle jääneiden numeroiden summa on {sum(litistetty_voittoruudukko)}")
    print(f"Ratkaiseva voittonumero oli {kaytetyt_voitonumerot[-1]}")
    print(f"Nämä kerrottuna keskenään = {sum(litistetty_voittoruudukko) * kaytetyt_voitonumerot[-1]}")
    ruudukot.remove(voittoruudukko)


voitettu = False
for i in range(len(voittava)):
    if not voitettu:
        for ruudukko in ruudukot:
            if bingo.vaakabingo(ruudukko, voittava[:i+1]) != False:
                voittoruudukko, kaytetyt_voitonumerot = bingo.vaakabingo(ruudukko, voittava[:i+1])
                voitettu = True
                break
            if bingo.pystybingo(ruudukko, voittava[:i+1]) != False:
                voittoruudukko, kaytetyt_voitonumerot = bingo.pystybingo(ruudukko, voittava[:i+1])
                voitettu = True
                break
litistetty_voittoruudukko = [numero for rivi in voittoruudukko for numero in rivi]

for numero in kaytetyt_voitonumerot:
    if numero in litistetty_voittoruudukko:
        litistetty_voittoruudukko.remove(numero)

print(f"Tämän pitäisi olla vihoviimeinen ruudukko, ruudukkojen listan pituus on {len(ruudukot)}")
print(f"Jäljelle jääneiden numeroiden summa on {sum(litistetty_voittoruudukko)}")
print(f"Ratkaiseva voittonumero oli {kaytetyt_voitonumerot[-1]}")
print(f"Nämä kerrottuna keskenään = {sum(litistetty_voittoruudukko) * kaytetyt_voitonumerot[-1]}")
