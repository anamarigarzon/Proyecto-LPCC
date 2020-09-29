#letras_proposicionales
#Creación, codificación y decodificación

def num_letras(Nd,Np,Nc,Ng,Ntd): #Recibe como argumentos la cantidad de días, prisioneros, colores, guardias y tipos de días
    #Función que saca el número de letras proposicionales del problema
    
    return Nd*Np*Nc*Ng*Ntd

    
def codifica(d, p, c, g, td, Nd, Np, Nc, Ng, Ntd): #Recibe como argumentos el dia, prisionero, color, guardia, tipo de día, y la respectiva cantidad de cada uno de estos atributos para el problema
    #codifica el valor de una letra proposicional a partir de sus atributos
    
    assert((d >= 0) and (d <= Nd - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nd - 1)  + "\nSe recibio " + str(d)
    assert((p >= 0) and (p <= Np - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Np - 1)  + "\nSe recibio " + str(p)
    assert((c >= 0) and (c <= Nc - 1)), 'Tercer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1)  + "\nSe recibio " + str(c)
    assert((g >= 0) and (g <= Ng - 1)), 'Cuarto argumento incorrecto! Debe ser un numero entre 0 y ' + str(Ng - 1)  + "\nSe recibio " + str(g)
    assert((td >= 0) and (td <= Ntd - 1)), 'Quinto argumento incorrecto! Debe ser un numero entre 0 y ' + str(Ntd - 1)  + "\nSe recibio " + str(td)
    
    #Modificar los valores con el fin de que al operarlos con la ecuación de abajo produzcan un entero único
    
    p = p+12 
    c = c+17
    g = g+19
    td = td+21
        
    n = td*p*c*g + d #Entero único para este problema
    
    return n #retorna variable que contiene al entero único


def lista_val_letras(Nd,Np,Nc,Ng,Ntd): #Recibe como argumentos la cantidad de días, prisioneros, colores, guardias y tipos de días
    #genera una lista con cada uno de los valores de las letras proposicionales
    
    mylist = [] # lista vacía

    for d in range(Nd):
        for p in range(Np):
            for c in range(Nc):
                for g in range(Ng):
                    for t in range(Ntd):
                        v1 = codifica(d, p, c, g, t, Nd, Np, Nc, Ng, Ntd)
                        mylist.append(v1) #Se guarda cada uno de los valores de las letras proposicionales en mylist
                        
    return mylist #Retorna lista con todos los valores de cada una las letras proposicionales


def lista_letras(n): #Recibe el número de letras proposicionales, y retorna una lista con n caracteres distintos
    letras = []
    
    for i in range(n):
        letras.append(chr(i+200))
    
    return letras        


def prueba_codifica(n, mylist): #Recibe como argumentos el número de letras proposicionales, y una lista que contiene los valores de las letras proposicionales
    #Función que prueba si en efecto, el valor de cada una de las letras proposicionales es único
    
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
        

def decodifica(n, k, lista1, Nd, Np, Nc, Ng, Ntd): #Recibe como atributos la letra proposicional n, el número de letras proposicionales k, una lista con los valores de las letras proposicionales, y la cantidad de cada uno de los atributos mencionados anteriormente
    #Función que decodifica una letra proposicional, y retorna una lista con sus atributos, ordenados en día, prisionero,color, guardia y tipo de día
    
    n = ord(n)
    
    assert((n >= 200) and (n <= k+200)), 'Codigo incorrecto! Debe estar entre 200 y' + str(k+200) + "\nSe recibio " + str(n)
    
    j = int(n) - 200 # restarle 200 al número para obtener la 
    
    num = lista1[j]

    for d in range(Nd):
        for p in range(Np):
            for c in range(Nc):
                for g in range(Ng):
                    for t in range(Ntd):
                        v1 = codifica(d, p, c, g, t, Nd, Np, Nc, Ng, Ntd)
                        if v1 == num:
                            atributos = [d,p,c,g,t] #lista con sus atributos, ordenados en día, prisionero,color, guardia y tipo de día, respectivamente
                            break
    
    return atributos
   
    
    
#BEGINNING-OF-EXECUTION
    
n = num_letras(12,5,2,2,2)
lista = lista_val_letras(12,5,2,2,2)

prueba_codifica(n, lista)

g = chr(200)
a = decodifica(g,480,lista,12,5,2,2,2)

print ("Letra: ",g)
print ("Código: [ ", end="")
for i in a:
    print (i,end= ", ")
print ("]")
#END-OF-EXECUTION
