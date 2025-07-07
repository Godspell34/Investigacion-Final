"""
Utilidades para los algoritmos de búsqueda binaria.
Incluye funciones de generación de datos y comparación de rendimiento.
"""

import time
import random
from typing import List, Callable, Tuple

def generar_array_ordenado(tamano: int, min_val: int = 1, max_val: int = 1000) -> List[int]:
    """
    Genera un array ordenado para pruebas.
    
    Args:
        tamano: Tamaño del array
        min_val: Valor mínimo
        max_val: Valor máximo
        
    Returns:
        Lista ordenada de números
    """
    return sorted([random.randint(min_val, max_val) for _ in range(tamano)])

def generar_array_con_duplicados(tamano: int, valores_unicos: int = 10) -> List[int]:
    """
    Genera un array ordenado con elementos duplicados.
    
    Args:
        tamano: Tamaño del array
        valores_unicos: Número de valores únicos diferentes
        
    Returns:
        Lista ordenada con duplicados
    """
    valores = list(range(1, valores_unicos + 1))
    array = [random.choice(valores) for _ in range(tamano)]
    return sorted(array)

def generar_array_rotado(tamano: int, rotaciones: int = None) -> List[int]:
    """
    Genera un array ordenado y luego lo rota.
    
    Args:
        tamano: Tamaño del array
        rotaciones: Número de rotaciones (aleatorio si es None)
        
    Returns:
        Array ordenado y rotado
    """
    array = list(range(1, tamano + 1))
    
    if rotaciones is None:
        rotaciones = random.randint(1, tamano - 1)
    
    return array[rotaciones:] + array[:rotaciones]

def generar_matriz_2d_ordenada(filas: int, columnas: int) -> List[List[int]]:
    """
    Genera una matriz 2D ordenada.
    
    Args:
        filas: Número de filas
        columnas: Número de columnas
        
    Returns:
        Matriz 2D ordenada
    """
    matriz = []
    valor = 1
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(valor)
            valor += 1
        matriz.append(fila)
    
    return matriz

def medir_tiempo(func: Callable, *args, **kwargs) -> float:
    """
    Mide el tiempo de ejecución de una función.
    
    Args:
        func: Función a medir
        *args, **kwargs: Argumentos para la función
        
    Returns:
        Tiempo de ejecución en segundos
    """
    inicio = time.time()
    resultado = func(*args, **kwargs)
    fin = time.time()
    
    return fin - inicio

def comparar_busquedas_binarias(algoritmos: dict, arrays: dict, objetivos: List[int], repeticiones: int = 3):
    """
    Compara el rendimiento de diferentes algoritmos de búsqueda binaria.
    
    Args:
        algoritmos: Diccionario con nombre y función del algoritmo
        arrays: Diccionario con nombre y array de prueba
        objetivos: Lista de valores a buscar
        repeticiones: Número de repeticiones para promediar
    """
    print("=" * 70)
    print("COMPARACIÓN DE RENDIMIENTO - BÚSQUEDAS BINARIAS")
    print("=" * 70)
    
    for nombre_array, array in arrays.items():
        print(f"\n📊 Array: {nombre_array} (tamaño: {len(array)})")
        print("-" * 50)
        
        for objetivo in objetivos:
            print(f"\n🎯 Buscando: {objetivo}")
            
            tiempos = {}
            resultados = {}
            
            for nombre_algo, funcion in algoritmos.items():
                tiempo_total = 0
                resultado_final = None
                
                for _ in range(repeticiones):
                    tiempo = medir_tiempo(funcion, array, objetivo)
                    tiempo_total += tiempo
                    
                    if resultado_final is None:
                        resultado_final = funcion(array, objetivo)
                
                tiempo_promedio = tiempo_total / repeticiones
                tiempos[nombre_algo] = tiempo_promedio
                resultados[nombre_algo] = resultado_final
                
                print(f"  {nombre_algo:25} | {tiempo_promedio:.8f}s | Resultado: {resultado_final}")
            
            # Encontrar el más rápido
            if tiempos:
                mas_rapido = min(tiempos, key=tiempos.get)
                print(f"  🏆 Más rápido: {mas_rapido}")

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

def mostrar_matriz(matriz: List[List[int]], max_filas: int = 5, max_cols: int = 10):
    """
    Muestra una matriz de forma legible.
    
    Args:
        matriz: Matriz a mostrar
        max_filas: Máximo número de filas a mostrar
        max_cols: Máximo número de columnas a mostrar
    """
    if not matriz:
        print("Matriz vacía")
        return
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    print(f"Matriz {filas}x{columnas}:")
    
    for i in range(min(filas, max_filas)):
        fila = matriz[i]
        if columnas <= max_cols:
            print(f"  [{', '.join(map(str, fila))}]")
        else:
            primeros = fila[:max_cols//2]
            ultimos = fila[-max_cols//2:]
            print(f"  [{', '.join(map(str, primeros))}, ..., {', '.join(map(str, ultimos))}]")
    
    if filas > max_filas:
        print(f"  ... ({filas - max_filas} filas más)")

def generar_casos_prueba_busqueda():
    """
    Genera casos de prueba típicos para búsqueda binaria.
    
    Returns:
        Diccionario con arrays de prueba y objetivos
    """
    casos = {
        "arrays": {
            "Pequeño (10)": generar_array_ordenado(10),
            "Mediano (100)": generar_array_ordenado(100),
            "Grande (1000)": generar_array_ordenado(1000),
            "Con duplicados": generar_array_con_duplicados(100, 20),
            "Rotado": generar_array_rotado(20, 7)
        },
        "objetivos": [
            # Objetivos que existen
            5, 25, 50, 75, 95,
            # Objetivos que no existen
            0, 1000, 9999,
            # Objetivos en los extremos
            1, 100
        ]
    }
    
    return casos

def test_busqueda_binaria_basica():
    """
    Prueba básica de búsqueda binaria.
    """
    print("🧪 PRUEBA BÁSICA DE BÚSQUEDA BINARIA")
    print("=" * 40)
    
    # Array de prueba
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"Array: {arr}")
    
    # Casos de prueba
    casos_prueba = [1, 5, 10, 15, 19, 0, 20]
    
    for objetivo in casos_prueba:
        resultado = busqueda_binaria(arr, objetivo)
        if resultado != -1:
            print(f"✅ {objetivo} encontrado en índice {resultado}")
        else:
            print(f"❌ {objetivo} no encontrado")

# Importar función de búsqueda binaria para las pruebas
from .basic_binary_search import busqueda_binaria 