import math


def ot():
    szam = int(input("Kérem, adjon meg egy 40 és 95 közötti számot! "))
    if szam < 40 or szam > 95:
        print("HIBA: nem megfelelő szám!")
    else:
        # első megoldás: szöveggé konvertálás, szövegkezelés, nem tanultuk.
        szam = str(szam)
        print(szam[0])

        # második megoldás:
        szam = int(szam)
        print(str(int(szam / 10)))

        # harmadik megoldás:
        szam = int(szam)
        print(str(math.floor(szam / 10)))
