"""
Demostración de búsqueda binaria en listas enlazadas.
"""

from linked_list_binary_search import (
    ListaEnlazada,
    busqueda_binaria_lista_enlazada,
    busqueda_binaria_lista_enlazada_optimizada,
    busqueda_binaria_lista_enlazada_con_salto,
    busqueda_binaria_lista_enlazada_con_comparaciones,
    crear_lista_enlazada_desde_array,
    comparar_busquedas_lista_enlazada
)
import time
import random

def demo_basica_lista_enlazada():
    """Demostración básica de búsqueda binaria en lista enlazada."""
    print("🚀 DEMOSTRACIÓN BÁSICA - BÚSQUEDA BINARIA EN LISTA ENLAZADA")
    print("=" * 60)
    
    # Crear lista enlazada desde un array
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    lista = crear_lista_enlazada_desde_array(arr)
    
    print(f"Lista enlazada: {lista.mostrar_lista()}")
    print(f"Tamaño: {lista.obtener_tamanio()}")
    
    # Buscar elementos
    objetivos = [7, 15, 20, 1, 19]
    
    for objetivo in objetivos:
        print(f"\n🎯 Buscando: {objetivo}")
        
        # Método 1: Búsqueda binaria con índice
        resultado1 = busqueda_binaria_lista_enlazada(lista, objetivo)
        print(f"  Búsqueda binaria (índice): {resultado1.valor if resultado1 else 'No encontrado'}")
        
        # Método 2: Búsqueda binaria optimizada
        resultado2 = busqueda_binaria_lista_enlazada_optimizada(lista, objetivo)
        print(f"  Búsqueda binaria (optimizada): {resultado2.valor if resultado2 else 'No encontrado'}")
        
        # Método 3: Búsqueda binaria con saltos
        resultado3 = busqueda_binaria_lista_enlazada_con_salto(lista, objetivo)
        print(f"  Búsqueda binaria (saltos): {resultado3.valor if resultado3 else 'No encontrado'}")

def demo_comparacion_completa():
    """Demostración de comparación completa entre métodos."""
    print("\n⚡ COMPARACIÓN COMPLETA DE MÉTODOS")
    print("=" * 60)
    
    # Crear lista enlazada más grande
    arr = list(range(1, 21))  # 1 a 20
    lista = crear_lista_enlazada_desde_array(arr)
    
    print(f"Lista enlazada: {lista.mostrar_lista()}")
    
    # Buscar elementos existentes y no existentes
    objetivos = [5, 10, 15, 25, 0]
    
    for objetivo in objetivos:
        print(f"\n🎯 Buscando: {objetivo}")
        comparar_busquedas_lista_enlazada(lista, objetivo)

def demo_rendimiento_lista_enlazada():
    """Demostración de rendimiento comparativo."""
    print("\n📊 ANÁLISIS DE RENDIMIENTO")
    print("=" * 60)
    
    # Crear listas de diferentes tamaños
    tamanios = [10, 50, 100, 500]
    
    for tamanio in tamanios:
        print(f"\n📈 Lista de tamaño {tamanio}")
        print("-" * 40)
        
        # Generar array aleatorio
        arr = sorted([random.randint(1, tamanio * 10) for _ in range(tamanio)])
        lista = crear_lista_enlazada_desde_array(arr)
        
        # Seleccionar objetivo aleatorio
        objetivo = random.choice(arr)
        
        # Medir tiempos
        tiempos = {}
        
        # Método 1: Búsqueda binaria con índice
        inicio = time.time()
        for _ in range(100):  # Repetir para obtener tiempo significativo
            busqueda_binaria_lista_enlazada(lista, objetivo)
        fin = time.time()
        tiempos["Búsqueda binaria (índice)"] = (fin - inicio) / 100
        
        # Método 2: Búsqueda binaria optimizada
        inicio = time.time()
        for _ in range(100):
            busqueda_binaria_lista_enlazada_optimizada(lista, objetivo)
        fin = time.time()
        tiempos["Búsqueda binaria (optimizada)"] = (fin - inicio) / 100
        
        # Método 3: Búsqueda binaria con saltos
        inicio = time.time()
        for _ in range(100):
            busqueda_binaria_lista_enlazada_con_salto(lista, objetivo)
        fin = time.time()
        tiempos["Búsqueda binaria (saltos)"] = (fin - inicio) / 100
        
        # Mostrar resultados
        for metodo, tiempo in tiempos.items():
            print(f"  {metodo:30} | {tiempo:.8f} segundos")
        
        # Encontrar el más rápido
        mas_rapido = min(tiempos, key=tiempos.get)
        print(f"  🏆 Más rápido: {mas_rapido}")

