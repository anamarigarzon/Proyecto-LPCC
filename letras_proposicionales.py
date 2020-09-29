#letras_proposicionales


def num_letras(Nd,Np,Nc,Ng,Ntd): #Función que saca el número de letras proposicionales del problema
    
    return Nd*Np*Nc*Ng*Ntd
    
def codifica(d, p, c, g, td, Nd, Np, Nc, Ng, Ntd): #Recibe como argumentos el dia, prisionero, color, guardia, tipo de día, y la respectiva cantidad de cada uno de estos atributos para el problema
    
    assert((d >= 0) and (d <= Nd - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nd - 1)  + "\nSe recibio " + str(d)
    assert((p >= 0) and (p <= Np - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Np - 1)  + "\nSe recibio " + str(p)
    assert((c >= 0) and (c <= Nc - 1)), 'Tercer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1)  + "\nSe recibio " + str(c)
    assert((g >= 0) and (g <= Ng - 1)), 'Cuarto argumento incorrecto! Debe ser un numero entre 0 y ' + str(Ng - 1)  + "\nSe recibio " + str(g)
    assert((td >= 0) and (td <= Ntd - 1)), 'Quinto argumento incorrecto! Debe ser un numero entre 0 y ' + str(Ntd - 1)  + "\nSe recibio " + str(td)
    
    p = p+12
    c = c+17
    g = g+19
    td = td+21
        
    n = td*p*c*g + d
    
    return n

def lista_letras(Nd,Np,Nc,Ng,Ntd): #retorna una lista con todos los valores de las letras proposicionales
    
    n=0

    mylist = []

    for d in range(Nd):
        for p in range(Np):
            for c in range(Nc):
                for g in range(Ng):
                    for t in range(Ntd):
                        v1 = codifica(d, p, c, g, t, Nd, Np, Nc, Ng, Ntd)
                        print(v1, end=" ")
                        mylist.append(v1)
                        n = n+1
    assert()
    return mylist

def prueba_codifica(n, mylist): #Prueba que, efectivamente, codifica funciona y todos los valores de las letras proposicionales son distintos
    
    j = 0

    for i in mylist:
        h = mylist.count(i)
        if (h > 1):
            print("prueba con otra fórmula")
            break
        else:
            j = j+1
    
    if(j==n):
        print("Los números no se repiten, perfecto")
