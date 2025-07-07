"""
Implementación básica del algoritmo QuickSort.
"""

def quicksort(arr):
    """
    Implementación del algoritmo QuickSort básico.
    
    Args:
        arr: Lista de números a ordenar
        
    Returns:
        Lista ordenada (nueva lista)
        
    Complejidad:
        - Tiempo: O(n log n) promedio, O(n²) peor caso
        - Espacio: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    # Elegir el pivote (en este caso, el último elemento)
    pivot = arr[-1]
    
    # Dividir en elementos menores, iguales y mayores al pivote
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursivamente ordenar las sublistas y combinar
    return quicksort(left) + [pivot] + quicksort(right)

def quicksort_inplace(arr, low=0, high=None):
    """
    Implementación de QuickSort in-place (modifica la lista original).
    
    Args:
        arr: Lista de números a ordenar
        low: Índice inicial (por defecto 0)
        high: Índice final (por defecto len(arr) - 1)
        
    Complejidad:
        - Tiempo: O(n log n) promedio, O(n²) peor caso
        - Espacio: O(log n)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Obtener el índice del pivote después de la partición
        pivot_index = partition(arr, low, high)
        
        # Recursivamente ordenar los elementos antes y después del pivote
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
    """
    Función de partición para QuickSort in-place.
    
    Args:
        arr: Lista de números
        low: Índice inicial
        high: Índice final
        
    Returns:
        Índice del pivote
    """
    # Elegir el último elemento como pivote
    pivot = arr[high]
    
    # Índice del elemento más pequeño
    i = low - 1
    
    # Mover elementos menores que el pivote al lado izquierdo
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Colocar el pivote en su posición correcta
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1 