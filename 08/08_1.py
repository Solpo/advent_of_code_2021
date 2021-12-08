with open("input.txt") as f:
    helppoja = 0
    for rivi in f:
        numerot, naytto = rivi.split(" | ")
        print(naytto)
        for luku in naytto.rstrip().split(" "):
            if len(luku) in [2, 3, 4, 7]:
                helppoja += 1

print(helppoja)