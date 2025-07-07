"""
Utilidades para los algoritmos de QuickSort.
Incluye funciones de comparación de rendimiento y visualización.
"""

import time
import random
from typing import List, Callable

def generar_array_aleatorio(tamano: int, min_val: int = 1, max_val: int = 1000) -> List[int]:
    """
    Genera un array aleatorio para pruebas.
    
    Args:
        tamano: Tamaño del array
        min_val: Valor mínimo
        max_val: Valor máximo
        
    Returns:
        Lista de números aleatorios
    """
    return [random.randint(min_val, max_val) for _ in range(tamano)]

def generar_array_duplicados(tamano: int, valores_unicos: int = 10) -> List[int]:
    """
    Genera un array con muchos elementos duplicados.
    
    Args:
        tamano: Tamaño del array
        valores_unicos: Número de valores únicos diferentes
        
    Returns:
        Lista con muchos duplicados
    """
    valores = list(range(1, valores_unicos + 1))
    return [random.choice(valores) for _ in range(tamano)]

def generar_array_ordenado(tamano: int) -> List[int]:
    """
    Genera un array ya ordenado.
    
    Args:
        tamano: Tamaño del array
        
    Returns:
        Lista ordenada
    """
    return list(range(1, tamano + 1))

def generar_array_inverso(tamano: int) -> List[int]:
    """
    Genera un array ordenado de forma inversa.
    
    Args:
        tamano: Tamaño del array
        
    Returns:
        Lista ordenada de forma inversa
    """
    return list(range(tamano, 0, -1))

def medir_tiempo(func: Callable, arr: List[int], *args, **kwargs) -> float:
    """
    Mide el tiempo de ejecución de una función.
    
    Args:
        func: Función a medir
        arr: Array de entrada
        *args, **kwargs: Argumentos adicionales para la función
        
    Returns:
        Tiempo de ejecución en segundos
    """
    # Crear una copia del array para no modificar el original
    arr_copia = arr.copy()
    
    inicio = time.time()
    func(arr_copia, *args, **kwargs)
    fin = time.time()
    
    return fin - inicio

def comparar_algoritmos(algoritmos: dict, arrays: dict, repeticiones: int = 3):
    """
    Compara el rendimiento de diferentes algoritmos de ordenamiento.
    
    Args:
        algoritmos: Diccionario con nombre y función del algoritmo
        arrays: Diccionario con nombre y array de prueba
        repeticiones: Número de repeticiones para promediar
    """
    print("=" * 60)
    print("COMPARACIÓN DE RENDIMIENTO - ALGORITMOS QUICKSORT")
    print("=" * 60)
    
    for nombre_array, array in arrays.items():
        print(f"\n📊 Array: {nombre_array} (tamaño: {len(array)})")
        print("-" * 40)
        
        tiempos = {}
        
        for nombre_algo, funcion in algoritmos.items():
            tiempo_total = 0
            for _ in range(repeticiones):
                tiempo = medir_tiempo(funcion, array)
                tiempo_total += tiempo
            
            tiempo_promedio = tiempo_total / repeticiones
            tiempos[nombre_algo] = tiempo_promedio
            
            print(f"{nombre_algo:20} | {tiempo_promedio:.6f} segundos")
        
        # Encontrar el más rápido
        mas_rapido = min(tiempos, key=tiempos.get)
        print(f"\n🏆 Más rápido: {mas_rapido}")

def verificar_ordenamiento(arr: List[int]) -> bool:
    """
    Verifica si un array está ordenado correctamente.
    
    Args:
        arr: Array a verificar
        
    Returns:
        True si está ordenado, False en caso contrario
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def mostrar_array(arr: List[int], max_elementos: int = 20):
    """
    Muestra un array de forma legible.
    
    Args:
        arr: Array a mostrar
        max_elementos: Máximo número de elementos a mostrar
    """
    if len(arr) <= max_elementos:
        print(f"[{', '.join(map(str, arr))}]")
    else:
        primeros = arr[:max_elementos//2]
        ultimos = arr[-max_elementos//2:]
        print(f"[{', '.join(map(str, primeros))}, ..., {', '.join(map(str, ultimos))}]")
    print(f"Tamaño: {len(arr)}") 