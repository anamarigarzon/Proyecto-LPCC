# -----------------------ALGORITMO DE TSEITIN-------------------------

# Subrutinas para la transformacion de una
# formula a su forma clausal

def enFNC(A):
    # Subrutina de Tseitin para encontrar la FNC de
    # la formula en la pila
    # Input: A (cadena) de la forma
    #                   p=-q
    #                   p=(qYr)
    #                   p=(qOr)
    #                   p=(q>r)
    # Output: B (cadena), equivalente en FNC
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = "-"+q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
def Tseitin(A, letrasProposicionalesA):
    #  IMPLEMENTAR AQUI ALGORITMO TSEITIN
    #letrasProposicionalesB = [chr(x) for x in range(97, 110)]
    #letrasProposicionalesB = ['A', 'B', 'C', 'D', 'E', 'F']
    #letrasProposicionalesB = [chr(x) for x in range(65, 91)]
    #letrasProposicionalesB = [chr(x) for x in range(65, 78)]
    
    letrasProposicionalesB = [chr(x) for x in range(256, 1200)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    L = [] # Inicializamos lista de conjunciones
    Pila = [] # Inicializamos pila
    I = -1 # Inicializamos contador de variables nuevas
    S = A[0] # Inicializamos sımbolo de trabajo
    
    while len(A) > 0:
        if (S in letrasProposicionalesA or S in letrasProposicionalesB) and len(Pila) > 0 and Pila[-1] == "-":
            I += 1
            atomo = letrasProposicionalesB[I]
            Pila = Pila[:-1]
            Pila.append(atomo)
            L.append(atomo + "=-" + S)
            A = A[1:]
            if len(A) > 0:
                S = A[0]
        elif S == ")":
            w = Pila[-1]
            u = Pila[-2]
            v = Pila[-3]
            Pila = Pila[:len(Pila)-4]
            I += 1
            atomo = letrasProposicionalesB[I]
            L.append(atomo + "=" + "(" + v + u + w + ")")
            S = atomo
        else:
            Pila.append(S)
            A = A[1:]
            if len(A) > 0:
                S = A[0]
                
    B = ""
    
    if I < 0:
        atomo = Pila[-1]
        
    else:
        atomo = letrasProposicionalesB[I]
        
    for x in L:
       y = enFNC(x)
       B = B + "Y" + y
    
    B = atomo + B
    return B

# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula
# Output: L (lista), lista de literales
# Se asume que cada literal es un solo caracter
def Clausula(C):

    #  IMPLEMENTAR AQUI ALGORITMO CLAUSULA
    L = []
    while len(C) > 0:
        S = C[0]
        if S == "-":
            L.append(S + C[1])
            C = C[3:]
        else:
            L.append(S)
            C = C[2:]
    return L

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC
# Output: L (lista), lista de listas de literales
def formaClausal(A):
    #  IMPLEMENTAR AQUI ALGORITMO FORMA CLAUSAL
    L = []
    i = 0
    while len(A) > 0:
        if (i >= len(A)):
            L.append(Clausula(A))
            A = []
        else:
            if A[i] == 'Y':
                L.append(Clausula(A[:i]))
                A = A[i+1:]
                i = 0
            else:
                i += 1
    
    return L
