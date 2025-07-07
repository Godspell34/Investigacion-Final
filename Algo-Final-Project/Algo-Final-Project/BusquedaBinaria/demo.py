"""
Demostración de todos los algoritmos de búsqueda binaria implementados.
"""

from basic_binary_search import (
    busqueda_binaria, busqueda_binaria_recursiva,
    busqueda_binaria_con_comparaciones, busqueda_binaria_con_trazado
)
from variants_binary_search import (
    busqueda_binaria_primera_ocurrencia, busqueda_binaria_ultima_ocurrencia,
    busqueda_binaria_menor_mayor_igual, busqueda_binaria_mayor_menor_igual,
    contar_ocurrencias, busqueda_binaria_rango, busqueda_binaria_floor_ceil
)
from advanced_binary_search import (
    busqueda_binaria_rotated_array, encontrar_punto_rotacion,
    busqueda_binaria_2d, busqueda_binaria_aproximada,
    busqueda_binaria_raiz_cuadrada, busqueda_binaria_potencia
)
from utils import (
    generar_array_ordenado, generar_array_con_duplicados,
    generar_array_rotado, generar_matriz_2d_ordenada,
    comparar_busquedas_binarias, mostrar_array, mostrar_matriz,
    generar_casos_prueba_busqueda, test_busqueda_binaria_basica
)

def demo_basica():
    """Demostración básica de búsqueda binaria."""
    print("🚀 DEMOSTRACIÓN BÁSICA DE BÚSQUEDA BINARIA")
    print("=" * 50)
    
    # Array de prueba
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    objetivo = 11
    
    print(f"Array: {arr}")
    print(f"Buscando: {objetivo}")
    
    # 1. Búsqueda binaria iterativa
    resultado1 = busqueda_binaria(arr, objetivo)
    print(f"Búsqueda binaria iterativa: {resultado1}")
    
    # 2. Búsqueda binaria recursiva
    resultado2 = busqueda_binaria_recursiva(arr, objetivo)
    print(f"Búsqueda binaria recursiva: {resultado2}")
    
    # 3. Con comparaciones
    resultado3, comparaciones = busqueda_binaria_con_comparaciones(arr, objetivo)
    print(f"Con comparaciones: índice {resultado3}, comparaciones {comparaciones}")

def demo_variantes():
    """Demostración de variantes de búsqueda binaria."""
    print("\n🎯 VARIANTES DE BÚSQUEDA BINARIA")
    print("=" * 50)
    
    # Array con duplicados
    arr = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7]
    objetivo = 2
    
    print(f"Array con duplicados: {arr}")
    print(f"Buscando: {objetivo}")
    
    # Primera ocurrencia
    primera = busqueda_binaria_primera_ocurrencia(arr, objetivo)
    print(f"Primera ocurrencia: {primera}")
    
    # Última ocurrencia
    ultima = busqueda_binaria_ultima_ocurrencia(arr, objetivo)
    print(f"Última ocurrencia: {ultima}")
    
    # Contar ocurrencias
    count = contar_ocurrencias(arr, objetivo)
    print(f"Total de ocurrencias: {count}")
    
    # Floor y Ceil
    objetivo_floor_ceil = 3.5
    floor, ceil = busqueda_binaria_floor_ceil(arr, objetivo_floor_ceil)
    print(f"Floor y Ceil de {objetivo_floor_ceil}: floor={floor}, ceil={ceil}")

def demo_arrays_rotados():
    """Demostración de búsqueda en arrays rotados."""
    print("\n🔄 BÚSQUEDA EN ARRAYS ROTADOS")
    print("=" * 50)
    
    # Array rotado
    arr_original = list(range(1, 11))
    arr_rotado = generar_array_rotado(10, 3)
    
    print(f"Array original: {arr_original}")
    print(f"Array rotado: {arr_rotado}")
    
    # Encontrar punto de rotación
    punto_rotacion = encontrar_punto_rotacion(arr_rotado)
    print(f"Punto de rotación: {punto_rotacion}")
    
    # Búsqueda en array rotado
    objetivo = 7
    resultado = busqueda_binaria_rotated_array(arr_rotado, objetivo)
    print(f"Buscando {objetivo} en array rotado: {resultado}")

