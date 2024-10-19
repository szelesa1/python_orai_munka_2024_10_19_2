# 1.	Hozz létre egy szín változót, állíts be egy tetszőleges szín értéket. Ha a szín piros, fehér, vagy zöld írd ki, hogy a magyar zászlóban szerepel. Minden más esetben írd ki, hogy „A magyar zászlóban nem szerepel.”

def egy():

    szin = "Piros"
    if szin == "fehér" or szin == "piros" or szin == "zöld" or szin == "Fehér" or szin == "Piros" or szin == "Zöld":
        print("A magyar zászlóban szerepel.")
    else:
        print("A magyar zászlóban nem szerepel.")

