"""
Demostración de todos los algoritmos de QuickSort implementados.
"""

from basic_quicksort import quicksort, quicksort_inplace
from three_way_quicksort import quicksort_3way
from dual_pivot_quicksort import quicksort_dual_pivot
from randomized_quicksort import quicksort_randomized, quicksort_median_of_three
from utils import (
    generar_array_aleatorio, generar_array_duplicados, 
    generar_array_ordenado, generar_array_inverso,
    comparar_algoritmos, verificar_ordenamiento, mostrar_array
)

def demo_basica():
    """Demostración básica de todos los algoritmos."""
    print("🚀 DEMOSTRACIÓN BÁSICA DE QUICKSORT")
    print("=" * 50)
    
    # Array de prueba
    numeros = [64, 34, 25, 12, 22, 11, 90, 25, 25, 34]
    print(f"Array original: {numeros}")
    
    # 1. QuickSort básico
    resultado1 = quicksort(numeros.copy())
    print(f"QuickSort básico: {resultado1}")
    
    # 2. QuickSort 3-way
    numeros2 = numeros.copy()
    quicksort_3way(numeros2)
    print(f"QuickSort 3-way: {numeros2}")
    
    # 3. Dual-Pivot QuickSort
    numeros3 = numeros.copy()
    quicksort_dual_pivot(numeros3)
    print(f"Dual-Pivot QuickSort: {numeros3}")
    
    # 4. QuickSort aleatorizado
    numeros4 = numeros.copy()
    quicksort_randomized(numeros4)
    print(f"QuickSort aleatorizado: {numeros4}")
    
    # 5. QuickSort mediana de tres
    numeros5 = numeros.copy()
    quicksort_median_of_three(numeros5)
    print(f"QuickSort mediana de tres: {numeros5}")

def demo_rendimiento():
    """Demostración de rendimiento comparativo."""
    print("\n⚡ DEMOSTRACIÓN DE RENDIMIENTO")
    print("=" * 50)
    
    # Definir algoritmos a comparar
    algoritmos = {
        "QuickSort básico": lambda arr: quicksort_inplace(arr),
        "QuickSort 3-way": quicksort_3way,
        "Dual-Pivot": quicksort_dual_pivot,
        "QuickSort aleatorio": quicksort_randomized,
        "Mediana de tres": quicksort_median_of_three
    }
    
    # Generar arrays de prueba
    arrays = {
        "Aleatorio (1000)": generar_array_aleatorio(1000),
        "Con duplicados (1000)": generar_array_duplicados(1000, 50),
        "Ordenado (1000)": generar_array_ordenado(1000),
        "Inverso (1000)": generar_array_inverso(1000)
    }
    
    # Comparar rendimiento
    comparar_algoritmos(algoritmos, arrays)

def demo_casos_especiales():
    """Demostración de casos especiales."""
    print("\n🎯 CASOS ESPECIALES")
    print("=" * 50)
    
    # Caso 1: Array vacío
    print("1. Array vacío:")
    arr_vacio = []
    resultado = quicksort(arr_vacio.copy())
    print(f"   Original: {arr_vacio}")
    print(f"   Ordenado: {resultado}")
    
    # Caso 2: Array con un elemento
    print("\n2. Array con un elemento:")
    arr_uno = [42]
    resultado = quicksort(arr_uno.copy())
    print(f"   Original: {arr_uno}")
    print(f"   Ordenado: {resultado}")
    
    # Caso 3: Array con todos elementos iguales
    print("\n3. Array con elementos iguales:")
    arr_iguales = [5, 5, 5, 5, 5]
    resultado = quicksort(arr_iguales.copy())
    print(f"   Original: {arr_iguales}")
    print(f"   Ordenado: {resultado}")
    
    # Caso 4: Array ya ordenado
    print("\n4. Array ya ordenado:")
    arr_ordenado = [1, 2, 3, 4, 5]
    resultado = quicksort(arr_ordenado.copy())
    print(f"   Original: {arr_ordenado}")
    print(f"   Ordenado: {resultado}")

def demo_verificacion():
    """Demostración de verificación de ordenamiento."""
    print("\n✅ VERIFICACIÓN DE ORDENAMIENTO")
    print("=" * 50)
    
    # Array desordenado
    arr_desordenado = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Array desordenado: {arr_desordenado}")
    print(f"¿Está ordenado? {verificar_ordenamiento(arr_desordenado)}")
    
    # Ordenar y verificar
    quicksort_inplace(arr_desordenado)
    print(f"Array ordenado: {arr_desordenado}")
    print(f"¿Está ordenado? {verificar_ordenamiento(arr_desordenado)}")

def main():
    """Función principal de demostración."""
    print("🎉 BIENVENIDO A LA DEMOSTRACIÓN DE QUICKSORT")
    print("=" * 60)
    
    try:
        # Ejecutar todas las demostraciones
        demo_basica()
        demo_rendimiento()
        demo_casos_especiales()
        demo_verificacion()
        
        print("\n🎊 ¡Demostración completada exitosamente!")
        
    except Exception as e:
        print(f"\n❌ Error durante la demostración: {e}")

if __name__ == "__main__":
    main() 