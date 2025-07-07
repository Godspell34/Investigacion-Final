"""
Búsquedas binarias avanzadas.
Incluye arrays rotados, matrices 2D y búsqueda aproximada.
"""

def busqueda_binaria_rotated_array(arr, objetivo):
    """
    Búsqueda binaria en un array rotado (sorted and rotated).
    
    Args:
        arr: Array que fue ordenado y luego rotado
        objetivo: Valor a buscar
        
    Returns:
        Índice del elemento si se encuentra, -1 si no se encuentra
        
    Complejidad:
        - Tiempo: O(log n)
        - Espacio: O(1)
    """
    if not arr:
        return -1
    
    izquierda = 0
    derecha = len(arr) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if arr[medio] == objetivo:
            return medio
        
        # Verificar si la mitad izquierda está ordenada
        if arr[izquierda] <= arr[medio]:
            # La mitad izquierda está ordenada
            if arr[izquierda] <= objetivo < arr[medio]:
                derecha = medio - 1
            else:
                izquierda = medio + 1
        else:
            # La mitad derecha está ordenada
            if arr[medio] < objetivo <= arr[derecha]:
                izquierda = medio + 1
            else:
                derecha = medio - 1
    
    return -1

def encontrar_punto_rotacion(arr):
    """
    Encuentra el punto de rotación en un array rotado.
    
    Args:
        arr: Array rotado
        
    Returns:
        Índice del elemento más pequeño (punto de rotación)
    """
    if not arr:
        return -1
    
    izquierda = 0
    derecha = len(arr) - 1
    
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        
        if arr[medio] > arr[derecha]:
            izquierda = medio + 1
        else:
            derecha = medio
    
    return izquierda

def busqueda_binaria_2d(matriz, objetivo):
    """
    Búsqueda binaria en una matriz 2D ordenada.
    La matriz debe estar ordenada de izquierda a derecha y de arriba a abajo.
    
    Args:
        matriz: Matriz 2D ordenada
        objetivo: Valor a buscar
        
    Returns:
        Tupla (fila, columna) si se encuentra, (-1, -1) si no se encuentra
        
    Complejidad:
        - Tiempo: O(log(m*n)) = O(log m + log n)
        - Espacio: O(1)
    """
    if not matriz or not matriz[0]:
        return (-1, -1)
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Comenzar desde la esquina superior derecha
    fila = 0
    col = columnas - 1
    
    while fila < filas and col >= 0:
        if matriz[fila][col] == objetivo:
            return (fila, col)
        elif matriz[fila][col] > objetivo:
            col -= 1  # Mover a la izquierda
        else:
            fila += 1  # Mover hacia abajo
    
    return (-1, -1)

def busqueda_binaria_2d_optimizada(matriz, objetivo):
    """
    Búsqueda binaria optimizada en matriz 2D usando búsqueda binaria en filas.
    
    Args:
        matriz: Matriz 2D ordenada
        objetivo: Valor a buscar
        
    Returns:
        Tupla (fila, columna) si se encuentra, (-1, -1) si no se encuentra
        
    Complejidad:
        - Tiempo: O(m * log n) donde m es el número de filas
        - Espacio: O(1)
    """
    if not matriz or not matriz[0]:
        return (-1, -1)
    
    for fila in range(len(matriz)):
        col = busqueda_binaria_en_fila(matriz[fila], objetivo)
        if col != -1:
            return (fila, col)
    
    return (-1, -1)

def busqueda_binaria_en_fila(fila, objetivo):
    """
    Búsqueda binaria en una fila específica.
    """
    return busqueda_binaria(fila, objetivo)

def busqueda_binaria_aproximada(arr, objetivo, tolerancia=0.001):
    """
    Búsqueda binaria para encontrar el elemento más cercano al objetivo.
    
    Args:
        arr: Lista ordenada de números
        objetivo: Valor objetivo
        tolerancia: Tolerancia para considerar elementos iguales
        
    Returns:
        Tupla (índice, valor, diferencia) del elemento más cercano
        
    Complejidad:
        - Tiempo: O(log n)
        - Espacio: O(1)
    """
    if not arr:
        return (-1, None, float('inf'))
    
    izquierda = 0
    derecha = len(arr) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if abs(arr[medio] - objetivo) <= tolerancia:
            return (medio, arr[medio], 0)
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    # Encontrar el elemento más cercano entre los candidatos
    candidatos = []
    
    if izquierda < len(arr):
        candidatos.append((izquierda, arr[izquierda]))
    if derecha >= 0:
        candidatos.append((derecha, arr[derecha]))
    
    mejor_indice = -1
    mejor_valor = None
    mejor_diferencia = float('inf')
    
    for indice, valor in candidatos:
        diferencia = abs(valor - objetivo)
        if diferencia < mejor_diferencia:
            mejor_diferencia = diferencia
            mejor_valor = valor
            mejor_indice = indice
    
    return (mejor_indice, mejor_valor, mejor_diferencia)

def busqueda_binaria_raiz_cuadrada(n, precision=0.0001):
    """
    Calcula la raíz cuadrada de un número usando búsqueda binaria.
    
    Args:
        n: Número para calcular la raíz cuadrada
        precision: Precisión deseada
        
    Returns:
        Raíz cuadrada aproximada
        
    Complejidad:
        - Tiempo: O(log(n/precision))
        - Espacio: O(1)
    """
    if n < 0:
        return None
    
    if n == 0 or n == 1:
        return n
    
    izquierda = 0
    derecha = max(1, n)
    
    while derecha - izquierda > precision:
        medio = (izquierda + derecha) / 2
        
        if medio * medio == n:
            return medio
        elif medio * medio < n:
            izquierda = medio
        else:
            derecha = medio
    
    return (izquierda + derecha) / 2

def busqueda_binaria_potencia(base, exponente, precision=0.0001):
    """
    Calcula la raíz n-ésima de un número usando búsqueda binaria.
    
    Args:
        base: Número base
        exponente: Exponente (1/exponente será la raíz)
        precision: Precisión deseada
        
    Returns:
        Raíz n-ésima aproximada
        
    Complejidad:
        - Tiempo: O(log(base/precision))
        - Espacio: O(1)
    """
    if base < 0 and exponente % 2 == 0:
        return None  # No hay raíz real para números negativos con exponente par
    
    if base == 0:
        return 0
    
    izquierda = -abs(base)
    derecha = abs(base)
    
    while derecha - izquierda > precision:
        medio = (izquierda + derecha) / 2
        
        potencia = medio ** exponente
        
        if abs(potencia - base) < precision:
            return medio
        elif potencia < base:
            izquierda = medio
        else:
            derecha = medio
    
    return (izquierda + derecha) / 2 