"""
Variantes avanzadas de búsqueda binaria.
Incluye búsqueda de primera/última ocurrencia y límites.
"""

def busqueda_binaria_primera_ocurrencia(arr, objetivo):
    """
    Encuentra la primera ocurrencia de un elemento en un array ordenado.
    
    Args:
        arr: Lista ordenada de números (puede tener duplicados)
        objetivo: Valor a buscar
        
    Returns:
        Índice de la primera ocurrencia, -1 si no se encuentra
        
    Complejidad:
        - Tiempo: O(log n)
        - Espacio: O(1)
    """
    if not arr:
        return -1
    
    izquierda = 0
    derecha = len(arr) - 1
    resultado = -1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if arr[medio] == objetivo:
            resultado = medio
            derecha = medio - 1  # Seguir buscando a la izquierda
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return resultado

def busqueda_binaria_ultima_ocurrencia(arr, objetivo):
    """
    Encuentra la última ocurrencia de un elemento en un array ordenado.
    
    Args:
        arr: Lista ordenada de números (puede tener duplicados)
        objetivo: Valor a buscar
        
    Returns:
        Índice de la última ocurrencia, -1 si no se encuentra
        
    Complejidad:
        - Tiempo: O(log n)
        - Espacio: O(1)
    """
    if not arr:
        return -1
    
    izquierda = 0
    derecha = len(arr) - 1
    resultado = -1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if arr[medio] == objetivo:
            resultado = medio
            izquierda = medio + 1  # Seguir buscando a la derecha
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return resultado

def busqueda_binaria_menor_mayor_igual(arr, objetivo):
    """
    Encuentra el primer elemento mayor o igual al objetivo.
    
    Args:
        arr: Lista ordenada de números
        objetivo: Valor a buscar
        
    Returns:
        Índice del primer elemento >= objetivo, len(arr) si no existe
        
    Complejidad:
        - Tiempo: O(log n)
        - Espacio: O(1)
    """
    if not arr:
        return 0
    
    izquierda = 0
    derecha = len(arr) - 1
    resultado = len(arr)
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if arr[medio] >= objetivo:
            resultado = medio
            derecha = medio - 1
        else:
            izquierda = medio + 1
    
    return resultado

def busqueda_binaria_mayor_menor_igual(arr, objetivo):
    """
    Encuentra el último elemento menor o igual al objetivo.
    
    Args:
        arr: Lista ordenada de números
        objetivo: Valor a buscar
        
    Returns:
        Índice del último elemento <= objetivo, -1 si no existe
        
    Complejidad:
        - Tiempo: O(log n)
        - Espacio: O(1)
    """
    if not arr:
        return -1
    
    izquierda = 0
    derecha = len(arr) - 1
    resultado = -1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if arr[medio] <= objetivo:
            resultado = medio
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return resultado

def contar_ocurrencias(arr, objetivo):
    """
    Cuenta el número de ocurrencias de un elemento en un array ordenado.
    
    Args:
        arr: Lista ordenada de números
        objetivo: Valor a contar
        
    Returns:
        Número de ocurrencias del elemento
        
    Complejidad:
        - Tiempo: O(log n)
        - Espacio: O(1)
    """
    primera = busqueda_binaria_primera_ocurrencia(arr, objetivo)
    ultima = busqueda_binaria_ultima_ocurrencia(arr, objetivo)
    
    if primera == -1:
        return 0
    
    return ultima - primera + 1

def busqueda_binaria_rango(arr, objetivo_inicio, objetivo_fin):
    """
    Encuentra el rango de elementos entre objetivo_inicio y objetivo_fin.
    
    Args:
        arr: Lista ordenada de números
        objetivo_inicio: Valor inicial del rango
        objetivo_fin: Valor final del rango
        
    Returns:
        Tupla (inicio, fin) con los índices del rango
        
    Complejidad:
        - Tiempo: O(log n)
        - Espacio: O(1)
    """
    inicio = busqueda_binaria_menor_mayor_igual(arr, objetivo_inicio)
    fin = busqueda_binaria_mayor_menor_igual(arr, objetivo_fin)
    
    if inicio > fin:
        return (-1, -1)
    
    return (inicio, fin)

def busqueda_binaria_floor_ceil(arr, objetivo):
    """
    Encuentra el floor (mayor elemento <= objetivo) y ceil (menor elemento >= objetivo).
    
    Args:
        arr: Lista ordenada de números
        objetivo: Valor de referencia
        
    Returns:
        Tupla (floor, ceil) con los índices
        
    Complejidad:
        - Tiempo: O(log n)
        - Espacio: O(1)
    """
    floor = busqueda_binaria_mayor_menor_igual(arr, objetivo)
    ceil = busqueda_binaria_menor_mayor_igual(arr, objetivo)
    
    return (floor, ceil) 