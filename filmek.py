"""
Olvasd be a mellékelt file (film.txt) tartalmát, majd add meg az adatok sorainak a számát (az első sor nélkül)!

Melyik a legrövidebb film címe?

Hány darab legalább 110 perces film van?

Kérd be egy színész nevét, és ajánlj egy pár filmet a készletből, ha tudsz (film címét íratjuk ki, ha van ilyen)! Ha nincs ilyen nevű színész, akkor azt is tudasd!

A 4-es feladat eredményét írasd ki fájlba is! 
"""

from Film import Film

def beolvas():
    filmek_lista=[]
    fajl=open("film.txt","r",encoding="utf-8")
    fajl.readline()
    nyers_lista=fajl.readlines()
    fajl.close()

    for i in range(0,len(nyers_lista),1):
        sor=nyers_lista[i]
        elem=sor.strip().split(";")
        cim: str=(elem[0])
        rendezo: str=(elem[1])
        foszereplo: str=(elem[2])
        ev: int=(elem[3])
        perc: int=(elem[4])
        film=Film(cim,rendezo,foszereplo,ev,perc)
        filmek_lista.append(film)
    return filmek_lista

"""def legrovidebb(filmek_lista):
    legrovidebb_index=0
    for i in range(0,len(filmek_lista),1):
        if filmek_lista[legrovidebb_index].perc >= filmek_lista[i].perc:
            legrovidebb_index=i
    return legrovidebb_index
"""
def szaztiz(filmek_lista):
    szamlalo= 0
    for i in range(0,len(filmek_lista),1):
        if filmek_lista[i].perc > 110:
            szamlalo += 1
    return szamlalo