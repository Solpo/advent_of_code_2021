import apufunktiot

with open("input.txt") as f:
    luvun_pituus = len(f.readline().rstrip())

luvut = []

with open("input.txt") as f:
    for rivi in f:
        luvut.append(rivi.rstrip())

# happi
happikarsittava = luvut.copy()
happikarsittu = []

for i in range(luvun_pituus):
    enemman = apufunktiot.kumpaa_enemman_kohdassa(happikarsittava, i)
    for binaari in happikarsittava:
        if binaari[i] == str(enemman):
            happikarsittu.append(binaari)
        elif enemman == 2 and binaari[i] == "1":
            happikarsittu.append(binaari)
        else:
            # print(f"i = {i}, binaari = {binaari}, ei lisätty")
            pass
    happikarsittava = happikarsittu.copy()
    happikarsittu = []
    if len(happikarsittava) == 0:
        print("happikarsittava meni nolliin, virhe")
    elif len(happikarsittava) == 1:
        print(f"Onnistui, happikarsittava = {happikarsittava}")
        print(f"desimaalilukuna {apufunktiot.binaaristr_intiksi(happikarsittava[0])}")
        break

# hiili
hiilikarsittava = luvut.copy()
hiilikarsittu = []

for i in range(luvun_pituus):
    enemman = apufunktiot.kumpaa_enemman_kohdassa(hiilikarsittava, i)
    for binaari in hiilikarsittava:
        if enemman == 2 and binaari[i] == "0":
            hiilikarsittu.append(binaari)
        
        elif binaari[i] != str(enemman):
            hiilikarsittu.append(binaari)
        else:
            pass
            # print(f"i = {i}, binaari = {binaari}, ei lisätty")
    hiilikarsittava = hiilikarsittu.copy()
    hiilikarsittu = []
    if len(hiilikarsittava) == 0:
        # print("hiilikarsittava meni nolliin, virhe")
        pass
    elif len(hiilikarsittava) == 1:
        print(f"Onnistui, hiilikarsittava = {hiilikarsittava}")
        print(f"desimaalilukuna {apufunktiot.binaaristr_intiksi(hiilikarsittava[0])}")
        break

print(f"Kerrottuna toisillaan (vastaus) = {apufunktiot.binaaristr_intiksi(happikarsittava[0]) * apufunktiot.binaaristr_intiksi(hiilikarsittava[0])}")