# Tämän ratkaiseminen sanakirjoilla eikä listoilla oli vähän turhan
# monimutkainen toteutus. Sou not, nytpä tämä sit lukisi tekstiäkin.

import apufunktiot

with open("input.txt") as f:
    luvun_pituus = len(f.readline().rstrip())

kohdat = {}
for i in range(luvun_pituus):
    kohdat[i] = {}

with open("input.txt") as f:
    for rivi in f:
        for kohta in range(len(rivi.strip())):
            try:
                kohdat[kohta][int(rivi[kohta])] += 1
            except:
                kohdat[kohta][int(rivi[kohta])] = 1

print(kohdat)

suuremmat = ""

for i in range(len(kohdat)):
    suuremmat += str(apufunktiot.enemman(kohdat[i]))

pienemmat = apufunktiot.kaanna_binaaristr(suuremmat)
vastaus = apufunktiot.binaaristr_intiksi(suuremmat) * apufunktiot.binaaristr_intiksi(pienemmat)

print(f"Vastaus on {vastaus}")