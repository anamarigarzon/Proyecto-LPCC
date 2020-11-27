# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:01:03 2020
@author: Ana Garzón y Gabriela Linares
Reglas en Lógica Proposicional
Proyecto Lógica para Ciencias de la Computación
"""

#NO SIRVE STRING2TREE


from codificacion_letras import *

conectivos = ['>','O','Y','=']

class Tree(object):
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label
        
def String2Tree(A):
    letrasProposicionales = letras
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
    if f.right == None:
        return str(Pinv(f.label, 5, 2, 5))
    elif f.label == '-':
        return f.label + Inorderp(f.right)
    else:
        return "(" + Inorderp(f.left) + f.label + Inorderp(f.right) + ")"

def Inorderpu(f):
    if f.right == None:
        return f.label
    elif f.label == '-':
        return f.label + Inorderpu(f.right)
    else:
        return "(" + Inorderpu(f.left) + f.label + Inorderpu(f.right) + ")"

def Inorder2Tree(A):
	if len(A) == 1:
		return Tree(A[0], None, None)
	elif A[0] == '-':
		return Tree(A[0], None, Inorder2Tree(A[1:]))
	elif A[0] == "(":
		counter = 0 #Contador de parentesis
		for i in range(1, len(A)):
			if A[i] == "(":
				counter += 1
			elif A[i] == ")":
				counter -=1
			elif (A[i] in ['Y', 'O', '>', '=']) and (counter == 0):
				return Tree(A[i], Inorder2Tree(A[1:i]), Inorder2Tree(A[i + 1:-1]))
	else:
		return -1



#-------------------------------------------------------------.
#Regla 1: Para el segundo turno, deben estar llenas o la celdas 1 y o la celda 0, pero no ambas
print("")
print("FÓRMULA REGLA 1")
print("")
prisioneros=[0,1,2,3,4]
casillas = []
Nfilas = 5
Ncolumnas = 2
Nnumeros = 5
regla_1_1 = ""
regla_1_2 = ""
formula = ""

for j in range(0, Ncolumnas):
    v1 = codifica(0, j, Nfilas, Ncolumnas)
    casillas.append(v1)

print("\n")       
print(casillas)
    

listareglas = []

for x in prisioneros:
    #s = [j for j in prisioneros if j != x]
    inicial = True
    for i in prisioneros:
        if inicial:
            regla_1_1 = P(0, 1, i, Nfilas, Ncolumnas, Nnumeros)
            inicial = False
        else:
            regla_1_1 += P(0, 1, i, Nfilas, Ncolumnas, Nnumeros) + "O"
        
    regla_1_1 = regla_1_1 + "-" + P(0, 0, x, Nfilas, Ncolumnas, Nnumeros) + '>'
    listareglas.append(regla_1_1)
    #print(Inorderp(String2Tree(regla_1_1)))
    #print("")
    regla_1_1 = ""

inicial1 = True        
for x in listareglas:
    if inicial1:
        regla_1_1 = x
        inicial1 = False
    else:
        regla_1_1 += x + "O"

#print(regla_1_1)

#print("")
 
#print(Inorderp(String2Tree(regla_1_1)))


#print("")
#print("")

listareglas = []

for x in prisioneros:
    #s = [j for j in prisioneros if j != x]
    inicial = True
    for i in prisioneros:
        if inicial:
            regla_1_2 = P(0, 0, i, Nfilas, Ncolumnas, Nnumeros)
            inicial = False
        else:
            regla_1_2 += P(0, 0, i, Nfilas, Ncolumnas, Nnumeros) + "O"
        
    regla_1_2 = regla_1_2 + "-" + P(0, 1, x, Nfilas, Ncolumnas, Nnumeros) + '>'
    listareglas.append(regla_1_2)
    #print(Inorderp(String2Tree(regla_1_2)))
    #print("")
    regla_1_2 = ""

inicial1 = True        
for x in listareglas:
    if inicial1:
        regla_1_2 = x
        inicial1 = False
    else:
        regla_1_2 += x + "O"

#print(regla_1_2)

#print("")
 
#print(Inorderp(String2Tree(regla_1_2)))

Regla1 = regla_1_1 + regla_1_2 + 'O'

#print(Regla1)

#print("")
 
print(Inorderp(String2Tree(Regla1)))


#-------------------------------------------------------------
#Regla 2: Un prisionero no está en más de una casilla

print("FÓRMULA REGLA 2")
print("")
    
prisioneros=[0,1,2,3,4]
casillas = []
Nfilas = 5
Ncolumnas = 2
Nnumeros = 5


for i in range(Nfilas):
    for j in range(Ncolumnas):
        v1 = codifica(i, j, Nfilas, Ncolumnas)
        casillas.append(v1)

print("\n")       
print(casillas)

def r21(p):
    listareglas = []
    
    for x in casillas:    
        f,c = decodifica(x,Nfilas,Ncolumnas)
        s = [j for j in casillas if j != x]
        inicial1 = True
        for i in s:
            f1,c1 = decodifica(i,Nfilas,Ncolumnas)
            if inicial1:
                regla_2_1 = P(f1, c1, p, Nfilas, Ncolumnas, Nnumeros)
                inicial1 = False
            else:
                regla_2_1 += P(f1, c1, p, Nfilas, Ncolumnas, Nnumeros) + "O"
                    
        regla_2_1 = regla_2_1 + "-" + P(f, c, p, Nfilas, Ncolumnas, Nnumeros) + '>'
        listareglas.append(regla_2_1)
        print(Inorderp(String2Tree(regla_2_1)))
        print("")
        regla_2_1 = ""
    
    inicial = True 
    for x in listareglas:
        if inicial:
            regla_2_1 = x
            inicial = False
        else:
            regla_2_1 += x + "O"
    
    return regla_2_1

Regla2 = ""
listareglas = []

for i in prisioneros:
    listareglas.append(r21(i))
    
inicial1 = True        
for x in listareglas:
    if inicial1:
        Regla2 = x
        inicial1 = False
    else:
        Regla2 += x + "O" #RECORDAR

#print(Regla2)

print("")
 
print(Inorderp(String2Tree(Regla2)))


#-------------------------------------------------------------
#Regla 3: Si un prisionero sale un día par, ningún prisionero puede salir un día impar. Así mismo, si un prisionero sale un día impar, ningún prisionero puede salir un día par.

print("")
print("FÓRMULA REGLA 3")
print("")

prisioneros=[0,1,2,3,4]
casillas1 = [0,2,4,6,8]
casillas2 = [1,3,5,7,9]
Nfilas = 5
Ncolumnas = 2
Nnumeros = 5


inicial = True

def r31(p,caslist,inicial1):
    regla_3_1 = ""
    for x in caslist:    
        f1,c1 = decodifica(x,Nfilas,Ncolumnas)
        if inicial1:
            regla_3_1 = P(f1, c1, p, Nfilas, Ncolumnas, Nnumeros)
            inicial1 = False
        else:
            regla_3_1 += P(f1, c1, p, Nfilas, Ncolumnas, Nnumeros) + "O"
                      
    return regla_3_1

def r32(num_cas):
    inicial = True
    regla_3_2 = ""
    if num_cas % 2 == 0:
        for p in prisioneros:
            if inicial:
                regla_3_2 = r31(p,casillas2,inicial)
                inicial = False
            else:
                regla_3_2 += r31(p,casillas2,inicial)
                
    else:
        for p in prisioneros:
            if inicial:
                regla_3_2 = r31(p,casillas1,inicial)
                inicial = False
            else:
                regla_3_2 += r31(p,casillas1,inicial)
    
    return regla_3_2
                
def r33(num_cas):
    inicial = True
    regla_3_3 = ""
    for i in prisioneros:
        f,c = decodifica(num_cas,Nfilas,Ncolumnas)
        if inicial:
            regla_3_3 = r32(num_cas) + '-' + P(f,c,i,Nfilas,Ncolumnas,Nnumeros) + '>'
            inicial = False
        else:
            regla_3_3 += r32(num_cas) + '-' + P(f,c,i,Nfilas,Ncolumnas,Nnumeros) + '>' + 'O'
    
    return regla_3_3
    
def r34():
    inicial = True
    regla_3_4 = ""
    for i in range(0,1):
        if inicial:
            regla_3_4 = r33(i)
            inicial = False
        else:
            regla_3_4 += r33(i) + 'O'
    return regla_3_4

Regla3 = r34()
        
print(Inorderp(String2Tree(Regla3)))   

print("")



#-------------------------------------------------------------                       
#Regla 4: Los cinco prisioneros deben salir. Eso significa que deben estar llenas o todas las casillas blancas, o todas las casillas grises. 
print("FÓRMULA REGLA 4")
print("")

prisioneros=[0,1,2,3,4]
casillasp = [0,2,4,6,8]
casillasi = [1,3,5,7,9]
Nfilas = 5
Ncolumnas = 2
Nnumeros = 5

def r41(casx):

    regla_4_1 = ""
    inicial = True
    f,c = decodifica(casx,Nfilas,Ncolumnas)
    for i in prisioneros:
        if inicial:
            regla_4_1 = P(f,c,i,Nfilas,Ncolumnas,Nnumeros)
            inicial = False
        else:
            regla_4_1 += P(f,c,i,Nfilas,Ncolumnas,Nnumeros) + 'O'
            
    return regla_4_1

def r42(casx):
    regla_4_2 = ""
    if casx % 2 == 0:
        inicial1 = True
        for i in casillasp:
            if inicial1:
                regla_4_2 = r41(i)
                inicial1 = False
            else:
                regla_4_2 += r41(i) + 'Y'
    else:
        inicial1 = True
        for i in casillasi:
            if inicial1:
                regla_4_2 = r41(i)
                inicial1 = False
            else:
                regla_4_2 += r41(i) + 'Y'
                
    return regla_4_2

Regla4 = r42(0) + r42(1) + 'O'

print(Inorderp(String2Tree(Regla4)))  

#-----------------------------------------------------------------
#------------------REGLA GENERAL-------------------

ReglaGeneral = Regla1 + Regla2 + 'Y' + Regla3 + 'Y' + Regla4 + 'Y'

print("")
print("-----REGLA GENERAL-----")
print("")
print(Inorderp(String2Tree(ReglaGeneral))) 

