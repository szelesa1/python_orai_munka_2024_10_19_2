# 1.	Kérj be egy 5-el osztható, háromjegyűjegyű számot, majd add meg a négyzetét! Ha nem megfelelő adatot adott meg a felhasználó, akkor írj neki hibaüzenetet: „HIBA: Nem megfelelő szám!”

def ketto():

    szam = int(input("Kérem adjon meg egy háromjegyű 5-el osztható számot! "))
    # jó eset
    if (((szam > 99) and (szam < 1000)) or ((szam < -99) and (szam > -1000)) and szam % 5 == 0):
          negyzet = szam ** 2
          print(negyzet)

    # rossz eset
    else:
         print("HIBA: Nem megfelelő szám!")

