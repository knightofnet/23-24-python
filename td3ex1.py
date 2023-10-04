#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def maFonction(n) :
    L=[]
    for i in range(1, n + 1) :
        if i % 2 != 0 and n % i == 0 :
            L.append(i)
    return len(L)

def maFonctionCompteur(n) :
    cpt = 0
    for i in range(1, n + 1) :
        if i % 2 != 0 and n % i == 0 :
            cpt += 1
    return cpt

print(maFonction(21))
assert maFonction(21) == 4