
#PUNTO 2 Y 3 TALLER DPLL
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
lista1 = [["p", "q","r"],["-p","-q","-r"],["-p","q","r"],["-q","r"],["q","-r"]]
lista2 = [["p","q","r","-s"],["p","t","s"],["-p","-q"],["p","r","-q","-s"]]
lista3 = [["p","q","-r"],["r","s","t"],["t"],["p","s"],["q","-p"]]
lista4 = [["p","-q"],["-p","-q"],["q","r"],["-q","-r"],["-p","-r"],["p","-r"]]
lista5 = [["r","p","s"],["-r","-p"],["-r","p","s"],["p","-s"]]
dic = {}

x, y = DPLL(lista1, dic)

print(x)
print(y)

print('')
dic = {}
x, y = DPLL(lista2, dic)

print(x)
print(y)

print('')
dic = {}
x, y = DPLL(lista3, dic)

print(x)
print(y)

print('')

dic = {}
x, y = DPLL(lista4, dic)

print(x)
print(y)

print('')

dic = {}
x, y = DPLL(lista5, dic)

print(x)
print(y)

print('')