def demo_casos_especiales_lista_enlazada():
    """Demostración de casos especiales."""
    print("\n🎭 CASOS ESPECIALES")
    print("=" * 60)
    
    # Caso 1: Lista vacía
    print("1. Lista vacía:")
    lista_vacia = ListaEnlazada()
    resultado = busqueda_binaria_lista_enlazada(lista_vacia, 5)
    print(f"   Resultado: {resultado}")
    
    # Caso 2: Lista con un elemento
    print("\n2. Lista con un elemento:")
    lista_uno = ListaEnlazada()
    lista_uno.insertar_ordenado(42)
    resultado = busqueda_binaria_lista_enlazada(lista_uno, 42)
    print(f"   Buscando 42: {resultado.valor if resultado else 'No encontrado'}")
    resultado = busqueda_binaria_lista_enlazada(lista_uno, 10)
    print(f"   Buscando 10: {resultado.valor if resultado else 'No encontrado'}")
    
    # Caso 3: Lista con elementos iguales
    print("\n3. Lista con elementos iguales:")
    lista_iguales = ListaEnlazada()
    for _ in range(5):
        lista_iguales.insertar_ordenado(5)
    print(f"   Lista: {lista_iguales.mostrar_lista()}")
    resultado = busqueda_binaria_lista_enlazada(lista_iguales, 5)
    print(f"   Buscando 5: {resultado.valor if resultado else 'No encontrado'}")

def demo_insercion_ordenada():
    """Demostración de inserción ordenada en lista enlazada."""
    print("\n📝 INSERCIÓN ORDENADA")
    print("=" * 60)
    
    lista = ListaEnlazada()
    valores = [15, 7, 23, 3, 11, 19, 5, 9]
    
    print("Insertando valores en orden:")
    for valor in valores:
        lista.insertar_ordenado(valor)
        print(f"  Después de insertar {valor}: {lista.mostrar_lista()}")
    
    print(f"\nLista final ordenada: {lista.mostrar_lista()}")
    print(f"Tamaño: {lista.obtener_tamanio()}")

def demo_acceso_por_indice():
    """Demostración de acceso por índice en lista enlazada."""
    print("\n🔢 ACCESO POR ÍNDICE")
    print("=" * 60)
    
    # Crear lista enlazada
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    lista = crear_lista_enlazada_desde_array(arr)
    
    print(f"Lista: {lista.mostrar_lista()}")
    print(f"Tamaño: {lista.obtener_tamanio()}")
    
    # Acceder a diferentes índices
    indices = [0, 2, 4, 6, 7, 10]
    
    for indice in indices:
        nodo = lista.obtener_nodo_en_indice(indice)
        if nodo:
            print(f"  Índice {indice}: {nodo.valor}")
        else:
            print(f"  Índice {indice}: No existe")

def main():
    """Función principal de demostración."""
    print("🎉 BIENVENIDO A LA DEMOSTRACIÓN DE BÚSQUEDA BINARIA EN LISTAS ENLAZADAS")
    print("=" * 70)
    
    try:
        # Ejecutar todas las demostraciones
        demo_basica_lista_enlazada()
        demo_comparacion_completa()
        demo_rendimiento_lista_enlazada()
        demo_casos_especiales_lista_enlazada()
        demo_insercion_ordenada()
        demo_acceso_por_indice()
        
    except Exception as e:
        print(f"\n❌ Error durante la demostración: {e}")

if __name__ == "__main__":
    main() 