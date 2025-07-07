"""
Comparación de rendimiento: Arrays vs Listas Enlazadas
Demuestra por qué las listas enlazadas son ineficientes para búsqueda binaria.
"""

import time
import random
from linked_list_binary_search import (
    ListaEnlazada,
    busqueda_binaria_lista_enlazada,
    crear_lista_enlazada_desde_array
)
from basic_binary_search import busqueda_binaria

def comparar_acceso_por_indice():
    """Compara el acceso por índice entre arrays y listas enlazadas."""
    print("🔢 COMPARACIÓN: ACCESO POR ÍNDICE")
    print("=" * 50)
    
    # Crear estructuras de datos
    tamanio = 10000
    arr = list(range(tamanio))
    lista = crear_lista_enlazada_desde_array(arr)
    
    # Índices a probar
    indices = [0, 100, 1000, 5000, 9999]
    
    print(f"Tamaño de la estructura: {tamanio}")
    print("\nAcceso por índice:")
    
    for indice in indices:
        # Array Python
        inicio = time.time()
        elemento_array = arr[indice]
        tiempo_array = time.time() - inicio
        
        # Lista Enlazada
        inicio = time.time()
        nodo_lista = lista.obtener_nodo_en_indice(indice)
        tiempo_lista = time.time() - inicio
        
        print(f"  Índice {indice:4}: Array={tiempo_array:.8f}s, Lista={tiempo_lista:.8f}s, "
              f"Ratio={tiempo_lista/tiempo_array:.0f}x más lento")

def comparar_busqueda_binaria():
    """Compara búsqueda binaria entre arrays y listas enlazadas."""
    print("\n🔍 COMPARACIÓN: BÚSQUEDA BINARIA")
    print("=" * 50)
    
    # Crear estructuras de datos
    tamanio = 10000
    arr = list(range(tamanio))
    lista = crear_lista_enlazada_desde_array(arr)
    
    # Objetivos a buscar
    objetivos = [0, 100, 1000, 5000, 9999, 15000]  # Algunos no existen
    
    print(f"Tamaño de la estructura: {tamanio}")
    print("\nBúsqueda binaria:")
    
    for objetivo in objetivos:
        # Array Python
        inicio = time.time()
        resultado_array = busqueda_binaria(arr, objetivo)
        tiempo_array = time.time() - inicio
        
        # Lista Enlazada
        inicio = time.time()
        resultado_lista = busqueda_binaria_lista_enlazada(lista, objetivo)
        tiempo_lista = time.time() - inicio
        
        print(f"  Objetivo {objetivo:5}: Array={tiempo_array:.8f}s, Lista={tiempo_lista:.8f}s, "
              f"Ratio={tiempo_lista/tiempo_array:.0f}x más lento")

def comparar_escalabilidad():
    """Compara cómo escalan las estructuras con diferentes tamaños."""
    print("\n📈 COMPARACIÓN: ESCALABILIDAD")
    print("=" * 50)
    
    tamanios = [100, 1000, 10000, 50000]
    
    print("Tamaño | Array (s) | Lista (s) | Ratio")
    print("-" * 40)
    
    for tamanio in tamanios:
        # Crear estructuras
        arr = list(range(tamanio))
        lista = crear_lista_enlazada_desde_array(arr)
        
        # Buscar elemento en el medio
        objetivo = tamanio // 2
        
        # Medir array
        inicio = time.time()
        busqueda_binaria(arr, objetivo)
        tiempo_array = time.time() - inicio
        
        # Medir lista enlazada
        inicio = time.time()
        busqueda_binaria_lista_enlazada(lista, objetivo)
        tiempo_lista = time.time() - inicio
        
        ratio = tiempo_lista / tiempo_array if tiempo_array > 0 else float('inf')
        
        print(f"{tamanio:6} | {tiempo_array:.6f} | {tiempo_lista:.6f} | {ratio:.0f}x")

