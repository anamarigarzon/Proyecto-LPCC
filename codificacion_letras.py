# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 08:11:58 2020
@author: Ana Garzón y Gabriela Linares
Codificación Letras Proposicionales
Proyecto Lógica para Ciencias de la Computación
"""

print("-------CODIFICACIÓN LETRAS PROPOSICIONALES---------")

def codifica(f, c, Nf, Nc):
    # Funcion que codifica la fila f y columna c
    assert((f >= 0) and (f <= Nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf) - 1  + "\nSe recibio " + str(f)
    assert((c >= 0) and (c <= Nc - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1)  + "\nSe recibio " + str(c)
    n = Nc * f + c
    #print(u'Número a codificar:', n)
    return n

def decodifica(n, Nf, Nc):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla
    #assert((n >= 0) and (n <= Nf * Nc - 1)), 'Codigo incorrecto! Debe estar entre 0 y' + str(Nf * Nc - 1) + "\nSe recibio " + str(n)
    f = int(n / Nc)
    c = n % Nc
    return f, c

Nfilas = 5
Ncolumnas = 2

print(u"Números correspondientes a la codificación")
print("\nfilas x columnas")
for i in range(Nfilas):
    for j in range(Ncolumnas):
        v1 = codifica(i, j, Nfilas, Ncolumnas)
        print(v1, end = " ")
    print("")
print("\n")

for v1 in range(10):
    f, c = decodifica(v1, Nfilas, Ncolumnas)
    print('Código: '+str(v1)+', Fila: '+str(f)+', Columna: '+str(c))

letras = []
print("\n\nfilas x columnas")
for i in range(Nfilas):
    for j in range(Ncolumnas):
        v1 = codifica(i, j, Nfilas, Ncolumnas)
        cod = chr(v1 + 256)
        print(cod, end = " ")
        letras.append(cod)
    print("")
print("\n")

for cod in letras:
    print('Letra = '+cod, end=', ')
    f, c = decodifica(ord(cod)-256, Nfilas, Ncolumnas)
    print('Fila = '+str(f), end=', ')
    print('Columna = '+str(c))
    
def P(f, c, o, Nf, Nc, No):
    # Funcion que codifica tres argumentos
    assert((f >= 0) and (f <= Nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf - 1) + "\nSe recibio " + str(f)
    assert((c >= 0) and (c <= Nc - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1) + "\nSe recibio " + str(c)
    assert((o >= 0) and (o <= No - 1)), 'Tercer argumento incorrecto! Debe ser un numero entre 0 y ' + str(No - 1)  + "\nSe recibio " + str(o)
    v1 = codifica(f, c, Nf, Nc)
    v2 = codifica(v1, o, Nf * Nc, No)
    codigo = chr(256 + v2)
    return codigo

def Pinv(codigo, Nf, Nc, No):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    x = ord(codigo) - 256
    v1, o = decodifica(x, Nf * Nc, No)
    f, c = decodifica(v1, Nf, Nc)
    return f, c, o

print("\n")
letras = []
n = 0
Nnumeros = 5
for k in range(Nnumeros):
    print("Prisionero: "+str(k))
    print("filas x columnas")
    for i in range(Nfilas):
        for j in range(Ncolumnas):
            n += 1
            cod = P(i, j, k, Nfilas, Ncolumnas, Nnumeros)
            print(cod, end = " ")
            letras.append(cod)
        print("")
    print('\n')
    


print("Total de letras proposicionales: ", n)

for cod in letras:
    print('Letra = '+cod, end=', ')
    f, c, o = Pinv(cod, Nfilas, Ncolumnas, Nnumeros)
    print('Prisionero = '+str(o), end=', ')
    print('Fila = '+str(f), end=', ')
    print('Columna = '+str(c), end=',')
    print('Número de letra: ', ord(cod))
