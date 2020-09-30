

import letras_proposicionales


#Regla 1: Un prisionero o es rojo, o es amarillo, pero no ambas

letras = letras_proposicionales.lista_letras(480)
lista = letras_proposicionales.lista_val_letras(12,5,2,2,2)

prisioneros = [0,1,2,3,4]
form_regla1 = ""
temp = ""

for j in prisioneros:
    form_regla1 += "("
    for i in letras:
        h=letras_proposicionales.decodifica(i,480,lista,12,5,2,2,2)
        if h[1] == j:            
            if (h[2]==0):
                form_regla1 += str(i)
                form_regla1 += "O"
            
    form_regla1= form_regla1 + ")"
        
        
#Tomar todas las letras proposicionales que tengan color rojo, y unirlas todas con un O 
#Luego, lo anterior implica (-->)
#Negar todas las letras proposicionales que tengan amarillo, y unirlas todas con un Y
