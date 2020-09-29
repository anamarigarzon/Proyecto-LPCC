#letras_proposicionales

def num_letras(Nd, Np, Nc, Ntg, Ntd): 
    return Nd*Np*Nc*Ntg*Ntd

def codifica1(d, p, Nd, Np): # Recibe día, prisionero, Número de días y número de prisioneros
    assert((d >= 1) and (d <= Nd)), 'Primer argumento incorrecto! Debe ser un numero entre 1 y ' + str(Nd)  + "\nSe recibio " + str(d)
    assert((p >= 1) and (p <= Np)), 'Segundo argumento incorrecto! Debe ser un numero entre 1 y ' + str(Np)  + "\nSe recibio " + str(p)
    
    n = Nd*p+d
    return n

#def codifica2():

#def codifica3():
    
#def decodifica():
    
#BOE

Nd = 12 #Número de días
Np = 5 #Número de prisioneros
Nc = 3 #Número de colores
Ntg = 2 #Número de tipos de guardias
Ntd = 2 #Número de tipo de días
    
print ("Hay ", (num_letras(Nd,Np,Nc, Ntg, Ntd)), " letras proposicionales.")
