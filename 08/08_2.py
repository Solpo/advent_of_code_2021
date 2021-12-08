summa = 0
rivinro = 0
with open("input.txt") as f:
    for rivi in f:
        rivinro += 1
        numerot, naytto = rivi.split(" | ")
        numerot = sorted(numerot.rstrip().split(" "), key=len)
        
        aakkostetut = []
        for sana in numerot:
            tyoryhma = []
            for kirjain in sana:
                tyoryhma.append(kirjain)
                tyoryhma.sort()
            uussana = ""
            for kirjain in tyoryhma:
                uussana += kirjain
            aakkostetut.append(uussana)
        numerot = aakkostetut

        ykkonen = [kirjain for kirjain in numerot[0]]
        seiska = [kirjain for kirjain in numerot[1]]
        nelonen = [kirjain for kirjain in numerot[2]]
        viiden_kokoiset = [numerot[i] for i in range(3, 6)]
        kuuden_kokoiset = [numerot[i] for i in range(6, 9)]
        kasi = [kirjain for kirjain in numerot[9]]
        
        for kirjain in seiska:
            if kirjain not in ykkonen:
                aa = kirjain
                break
        else:
            print("aa seiskasta kusi")

        yla_al = []
        for kirjain in nelonen:
            if kirjain not in ykkonen:
                yla_al.append(kirjain)

        for viiden_kokoinen in viiden_kokoiset:
            for kirjain in yla_al:
                if kirjain not in viiden_kokoinen:
                    break
            else:
                vitonen = [viiva for viiva in viiden_kokoinen]
                break
        else:
            print(f"Vitosen löytäminen kusi rivillä {rivinro}")

        for kirjain in ykkonen:
            if kirjain in vitonen:
                af = kirjain
                break

        for kirjain in ykkonen:
            if kirjain != af:
                cee = kirjain
                break
        
        for kuuden_kokoinen in kuuden_kokoiset:
            if cee not in kuuden_kokoinen:
                kutonen = [viiva for viiva in kuuden_kokoinen]
                break
        
        for viiden_kokoinen in viiden_kokoiset:
            for kirjain in ykkonen:
                if kirjain not in viiden_kokoinen:
                    break
            else:
                kolmonen = [viiva for viiva in viiden_kokoinen]
                break
        else: 
            print("Kolmosen löytäminen viiden kokoisista kusi")

        for kirjain in yla_al:
            if kirjain not in kolmonen:
                bee = kirjain
                break
        else:
            print(f"yla-al kusee rivillä {rivinro}")
            break
        
        for kirjain in nelonen:
            if kirjain not in ykkonen and kirjain != bee:
                dee = kirjain
                break
        else:
            print("Nelonen viturallaan")
        
        for kirjain in kutonen:
            if kirjain not in vitonen:
                ee = kirjain
                break
        
        for kirjain in kasi:
            if kirjain not in [aa, bee, cee, dee, ee, af]:
                gee = kirjain
                break

        
        # Sitten näytön sisältö
        taulu = ""
        for luku in naytto.rstrip().split(" "):
            if len(luku) == 2:
                taulu += "1"
            elif len(luku) == 3:
                taulu += "7"
            elif len(luku) == 4:
                taulu += "4"
            elif len(luku) == 7:
                taulu += "8"
            elif len(luku) == 5:
                if ee in luku:
                    taulu += "2"
                elif bee in luku:
                    taulu += "5"
                elif bee not in taulu and ee not in taulu:
                    taulu += "3"
                else:
                    print("Mitäs helvettiä nyt (ei mätsäävää viiden kokoista")
            elif len(luku) == 6:
                if dee not in luku:
                    taulu += "0"
                elif cee not in luku:
                    taulu += "6"
                elif ee not in luku:
                    taulu += "9"
                else:
                    print("Mitäs helvettiä nyt (ei mätsäävää kuuden kokoista")
                    break
            else:
                print("Mitäs helvettiä nyt (vääränkokoinen luku")
        if len(taulu) < 4:
            print(f"Rivillä {rivinro} ongelma")
        
        print(taulu)
        taulu = int(taulu)
        
        # print(taulu)
        summa += taulu


            
print(f"Vastaus on {summa}")