def negy():

    n = 1
    k = 1

    if (k % 2 == 1) and (n > 0) and (pow(2, n) > k):
        # jó eset
        print("Proth-számok: ", end="")
        for n in range(0, 10, 1):
            proth = (k * pow(2, n)) + 1
            print(str(proth) + ", ", end="")
        proth = (k * pow(2, 10)) + 1
        print(proth)
    else:
        print("HIBA: Nem megfelelő számok!")


def negyb():

    print("Proth-számok: ", end="")

    n = 1
    k = 1
    szamlalo = 0

    while szamlalo < 10:
        if (k > 0) and (k % 2 == 1) and (n > 0) and (pow(23) > k):
            proth = (k * pow(2, n)) + 1
            print(str(proth) + ", ", end="")
            szamlalo += 1
            proth = (k * pow(2, 10)) + 1
            print(str(proth), end="")
        else:
            print("HIBA: Nem megfelelő számok!")
        n += 1
