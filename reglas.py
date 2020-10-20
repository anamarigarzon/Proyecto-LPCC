# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:01:03 2020

@author: Ana Garzón y Gabriela Linares

Reglas en Lógica Proposicional

Proyecto Lógica para Ciencias de la Computación
"""

#NO SIRVE STRING2TREE


import codificacion_letras

conectivos = ['>','O','Y','=']

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def String2Tree(A):
	# Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
	# Input: - A, lista de caracteres con una formula escrita en notacion polaca inversa
	#        - letrasProposicionales, lista de letras proposicionales
	#        - conectivos, lista de conectivos
	# Output: formula como tree
	pila = []
	for c in A:
		# print("Examinando " + str(c))
		if c in codificacion_letras.cod:
			# print(u"El símbolo es letra proposicional")
			pila.append(Tree(c, None, None))
		elif c == '-':
			# print("Negamos")
			formulaAux = Tree(c, None, pila[-1])
			del pila[-1]
			pila.append(formulaAux)
		elif c in conectivos:
			# print("Unimos mediante conectivo")
			formulaAux = Tree(c, pila[-1], pila[-2])
			del pila[-1]
			del pila[-1]
			pila.append(formulaAux)
		else:
			print(u"Hay un problema: el símbolo " + str(c) + " no se reconoce")
	return pila[-1]

def Inorderp(f):
    if f.right == None:
        return str(codificacion_letras.Pinv(f.label, Nfilas, Ncolumnas, Nnumeros))
    elif f.label == '-':
        return f.label + Inorderp(f.right)
    else:
        return "(" + Inorderp(f.left) + f.label + Inorderp(f.right) + ")"

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

#-------------------------------------------------------------
#Regla 1:
print("FÓRMULA REGLA 1")
print("")
prisioneros=[0,1,2,3,4]
casillas = []
Nfilas = 5
Ncolumnas = 2
Nnumeros = 5
R1 = ""
Regla1 = ""

for i in range(1):
    for j in range(0, Ncolumnas):
        v1 = codificacion_letras.codifica(i, j, Nfilas, Ncolumnas)
        casillas.append(v1)
 
print("\n")       
print(casillas)

ini = True
for i in prisioneros:
    R1 += "Y"
    Regla1 += ">"
    for j in casillas:
        f, c = codificacion_letras.decodifica(j, Nfilas, Ncolumnas)
        aux = [x for x in casillas if x != j]
        Regla1 += codificacion_letras.P(f, c, i, Nfilas, Ncolumnas, Nnumeros)
        if ini == True:
            Regla1 += "-OOO"
        ini == False
        for h in aux:
            f, c = codificacion_letras.decodifica(h, Nfilas, Ncolumnas)
            Regla1 += codificacion_letras.P(f, c, i, Nfilas, Ncolumnas, Nnumeros)
            
R1 += Regla1 #R2 es la cadena en notación polaca
Regla1 = R1[::-1] #Regla2 es la cadena en notación polaca inversa

print("\n" + Regla1)
print("")

#-------------------------------------------------------------
#Regla 2: Un prisionero no está en más de una casilla

print("FÓRMULA REGLA 2")
print("")
    
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
    for j in casillas:
        R2 += "Y"
        Regla2 += ">"
        f, c = codificacion_letras.decodifica(j, Nfilas, Ncolumnas)
        aux = [x for x in casillas if x != j]
        Regla2 += codificacion_letras.P(f, c, i, Nfilas, Ncolumnas, Nnumeros)
        if ini == True:
            Regla2 += "-OOOOOOOO"
        ini == False
        for h in aux:
            f, c = codificacion_letras.decodifica(h, Nfilas, Ncolumnas)
            Regla2 += codificacion_letras.P(f, c, i, Nfilas, Ncolumnas, Nnumeros)

R2 += Regla2 #R2 es la cadena en notación polaca
Regla2 = R2[::-1] #Regla2 es la cadena en notación polaca inversa
print(Regla2)
#print(Inorderp(String2Tree(Regla2))) #ERROR, INDEX OUT OF RANGE

print("")

#-------------------------------------------------------------
#Regla 3: Si un prisionero sale un día par, ningún prisionero puede salir un día impar. Así mismo, si un prisionero sale un día impar, ningún prisionero puede salir un día par.
    
print("FÓRMULA REGLA 3")
print("")

prisioneros=[0,1,2,3,4]
casillasi = [1,3,5,7,9]
casillasp = [0,2,4,6,8]
Nfilas = 5
Ncolumnas = 2
Nnumeros = 5
R3 = ""
Regla3 = ""

ini = True
for n in prisioneros:
    for j in range(0,2):
        R3 += "Y"
        Regla3 += ">"
        f, c = codificacion_letras.decodifica(j, Nfilas, Ncolumnas)
        Regla3 += codificacion_letras.P(f, c, n, Nfilas, Ncolumnas, Nnumeros)
        Regla3 += "-"
        for i in range(25):
            Regla3 += "O"
        if j == 0:
            for h in casillasi:
                a, b = codificacion_letras.decodifica(h, Nfilas, Ncolumnas)
                for x in prisioneros:
                    Regla3 += codificacion_letras.P(a, b, x, Nfilas, Ncolumnas, Nnumeros)
        if j == 1:
            for h in casillasp:
                a, b = codificacion_letras.decodifica(h, Nfilas, Ncolumnas)
                for x in prisioneros:
                    Regla3 +=codificacion_letras.P(a, b, x, Nfilas, Ncolumnas, Nnumeros)
                
R3 += Regla3 #R3 es la cadena en notación polaca
Regla3 = R3[::-1] #Regla3 es la cadena en notación polaca inversa    
print(Regla3)
#print(Inorderp(String2Tree(Regla3))) #ERROR, INDEX OUT OF RANGE

print("")
    
#-------------------------------------------------------------                       
#Regla 4: Los cinco prisioneros deben salir. Eso significa que deben estar llenas o todas las casillas blancas, o todas las casillas grises. 
print("FÓRMULA REGLA 4")
print("")

prisioneros=[0,1,2,3,4]

letrasporcelda = ["","","","","","","","","",""]
casillas = []

lpcp = []
lpci = []

Nfilas = 5
Ncolumnas = 2
Nnumeros = 5
prisioneros = [0,1,2,3,4]
R4 = "OY"
Regla4 = ""

for i in range(Nfilas):
    for j in range(Ncolumnas):
        v1 = codificacion_letras.codifica(i, j, Nfilas, Ncolumnas)
        casillas.append(v1)

for i in casillas:
     f, c = codificacion_letras.decodifica(i, Nfilas, Ncolumnas)
     for n in prisioneros:
         letrasporcelda[i] += (codificacion_letras.P(f, c, n, Nfilas, Ncolumnas, Nnumeros))

for i in range(10):
    if i%2 == 0:
        lpcp.append(letrasporcelda[i])
    else:
        lpci.append(letrasporcelda[i])


Regla4 = "YYYY"
for i in lpcp:
    a = "OOOO"
    a += i
    Regla4 += a

R4 += Regla4

Regla4 ="-OOOO"
    
for i in lpci:
    a = "OOOO"
    a += i
    i = a
    Regla4 += a

R4 += Regla4

Regla4 = "YYYYY"
for i in lpci:
    a = "OOOO"
    a += i
    Regla4 += a

R4 += Regla4

Regla4 ="-OOOO"
for i in lpci:
    a = "OOOO"
    a += i
    i = a
    Regla4 += a

R4 += Regla4
Regla4 = R4[::-1]
print(Regla4)
#print(Inorderp(String2Tree(Regla4))) # ERROR, INDEX OUT OF RANGE

