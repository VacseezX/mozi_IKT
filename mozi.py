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