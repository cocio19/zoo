opakovat = "ano"
while opakovat == "ano":

    import random

    cislo1 = int(input("zadej 1 cislo"))
    cislo2 = int(input("zadej 2 cislo"))
    zamenko = input("zadej +,-,*,/")

    vysledky = []

    if zamenko == "+":
        soucet = cislo1 +cislo2
        vysledky.append(soucet)
    elif zamenko == "-":
        rozdil = cislo1 - cislo2
        vysledky.append(rozdil)
    elif zamenko == "*":
        socin = cislo1 * cislo2
        vysledky.append(socin)
    elif zamenko == "/":
        podil = cislo1 / cislo2
        vysledky.append(podil)
    else:
        print("spatne zanmenko")


    print(random.choice(vysledky))
    print(vysledky)

    opakovat = input("chcete znova?")

