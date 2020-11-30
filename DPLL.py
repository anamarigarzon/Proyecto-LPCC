from tseitin import *

print("")
print("--------------DPLL----------------")
def unidad(S):
  for x in S:
    if len(x) == 1:
      un = x[0]
      return un
  return None

def complemento(un):
  if un[0] == '-':
    return un[1]
  else:
    return '-' + un

def unit_propagate(S,I):

  y = True

  while y:

    for i in S:
      if len(i) == 0:
        y = False

    un = unidad(S)

    if un != None:
      y = True
      #SE BORRAN LAS CLAUSULAS COMPLETAS QUE TIENEN A L
      if len(un) == 1:
        I[un] = 1
        
      else:
        I[complemento(un)] = 0
      S = [x for x in S if un not in x]
      #SE BORRA Lc DE LAS DEMÁS CLAUSULAS
      for clause in S:
        if complemento(un) in clause:
          clause.remove(complemento(un))

    else:
      y = False
      
  return S, I


def literal_no_asignado(atomos, diccionario):
  for x in atomos:
    for y in x:
      if not y in diccionario:
        return y


def DPLL(S,I):
  S, I = unit_propagate(S,I)
  
  if [] in S:
    return "Insatisfacible", {}
  
  elif len(S) == 0:
    return "Satisfacible", I

  p = literal_no_asignado(S, I)

  #SE BORRAN LAS CLAUSULAS COMPLETAS QUE TIENEN A L
  Sp = [x[:] for x in S if p not in x]
  #SE BORRA Lc DE LAS DEMÁS CLAUSULAS
  for clause in Sp:
    if complemento(p) in clause:
      clause.remove(complemento(p))

  Ip = I

  if len(p) == 1:
        Ip[p] = 1
  else:
        Ip[complemento(p)] = 0

  o, l = DPLL(Sp, Ip)

  if o == "Satisfacible" and l == Ip:
    return "Satisfacible", Ip
  
  else:
    Spp = S

    #SE BORRA Lc DE TODAS LAS CLAUSULAS
    Spp = [x[:] for x in S if complemento(p) not in x]

    #SE BORRA L DE LAS CLAUSULAS QUE TIENEN A L
    for clause in Spp:
      if p in clause:
        clause.remove(p)

    Ipp = I

    if len(p) == 1:
          Ipp[p] = 0
    else:
          Ipp[complemento(p)] = 1

    return  DPLL(Spp,Ipp)

#PUNTO 4 TALLER DPLL


dic = {}

Vverdad, Diccionario1 = DPLL(Clausulas, dic)

Diccionario = {}

for i in Diccionario1:
    if i in letras:
        Diccionario[i] = Diccionario1[i]

print("")
print("El problema es: ", Vverdad)
print("")
print("Valores de las letras de una posible solución:")
print("")
print(Diccionario)
