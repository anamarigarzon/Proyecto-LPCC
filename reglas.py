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

#Regla 1:

#Regla 2:
    
#Regla 3:
    
#Regla 4:
