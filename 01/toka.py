with open("input_1.txt") as syote:
    luvut = []
    for r in syote:
        luvut.append(int(r))

kasvua = 0

for i in range(len(luvut) - 3):
    if sum(luvut[i:i+3]) < sum(luvut[i+1:i+4]):
        kasvua += 1

print(kasvua)