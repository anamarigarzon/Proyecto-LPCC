#Reglas Proposicionales

#Color, si el atributo es cero, es rojo y si es uno, es amarillo.
#Guardia, si el atributo es cero, es de visión normal y si es uno, es daltónico
#Tipo de día, si el atributo es cero, es par y si es uno, es impar
#Día, corresponde al atributo + 1
#Prisionero, corresponde al atributo + 1

import letras_proposicionales


#Regla 1: Un prisionero o es rojo, o es amarillo, pero no ambas

letras = letras_proposicionales.lista_letras(480)
lista = letras_proposicionales.lista_val_letras(12,5,2,2,2)

rojos = []
amarillos=[]

for i in letras:
    h=letras_proposicionales.decodifica(i,480,lista,12,5,2,2,2)
    if (h[2]==0):
        rojos.append(h)
    else:
        amarillos.append(h)
        
regla1 = ""
        
#Tomar todas las letras proposicionales que tengan color rojo, y unirlas todas con un O 
#Luego, lo anterior implica (-->)
#Negar todas las letras proposicionales que tengan amarillo, y unirlas todas con un Y
#Concatenar todo en una fórmula en el string regla 1
