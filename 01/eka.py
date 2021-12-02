with open("input_1.txt") as syote:
    luvut = []
    for r in syote:
        luvut.append(int(r))

kasvua = 0
for i in range(1, len(luvut)):
    if luvut[i] > luvut[i-1]:
        kasvua +=1

print(kasvua)

