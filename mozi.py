import random
import math

moziTerem = []
megadottSzam = 0
arak = [2500, 2100, 1300, 0]

def ulohelyek(lista:list):
    for sor in range(15):
        sorok = []
        for ulohely in range(10):
            sorok.append(random.choice(arak))
        sorok.append(" ")
        for ulohely in range(10):
            sorok.append(random.choice(arak))
        lista.append(sorok)
    return lista

def foglaltJegy(szam:int):
    while szam < 2 or szam > 5:
        print("Adja meg a megvásárolni kívánt jegyek darabszámát!")
        szam = int(input())
    return szam

def szabadHely(lista:list, szam:int):
    i = 0
    for sor in lista:
        szabadHelyek = 0
        i += 1
        for ulohely in sor:
            if ulohely == 0 and ulohely != " ":
                szabadHelyek += 1
            else:
                szabadHelyek = 0
            if szabadHelyek == szam:
                return i

def bevetel(lista:list):
    bevetel = 0
    for sor in lista:
        for ulohely in sor:
            if ulohely != " ":
                bevetel += ulohely
    return bevetel

def kihasznaltsag(lista:list):
    foglaltUlohely = 0
    for sor in lista:
        for ulohely in sor:
            if ulohely != 0 and ulohely != " ":
                foglaltUlohely += 1
    return round((foglaltUlohely/3),2)