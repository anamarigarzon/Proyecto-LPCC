#-*-coding: utf-8-*-
#Ana María Garzón y Gabriela Linares
#A partir de codificación de tablero de ajedrez 3x3 de Edgar Andrade 

# Visualizacion de tableros a partir de
# una lista de literales. Cada literal representa una casilla;
# el literal es positivo sii hay un prisionero en la casilla.

# Formato de la entrada: - las letras proposionales seran: 1, ..., 9;
#                        - solo se aceptan literales (ej. 1, ~2, 3, ~4, etc.)
# Requiere también un número natural, para servir de índice del tablero,
# toda vez que pueden solicitarse varios tableros.

# Salida: archivo tablero_%i.png, donde %i es un número natural

#################
# importando paquetes para dibujar
print("Importando paquetes...")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
print("Listo!")

def dibujar_tablero(f, n):
    # Visualiza un tablero dada una formula f
    # Input:
    #   - f, una lista de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step1 = 1./4
    step2 = 1./5
    tangulos = []
    # Crear los cuadrados grises en el tablero
    tangulos.append(patches.Rectangle(\
                                    (0, 0), \
                                    step2, \
                                    step1*2,\
                                    facecolor='lightslategrey')\
                                    )
    tangulos.append
    tangulos.append(patches.Rectangle(*[(step2*2, 0), step2, step1*2],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(step2, step1*2), step2, step1*2],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(step2*3, step1*2), step2, step1*2],\
            facecolor='lightslategrey'))
    tangulos.append(patches.Rectangle(*[(step2*4, 0), step2, step1*2],\
            facecolor='lightslategrey'))
        
    # Creo los cuadrados oscuros en el tablero
    tangulos.append(patches.Rectangle(*[(0, step1*2), step2, step1*2],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step2, 0), step2, step1*2],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step2*2, step1*2), step2, step1*2],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step2*3, 0), step2, step1*2],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step2*4, step1*2), step2, step1*2],\
            facecolor='cornsilk'))

    # Creo las líneas del tablero
    locacion = step1
    # Crea linea horizontal en el rectangulo
    tangulos.append(patches.Rectangle(*[(0, step1 + locacion), 1, 0.005],\
                                         facecolor='black'))
    
    
    
    for j in range(5):
        locacion = j*step2
        # Crea las lineas verticales en el rectangulo
        tangulos.append(patches.Rectangle(*[(step2 + locacion, 0), 0.005, 1],\
                                          facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)

    # Cargando imagen del prisionero
    arr_img = plt.imread("prisionero.png", format='png')
    imagebox = OffsetImage(arr_img, zoom=0.1)
    imagebox.image.axes = axes

    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[1] = [0.1, 0.75]
    direcciones[3] = [0.3, 0.75]
    direcciones[5] = [0.5, 0.75]
    direcciones[7] = [0.7, 0.75]
    direcciones[9] = [0.9, 0.75]
    direcciones[0] = [0.1, 0.2]
    direcciones[2] = [0.3, 0.2]
    direcciones[4] = [0.5, 0.2]
    direcciones[6] = [0.7, 0.2]
    direcciones[8] = [0.9, 0.2]

    for l in f:
        if f[l][1] != 0:
            ab = AnnotationBbox(imagebox, direcciones[int(l)], frameon=False)
            axes.add_artist(ab)
            
    # Creando las direcciones en la imagen del número del prisionero de acuerdo a literal
    direcciones2 = {}
    direcciones2[1] = [0.09, 0.9]
    direcciones2[3] = [0.29, 0.9]
    direcciones2[5] = [0.49, 0.9]
    direcciones2[7] = [0.69, 0.9]
    direcciones2[9] = [0.89, 0.9]
    direcciones2[0] = [0.09, 0.37]
    direcciones2[2] = [0.29, 0.37]
    direcciones2[4] = [0.49, 0.37]
    direcciones2[6] = [0.69, 0.37]
    direcciones2[8] = [0.89, 0.37]
    
    for l in f:
        if f[l][1] != 0:
            axes.text(direcciones2[l][0],direcciones2[l][1],str(f[l][0]))

    #plt.show()
    fig.savefig("tablero_" + str(n) + ".png")
   
#La fórmula es un diccionario que tiene como key la casilla, y como value una lista que tiene en la posición 0 el numero del 1 al 5
#que identifica al prisionero, y en la posición 1, un 1 si en esa casilla está ese prisionero, y un 0 si la casilla está vacía.
f={0:[1,1], 1:[2,0], 2:[3,0], 3:[4,1], 4:[5,1], 5:[1,0], 6:[2,0], 7:[3,1], 8:[2,1], 9:[5,0]}
#Falta transformar la f para que en lugar de un diccionario, reciba una fórmula.

dibujar_tablero(f,121)
