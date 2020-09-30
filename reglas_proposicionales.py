#Reglas Proposicionales

#Color, si el atributo es cero, es rojo y si es uno, es amarillo.
#Guardia, si el atributo es cero, es de visión normal y si es uno, es daltónico
#Tipo de día, si el atributo es cero, es par y si es uno, es impar
#Día, corresponde al atributo + 1
#Prisionero, corresponde al atributo + 1

import letras_proposicionales



letras = letras_proposicionales.lista_letras(480)
lista = letras_proposicionales.lista_val_letras(12,5,2,2,2)

color = [0,1]
guardia = [0,1]
tipodia = [0,1]
dia = [1,2,3,4,5,6,7,8,9,10,11,12]
prisionero = [0,1,2,3,4]

def Regla1(letras): #Un prisionero no puede ser amarillo y rojo a la vez
    
    Nd = 12
    Np = 5
    Nc = 2
    Ng = 2
    Ntd = 2
    
    for i in letras:
        letras_proposicionales.decodifica(i,480,lista,12,5,2,2,2)
        if 
