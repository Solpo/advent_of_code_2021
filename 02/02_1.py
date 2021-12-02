with open("input.txt") as syote:
    liikkeet = []
    for r in syote:
        liike = r.split(" ")
        if liike[0] == "up":
            liike = ("y", -int(liike[1]))
        elif liike[0] == "down":
            liike = ("y", int(liike[1]))
        elif liike[0] == "forward":
            liike = ("x", int(liike[1]))
        else:
            liikkeet = "virhe"
            break
        liikkeet.append((liike[0], int(liike[1])))

x = 0
y = 0
for koordinaatti in liikkeet:
    if koordinaatti[0] == "x":
        x += koordinaatti[1]
    elif koordinaatti[0] == "y":
        y += koordinaatti[1]
    else:
        liikkeet = "virhe"
        break
    
print(liikkeet)
print(f"x = {x}")
print(f"y = {y}")
print(f"x * y = {x * y}")
