# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:01:03 2020

@author: Ana Garzón y Gabriela Linares

Reglas en Lógica Proposicional

Proyecto Lógica para Ciencias de la Computación
"""
import codificacion_letras

class Tree(object):
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label
        
def String2Tree(A):
    letrasProposicionales=[chr(x) for x in range(256, 600)]
    Conectivos = ['O','Y','>','=']
    Pila = []
    for c in A:
        if c in letrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c=='-':
            FormulaAux = Tree(c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree(c,Pila[-1],Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
        else:
            print(u"Hay un problema: el símbolo " + str(c)+ " no se reconoce")
    return Pila[-1]

def Inorderp(f):
    Nfilas = 5
    Ncolumnas = 2
    Nnumeros = 5
    if f.right == None:
        return str(codificacion_letras.Pinv(f.label, Nfilas, Ncolumnas, Nnumeros))
    elif f.label == '-':
        return f.label + Inorderp(f.right)
    else:
        return "(" + Inorderp(f.left) + f.label + Inorderp(f.right) + ")"

#-------------------------------------------------------------
#Regla 1:

#-------------------------------------------------------------
#Regla 2:
    
prisioneros=[0,1,2,3,4]
casillas = []
Nfilas = 5
Ncolumnas = 2
Nnumeros = 5
R2 = ""
Regla2 = ""


for i in range(Nfilas):
    for j in range(Ncolumnas):
        v1 = codificacion_letras.codifica(i, j, Nfilas, Ncolumnas)
        casillas.append(v1)
        
ini = True
for i in prisioneros:
    R2 += "Y"
    Regla2 += ">"
    for j in casillas:
        f, c = codificacion_letras.decodifica(j, Nfilas, Ncolumnas)
        aux = [x for x in casillas if x != j]
        Regla2 += codificacion_letras.P(f, c, i, Nfilas, Ncolumnas, Nnumeros)
        if ini == True:
            Regla2 += "-OOOOOOOOO"
        ini == False
        for h in aux:
            f, c = codificacion_letras.decodifica(h, Nfilas, Ncolumnas)
            Regla2 += codificacion_letras.P(f, c, i, Nfilas, Ncolumnas, Nnumeros)

R2 += Regla2 #R2 es la cadena en notación polaca
Regla2 = R2[::-1] #Regla2 es la cadena en notación polaca inversa

#-------------------------------------------------------------
#Regla 3:
prisioneros=[0,1,2,3,4]
casillas = []
Nfilas = 5
Ncolumnas = 2
Nnumeros = 5

#-------------------------------------------------------------                       
#Regla 4:
prisioneros=[0,1,2,3,4]
casillas = []
Nfilas = 5
Ncolumnas = 2
Nnumeros = 5
