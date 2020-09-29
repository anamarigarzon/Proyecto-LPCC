# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:11:58 2020

@author: gabil
"""

def codifica(d, p, c, g, td, Nd, Np, Nc, Ng, Ntd):
    # Funcion que codifica la fila f y columna c
    assert((d >= 0) and (d <= Nd - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nd - 1)  + "\nSe recibio " + str(d)
    assert((p >= 0) and (p <= Np - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Np - 1)  + "\nSe recibio " + str(p)
    assert((c >= 0) and (c <= Nc - 1)), 'Tercer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1)  + "\nSe recibio " + str(c)
    assert((g >= 0) and (g <= Ng - 1)), 'Cuarto argumento incorrecto! Debe ser un numero entre 0 y ' + str(Ng - 1)  + "\nSe recibio " + str(g)
    assert((td >= 0) and (td <= Ntd - 1)), 'Quinto argumento incorrecto! Debe ser un numero entre 0 y ' + str(Ntd - 1)  + "\nSe recibio " + str(td)
    n = Nd * Np * Nc * Ng * Ntd * d + p
    # print(u'Número a codificar:', n)
    return n

def decodifica(n, Nf, Nc):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla
    assert((n >= 0) and (n <= Nf * Nc - 1)), 'Codigo incorrecto! Debe estar entre 0 y' + str(Nf * Nc - 1) + "\nSe recibio " + str(n)
    f = int(n / Nc)
    c = n % Nc
    return f, c

Nd = 12
Np = 5
Nc = 2
Ng = 2
Ntd = 2
filas = 480
col = 5

print(u"Números correspondientes a la codificación")
print("\nDias\tPrisioneros\tColor\tGuardia\tTdia")
for d in range(Nd):
    for p in range(Np):
        for c in range(Nc):
            for g in range(Ng):
                for t in range(Ntd):
                    v1 = codifica(d, p, c, g, t, Nd, Np, Nc, Ng, Ntd)

for i in range(filas):
    p#rint("\t")
    for x in range(col):
        print(v1, end = " ")
    