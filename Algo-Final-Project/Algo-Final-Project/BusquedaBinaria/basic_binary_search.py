"""
Implementación básica de búsqueda binaria.
Incluye versiones iterativa y recursiva.
"""

def busqueda_binaria(arr, objetivo):
    """
    Búsqueda binaria iterativa.
    
    Args:
        arr: Lista ordenada de números
        objetivo: Valor a buscar
        
    Returns:
        Índice del elemento si se encuentra, -1 si no se encuentra
        
    Complejidad:
        - Tiempo: O(log n)
        - Espacio: O(1)
        
    Requisitos:
        - El array debe estar ordenado
    """
    # eliminar el array si esta vacio
    if not arr:
        return -1
    
    # inicializar los indices
    izquierda = 0
    derecha = len(arr) - 1
    
    # mientras el indice izquierdo sea menor o igual al indice derecho
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        # si el elemento medio es igual al objetivo, retornar el indice medio
        if arr[medio] == objetivo:
            return medio
        # si el elemento medio es menor al objetivo, mover el indice izquierdo a la derecha del medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        # si el elemento medio es mayor al objetivo, mover el indice derecho a la izquierda del medio
        else:
            derecha = medio - 1
    
    # si no se encuentra el elemento, retornar -1
    return -1

def busqueda_binaria_recursiva(arr, objetivo, izquierda=None, derecha=None):
    """
    Búsqueda binaria recursiva.
    
    Args:
        arr: Lista ordenada de números
        objetivo: Valor a buscar
        izquierda: Índice izquierdo (para recursión)
        derecha: Índice derecho (para recursión)
        
    Returns:
        Índice del elemento si se encuentra, -1 si no se encuentra
        
    Complejidad:
        - Tiempo: O(log n)
        - Espacio: O(log n) debido a la pila de recursión
    """
    if not arr:
        return -1
    
    # Inicializar índices en la primera llamada
    if izquierda is None:
        izquierda = 0
    if derecha is None:
        derecha = len(arr) - 1
    
    # Caso base: no se encontró
    if izquierda > derecha:
        return -1
    
    medio = (izquierda + derecha) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, izquierda, medio - 1)

def busqueda_binaria_con_comparaciones(arr, objetivo):
    """
    Búsqueda binaria que cuenta el número de comparaciones realizadas.
    
    Args:
        arr: Lista ordenada de números
        objetivo: Valor a buscar
        
    Returns:
        Tupla (índice, número_de_comparaciones)
    """
    if not arr:
        return (-1, 0)
    
    izquierda = 0
    derecha = len(arr) - 1
    comparaciones = 0
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        
        if arr[medio] == objetivo:
            return (medio, comparaciones)
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return (-1, comparaciones)

def busqueda_binaria_con_trazado(arr, objetivo):
    """
    Búsqueda binaria que muestra el proceso paso a paso.
    
    Args:
        arr: Lista ordenada de números
        objetivo: Valor a buscar
        
    Returns:
        Índice del elemento si se encuentra, -1 si no se encuentra
    """
    if not arr:
        print("Array vacío")
        return -1
    
    izquierda = 0
    derecha = len(arr) - 1
    paso = 1
    
    print(f"Buscando {objetivo} en: {arr}")
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        print(f"Paso {paso}: izquierda={izquierda}, medio={medio}, derecha={derecha}")
        print(f"  arr[medio] = {arr[medio]}")
        
        if arr[medio] == objetivo:
            print(f"  ¡Encontrado en índice {medio}!")
            return medio
        elif arr[medio] < objetivo:
            print(f"  {arr[medio]} < {objetivo}, buscar en la derecha")
            izquierda = medio + 1
        else:
            print(f"  {arr[medio]} > {objetivo}, buscar en la izquierda")
            derecha = medio - 1
        
        paso += 1
    
    print(f"  No se encontró {objetivo}")
    return -1 