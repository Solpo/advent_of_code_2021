with open("input.txt") as f:
    maarat_ian_perusteella = {}
    iat = [int(ika) for ika in f.readline().rstrip().split(",")]

print(iat)
for ika in iat:
    if ika in maarat_ian_perusteella.keys():
        maarat_ian_perusteella[ika] += 1
    else:
        maarat_ian_perusteella[ika] = 1

print(maarat_ian_perusteella)

for _ in range(256):
    uudet_maarat = {}

    for i in range(max(maarat_ian_perusteella.keys()), min(maarat_ian_perusteella.keys()) -1, -1):
        if i in maarat_ian_perusteella.keys():
            if i > 0:
                uudet_maarat[i-1] = maarat_ian_perusteella[i]
            elif i == 0:
                uudet_maarat[8] = maarat_ian_perusteella[i]
                if 6 not in uudet_maarat.keys():
                    uudet_maarat[6] = maarat_ian_perusteella[i]
                else:
                    uudet_maarat[6] += maarat_ian_perusteella[i]
    maarat_ian_perusteella = uudet_maarat

    print(f"Kierros {_}")
    for i in range(max(maarat_ian_perusteella.keys()), min(maarat_ian_perusteella.keys()) -1, -1):
        if i in maarat_ian_perusteella.keys():
            print(i, " ",  maarat_ian_perusteella[i])

print(f"Valokaloja on {sum(maarat_ian_perusteella.values())}")