def comparar_busqueda_lineal_vs_binaria():
    """Compara búsqueda lineal vs binaria en listas enlazadas."""
    print("\n⚡ COMPARACIÓN: LINEAL vs BINARIA en Listas Enlazadas")
    print("=" * 60)
    
    tamanios = [100, 1000, 10000]
    
    for tamanio in tamanios:
        print(f"\nTamaño: {tamanio}")
        print("-" * 30)
        
        # Crear lista enlazada
        arr = list(range(tamanio))
        lista = crear_lista_enlazada_desde_array(arr)
        
        # Buscar elemento al final
        objetivo = tamanio - 1
        
        # Búsqueda lineal
        inicio = time.time()
        actual = lista.cabeza
        while actual and actual.valor != objetivo:
            actual = actual.siguiente
        tiempo_lineal = time.time() - inicio
        
        # Búsqueda binaria (simulada)
        inicio = time.time()
        busqueda_binaria_lista_enlazada(lista, objetivo)
        tiempo_binaria = time.time() - inicio
        
        print(f"  Búsqueda lineal: {tiempo_lineal:.6f}s")
        print(f"  Búsqueda binaria: {tiempo_binaria:.6f}s")
        print(f"  ¿Cuál es más rápida? {'LINEAL' if tiempo_lineal < tiempo_binaria else 'BINARIA'}")

def analizar_por_que_son_malas():
    """Explica por qué las listas enlazadas son malas para búsqueda binaria."""
    print("\n🤔 ¿POR QUÉ LAS LISTAS ENLAZADAS SON 'MALAS'?")
    print("=" * 60)
    
    print("1. 🐌 ACCESO POR ÍNDICE:")
    print("   - Array: O(1) - Acceso directo")
    print("   - Lista Enlazada: O(n) - Debe recorrer nodos")
    print("   - Impacto: La búsqueda binaria pierde su ventaja O(log n)")
    
    print("\n2. 💾 LOCALIDAD DE CACHE:")
    print("   - Array: Datos contiguos en memoria")
    print("   - Lista Enlazada: Datos dispersos, saltos de memoria")
    print("   - Impacto: Mucho más lento en la práctica")
    
    print("\n3. 🔗 OVERHEAD DE PUNTEROS:")
    print("   - Array: Solo datos")
    print("   - Lista Enlazada: Datos + punteros + fragmentación")
    print("   - Impacto: Más memoria y más lento")
    
    print("\n4. 📊 COMPLEJIDAD REAL:")
    print("   - Búsqueda binaria en array: O(log n)")
    print("   - Búsqueda binaria en lista enlazada: O(n)")
    print("   - Búsqueda lineal en lista enlazada: O(n)")
    print("   - Conclusión: ¡No hay ventaja!")

def recomendaciones():
    """Proporciona recomendaciones sobre cuándo usar cada estructura."""
    print("\n💡 RECOMENDACIONES")
    print("=" * 40)
    
    print("✅ USAR ARRAYS (Listas de Python) PARA:")
    print("   - Búsqueda binaria")
    print("   - Acceso frecuente por índice")
    print("   - Algoritmos que requieren acceso aleatorio")
    print("   - Cuando el tamaño es conocido")
    
    print("\n✅ USAR LISTAS ENLAZADAS PARA:")
    print("   - Inserción/eliminación frecuente al inicio")
    print("   - Tamaño dinámico desconocido")
    print("   - Implementación de pilas/colas")
    print("   - Cuando la memoria es muy limitada")
    
    print("\n❌ NO USAR LISTAS ENLAZADAS PARA:")
    print("   - Búsqueda binaria")
    print("   - Acceso frecuente por índice")
    print("   - Algoritmos que requieren acceso aleatorio")

def main():
    """Función principal de comparación."""
    print("🎯 COMPARACIÓN: ARRAYS vs LISTAS ENLAZADAS")
    print("=" * 60)
    print("Demostrando por qué las listas enlazadas son ineficientes")
    print("para búsqueda binaria comparadas con arrays normales.")
    print("=" * 60)
    
    try:
        comparar_acceso_por_indice()
        comparar_busqueda_binaria()
        comparar_escalabilidad()
        comparar_busqueda_lineal_vs_binaria()
        analizar_por_que_son_malas()
        recomendaciones()
        
        print("\n🎊 ¡Análisis completado!")
        
    except Exception as e:
        print(f"\n❌ Error durante la comparación: {e}")

if __name__ == "__main__":
    main() 