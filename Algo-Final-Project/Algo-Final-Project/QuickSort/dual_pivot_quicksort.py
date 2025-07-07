"""
Implementación de QuickSort con dos pivotes (Dual-Pivot QuickSort).
Más eficiente que el QuickSort tradicional.
"""

def quicksort_dual_pivot(arr, left=0, right=None):
    """
    Implementación de QuickSort con dos pivotes (Dual-Pivot QuickSort).
    Más eficiente que el QuickSort tradicional.
    
    Args:
        arr: Lista de números a ordenar
        left: Índice izquierdo
        right: Índice derecho
        
    Complejidad:
        - Tiempo: O(n log n) promedio, O(n²) peor caso
        - Espacio: O(log n)
        - Ventaja: Mejor rendimiento en la práctica que QuickSort tradicional
    """
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        # Asegurar que el primer pivote sea menor que el segundo
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        
        # Elegir dos pivotes
        pivot1, pivot2 = arr[left], arr[right]
        
        # Partición de tres vías
        less, great = partition_dual_pivot(arr, left, right, pivot1, pivot2)
        
        # Recursivamente ordenar las tres sublistas
        quicksort_dual_pivot(arr, left, less - 1)      # < pivot1
        quicksort_dual_pivot(arr, less + 1, great - 1) # entre pivot1 y pivot2
        quicksort_dual_pivot(arr, great + 1, right)    # > pivot2

def partition_dual_pivot(arr, left, right, pivot1, pivot2):
    """
    Partición para Dual-Pivot QuickSort.
    Divide el array en tres partes: < pivot1, entre pivot1 y pivot2, > pivot2
    
    Args:
        arr: Lista de números
        left: Índice izquierdo
        right: Índice derecho
        pivot1: Primer pivote (menor)
        pivot2: Segundo pivote (mayor)
    
    Returns:
        Tupla (less, great) donde:
        - less es el índice del último elemento < pivot1
        - great es el índice del primer elemento > pivot2
    """
    less = left + 1    # Índice del último elemento < pivot1
    great = right - 1  # Índice del primer elemento > pivot2
    k = left + 1       # Índice actual
    
    while k <= great:
        # Si el elemento actual es menor que pivot1
        if arr[k] < pivot1:
            arr[k], arr[less] = arr[less], arr[k]
            less += 1
        # Si el elemento actual es mayor que pivot2
        elif arr[k] > pivot2:
            # Encontrar el primer elemento <= pivot2 desde la derecha
            while k < great and arr[great] > pivot2:
                great -= 1
            arr[k], arr[great] = arr[great], arr[k]
            great -= 1
            
            # Verificar si el elemento intercambiado es menor que pivot1
            if arr[k] < pivot1:
                arr[k], arr[less] = arr[less], arr[k]
                less += 1
        # Si el elemento está entre pivot1 y pivot2, no hacer nada
        k += 1
    
    # Colocar los pivotes en sus posiciones finales
    arr[left], arr[less - 1] = arr[less - 1], arr[left]
    arr[right], arr[great + 1] = arr[great + 1], arr[right]
    
    return less - 1, great + 1 