def demo_matrices_2d():
    """Demostración de búsqueda en matrices 2D."""
    print("\n📊 BÚSQUEDA EN MATRICES 2D")
    print("=" * 50)
    
    # Generar matriz 2D ordenada
    matriz = generar_matriz_2d_ordenada(5, 6)
    mostrar_matriz(matriz)
    
    # Búsqueda en matriz 2D
    objetivo = 15
    resultado = busqueda_binaria_2d(matriz, objetivo)
    print(f"Buscando {objetivo}: {resultado}")
    
    if resultado != (-1, -1):
        fila, col = resultado
        print(f"Encontrado en posición ({fila}, {col}) = {matriz[fila][col]}")

def demo_busqueda_aproximada():
    """Demostración de búsqueda aproximada."""
    print("\n🎯 BÚSQUEDA APROXIMADA")
    print("=" * 50)
    
    # Array con números decimales
    arr = [1.1, 2.3, 3.5, 4.7, 5.9, 7.1, 8.3, 9.5]
    objetivo = 6.0
    
    print(f"Array: {arr}")
    print(f"Buscando aproximación de: {objetivo}")
    
    indice, valor, diferencia = busqueda_binaria_aproximada(arr, objetivo)
    print(f"Resultado: índice={indice}, valor={valor}, diferencia={diferencia}")

def demo_calculos_matematicos():
    """Demostración de cálculos matemáticos con búsqueda binaria."""
    print("\n🧮 CÁLCULOS MATEMÁTICOS")
    print("=" * 50)
    
    # Raíz cuadrada
    numero = 25
    raiz = busqueda_binaria_raiz_cuadrada(numero)
    print(f"Raíz cuadrada de {numero}: {raiz}")
    print(f"Verificación: {raiz}² = {raiz * raiz}")
    
    # Raíz cúbica
    numero_cubo = 27
    raiz_cubo = busqueda_binaria_potencia(numero_cubo, 3)
    print(f"Raíz cúbica de {numero_cubo}: {raiz_cubo}")
    print(f"Verificación: {raiz_cubo}³ = {raiz_cubo ** 3}")

def demo_rendimiento():
    """Demostración de rendimiento comparativo."""
    print("\n⚡ COMPARACIÓN DE RENDIMIENTO")
    print("=" * 50)
    
    # Definir algoritmos a comparar
    algoritmos = {
        "Búsqueda binaria": busqueda_binaria,
        "Búsqueda recursiva": busqueda_binaria_recursiva,
        "Primera ocurrencia": busqueda_binaria_primera_ocurrencia,
        "Última ocurrencia": busqueda_binaria_ultima_ocurrencia
    }
    
    # Generar casos de prueba
    casos = generar_casos_prueba_busqueda()
    
    # Comparar rendimiento
    comparar_busquedas_binarias(
        algoritmos, 
        casos["arrays"], 
        casos["objetivos"][:5]  # Solo primeros 5 objetivos para no saturar
    )

def demo_casos_especiales():
    """Demostración de casos especiales."""
    print("\n🎭 CASOS ESPECIALES")
    print("=" * 50)
    
    # Caso 1: Array vacío
    print("1. Array vacío:")
    arr_vacio = []
    resultado = busqueda_binaria(arr_vacio, 5)
    print(f"   Resultado: {resultado}")
    
    # Caso 2: Array con un elemento
    print("\n2. Array con un elemento:")
    arr_uno = [42]
    resultado = busqueda_binaria(arr_uno, 42)
    print(f"   Buscando 42: {resultado}")
    resultado = busqueda_binaria(arr_uno, 10)
    print(f"   Buscando 10: {resultado}")
    
    # Caso 3: Array con todos elementos iguales
    print("\n3. Array con elementos iguales:")
    arr_iguales = [5, 5, 5, 5, 5]
    primera = busqueda_binaria_primera_ocurrencia(arr_iguales, 5)
    ultima = busqueda_binaria_ultima_ocurrencia(arr_iguales, 5)
    print(f"   Primera ocurrencia de 5: {primera}")
    print(f"   Última ocurrencia de 5: {ultima}")

def main():
    """Función principal de demostración."""
    print("🎉 BIENVENIDO A LA DEMOSTRACIÓN DE BÚSQUEDA BINARIA")
    print("=" * 60)
    
    try:
        # Ejecutar todas las demostraciones
        demo_basica()
        demo_variantes()
        demo_arrays_rotados()
        demo_matrices_2d()
        demo_busqueda_aproximada()
        demo_calculos_matematicos()
        demo_rendimiento()
        demo_casos_especiales()
        
        print("\n🎊 ¡Demostración completada exitosamente!")
        
    except Exception as e:
        print(f"\n❌ Error durante la demostración: {e}")

if __name__ == "__main__":
    main() 