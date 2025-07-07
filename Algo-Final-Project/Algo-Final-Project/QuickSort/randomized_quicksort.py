"""
Implementación de QuickSort con selección aleatoria del pivote.
Mejora el rendimiento en el peor caso.
"""

import random

def quicksort_randomized(arr, low=0, high=None):
    """
    QuickSort con selección aleatoria del pivote.
    Mejora el rendimiento en el peor caso.
    
    Args:
        arr: Lista de números a ordenar
        low: Índice inicial
        high: Índice final
        
    Complejidad:
        - Tiempo: O(n log n) promedio, O(n²) peor caso (pero menos probable)
        - Espacio: O(log n)
        - Ventaja: Evita el peor caso en arrays ya ordenados
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Seleccionar pivote aleatorio
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        
        # Partición estándar
        pivot_index = partition_randomized(arr, low, high)
        
        # Recursivamente ordenar
        quicksort_randomized(arr, low, pivot_index - 1)
        quicksort_randomized(arr, pivot_index + 1, high)

def partition_randomized(arr, low, high):
    """
    Partición estándar para QuickSort aleatorizado.
    
    Args:
        arr: Lista de números
        low: Índice inicial
        high: Índice final
        
    Returns:
        Índice del pivote
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_median_of_three(arr, low=0, high=None):
    """
    QuickSort con selección del pivote usando la mediana de tres elementos.
    Mejora la selección del pivote para evitar casos degenerados.
    
    Args:
        arr: Lista de números a ordenar
        low: Índice inicial
        high: Índice final
        
    Complejidad:
        - Tiempo: O(n log n) promedio
        - Espacio: O(log n)
        - Ventaja: Mejor selección del pivote que selección aleatoria
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Seleccionar pivote usando mediana de tres
        pivot_index = median_of_three(arr, low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        
        # Partición estándar
        pivot_index = partition_randomized(arr, low, high)
        
        # Recursivamente ordenar
        quicksort_median_of_three(arr, low, pivot_index - 1)
        quicksort_median_of_three(arr, pivot_index + 1, high)

def median_of_three(arr, low, high):
    """
    Selecciona el pivote usando la mediana de tres elementos.
    
    Args:
        arr: Lista de números
        low: Índice inicial
        high: Índice final
        
    Returns:
        Índice del elemento mediano
    """
    mid = (low + high) // 2
    
    # Ordenar los tres elementos
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    # Intercambiar el mediano con el penúltimo elemento
    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
    
    return high - 1 