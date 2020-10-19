#-*-coding: utf-8-*-
# Edgar Andrade, Septiembre 2018

# Visualizacion de tableros de ajedrez 3x3 a partir de
# una lista de literales. Cada literal representa una casilla;
# el literal es positivo sii hay un caballo en la casilla.

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

    # Cargando imagen de caballo
    arr_img = plt.imread("prisionero.png", format='png')
    imagebox = OffsetImage(arr_img, zoom=0.1)
    imagebox.image.axes = axes

    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[0] = [0.1, 0.75]
    direcciones[1] = [0.3, 0.75]
    direcciones[2] = [0.5, 0.75]
    direcciones[3] = [0.7, 0.75]
    direcciones[4] = [0.9, 0.75]
    direcciones[5] = [0.1, 0.2]
    direcciones[6] = [0.3, 0.2]
    direcciones[7] = [0.5, 0.2]
    direcciones[8] = [0.7, 0.2]
    direcciones[9] = [0.9, 0.2]

    for l in f:
        if f[l][1] != 0:
            ab = AnnotationBbox(imagebox, direcciones[int(l)], frameon=False)
            axes.add_artist(ab)
            
    # Creando las direcciones en la imagen del número del prisionero de acuerdo a literal
    direcciones2 = {}
    direcciones2[0] = [0.09, 0.9]
    direcciones2[1] = [0.29, 0.9]
    direcciones2[2] = [0.49, 0.9]
    direcciones2[3] = [0.69, 0.9]
    direcciones2[4] = [0.89, 0.9]
    direcciones2[5] = [0.09, 0.37]
    direcciones2[6] = [0.29, 0.37]
    direcciones2[7] = [0.49, 0.37]
    direcciones2[8] = [0.69, 0.37]
    direcciones2[9] = [0.89, 0.37]
    
    for l in f:
        if f[l][1] != 0:
            axes.text(direcciones2[l][0],direcciones2[l][1],str(f[l][0]))

    #plt.show()
    fig.savefig("tablero_" + str(n) + ".png")
   

f={0:[1,0], 1:[2,1], 2:[3,0], 3:[4,1], 4:[5,0], 5:[1,1], 6:[2,0], 7:[3,1], 8:[4,0], 9:[5,1]}

dibujar_tablero(f,121)