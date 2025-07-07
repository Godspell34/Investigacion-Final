"""
Implementación de QuickSort con partición de 3 vías.
Ideal para arrays con muchos elementos duplicados.
"""

def quicksort_3way(arr, low=0, high=None):
    """
    Implementación de QuickSort con partición de 3 vías.
    Eficiente para arrays con muchos elementos duplicados.
    
    Args:
        arr: Lista de números a ordenar
        low: Índice inicial
        high: Índice final
        
    Complejidad:
        - Tiempo: O(n log n) promedio, O(n²) peor caso
        - Espacio: O(log n)
        - Ventaja: Muy eficiente con muchos duplicados
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partición de 3 vías
        lt, gt = partition_3way(arr, low, high)
        
        # Recursivamente ordenar las sublistas
        quicksort_3way(arr, low, lt - 1)
        quicksort_3way(arr, gt + 1, high)

def partition_3way(arr, low, high):
    """
    Partición de 3 vías para QuickSort.
    Divide el array en tres partes: < pivot, = pivot, > pivot
    
    Args:
        arr: Lista de números
        low: Índice inicial
        high: Índice final
    
    Returns:
        Tupla (lt, gt) donde:
        - lt es el índice del último elemento < pivot
        - gt es el índice del primer elemento > pivot
    """
    pivot = arr[low]  # Elegir el primer elemento como pivote
    lt = low          # lt = less than (menor que)
    gt = high         # gt = greater than (mayor que)
    i = low + 1       # i = current element (elemento actual)
    
    while i <= gt:
        if arr[i] < pivot:
            # Elemento menor que el pivote
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            # Elemento mayor que el pivote
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            # Elemento igual al pivote
            i += 1
    
    return lt, gt 