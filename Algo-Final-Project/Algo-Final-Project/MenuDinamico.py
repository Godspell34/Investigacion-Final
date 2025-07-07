from colorama import init, Fore, Style
import os
import time
import random
from typing import List, Callable, Dict, Any

# Importar algoritmos de búsqueda
from BusquedaBinaria import (
    busqueda_binaria, busqueda_binaria_recursiva,
    busqueda_binaria_primera_ocurrencia, busqueda_binaria_ultima_ocurrencia,
    busqueda_binaria_rotated_array, busqueda_binaria_2d,
    busqueda_binaria_aproximada, busqueda_binaria_lista_enlazada,
    crear_lista_enlazada_desde_array
)

# Importar algoritmos de ordenamiento
from QuickSort import (
    quicksort, quicksort_3way, quicksort_dual_pivot,
    quicksort_randomized
)

init(autoreset=True)

class MenuDinamico:
    def __init__(self):
        self.array_actual = []
        self.lista_enlazada_actual = None
        self.resultados_comparacion = {}
        
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_titulo(self, titulo):
        print(Fore.CYAN + Style.BRIGHT + f"\n{'='*20} {titulo} {'='*20}")
    
    def mostrar_menu_principal(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("MENÚ DINÁMICO DE ANÁLISIS")
        print(Fore.YELLOW + "1. " + Fore.GREEN + "Generar datos de prueba")
        print(Fore.YELLOW + "2. " + Fore.BLUE + "Comparar métodos de búsqueda")
        print(Fore.YELLOW + "3. " + Fore.MAGENTA + "Comparar métodos de ordenamiento")
        print(Fore.YELLOW + "4. " + Fore.CYAN + "Análisis completo de rendimiento")
        print(Fore.YELLOW + "5. " + Fore.RED + "Salir")
        print(Fore.CYAN + "=" * 60)
    
    def mostrar_menu_busqueda(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("COMPARACIÓN DE MÉTODOS DE BÚSQUEDA")
        print(Fore.YELLOW + "1. " + Fore.GREEN + "Búsqueda binaria básica vs recursiva")
        print(Fore.YELLOW + "2. " + Fore.BLUE + "Búsqueda en arrays con duplicados")
        print(Fore.YELLOW + "3. " + Fore.MAGENTA + "Búsqueda en arrays rotados")
        print(Fore.YELLOW + "4. " + Fore.CYAN + "Búsqueda en matrices 2D")
        print(Fore.YELLOW + "5. " + Fore.RED + "Arrays vs Listas Enlazadas")
        print(Fore.YELLOW + "6. " + Fore.GREEN + "Búsqueda aproximada")
        print(Fore.YELLOW + "7. " + Fore.BLUE + "Volver al menú principal")
        print(Fore.CYAN + "=" * 60)
    
    def mostrar_menu_ordenamiento(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("COMPARACIÓN DE MÉTODOS DE ORDENAMIENTO")
        print(Fore.YELLOW + "1. " + Fore.GREEN + "QuickSort básico vs variantes")
        print(Fore.YELLOW + "2. " + Fore.BLUE + "Análisis con arrays con duplicados")
        print(Fore.YELLOW + "3. " + Fore.MAGENTA + "Análisis con arrays ya ordenados")
        print(Fore.YELLOW + "4. " + Fore.CYAN + "Análisis con arrays inversos")
        print(Fore.YELLOW + "5. " + Fore.GREEN + "Volver al menú principal")
        print(Fore.CYAN + "=" * 60)
    
    def generar_datos_prueba(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("GENERACIÓN DE DATOS DE PRUEBA")
        
        print(Fore.YELLOW + "Tipos de datos disponibles:")
        print(Fore.GREEN + "1. Array aleatorio")
        print(Fore.BLUE + "2. Array con duplicados")
        print(Fore.MAGENTA + "3. Array ordenado")
        print(Fore.CYAN + "4. Array inverso")
        print(Fore.RED + "5. Array rotado")
        
        opcion = input(Fore.YELLOW + "\nSelecciona el tipo de datos: ")
        tamanio = int(input(Fore.YELLOW + "Tamaño del array: "))
        
        if opcion == "1":
            self.array_actual = [random.randint(1, tamanio * 10) for _ in range(tamanio)]
            print(Fore.GREEN + f"Array aleatorio generado: {self.array_actual[:10]}...")
        elif opcion == "2":
            valores_unicos = min(10, tamanio // 10)
            valores = list(range(1, valores_unicos + 1))
            self.array_actual = [random.choice(valores) for _ in range(tamanio)]
            print(Fore.GREEN + f"Array con duplicados generado: {self.array_actual[:10]}...")
        elif opcion == "3":
            self.array_actual = list(range(1, tamanio + 1))
            print(Fore.GREEN + f"Array ordenado generado: {self.array_actual[:10]}...")
        elif opcion == "4":
            self.array_actual = list(range(tamanio, 0, -1))
            print(Fore.GREEN + f"Array inverso generado: {self.array_actual[:10]}...")
        elif opcion == "5":
            self.array_actual = list(range(1, tamanio + 1))
            rotaciones = random.randint(1, tamanio - 1)
            self.array_actual = self.array_actual[rotaciones:] + self.array_actual[:rotaciones]
            print(Fore.GREEN + f"Array rotado generado: {self.array_actual[:10]}...")
        
        # Crear lista enlazada correspondiente
        self.lista_enlazada_actual = crear_lista_enlazada_desde_array(sorted(self.array_actual))
        print(Fore.BLUE + f"Lista enlazada ordenada creada con {len(self.array_actual)} elementos")
        
        input(Fore.WHITE + "\nPresiona Enter para continuar...")
    
    def comparar_busqueda_basica(self):
        if not self.array_actual:
            print(Fore.RED + "Primero genera datos de prueba")
            return
        
        self.limpiar_pantalla()
        self.mostrar_titulo("BÚSQUEDA BINARIA BÁSICA vs RECURSIVA")
        
        # Ordenar el array para búsqueda binaria
        array_ordenado = sorted(self.array_actual)
        objetivo = random.choice(array_ordenado)
        
        print(Fore.YELLOW + f"Buscando: {objetivo}")
        print(Fore.CYAN + f"Array: {array_ordenado[:10]}...")
        
        # Comparar métodos
        metodos = {
            "Búsqueda binaria iterativa": lambda: busqueda_binaria(array_ordenado, objetivo),
            "Búsqueda binaria recursiva": lambda: busqueda_binaria_recursiva(array_ordenado, objetivo)
        }
        
        self.comparar_metodos(metodos, "búsqueda binaria básica")
    
    def comparar_busqueda_duplicados(self):
        if not self.array_actual:
            print(Fore.RED + "Primero genera datos de prueba")
            return
        
        self.limpiar_pantalla()
        self.mostrar_titulo("BÚSQUEDA EN ARRAYS CON DUPLICADOS")
        
        # Crear array con duplicados si no lo es
        if len(set(self.array_actual)) == len(self.array_actual):
            valores_unicos = min(10, len(self.array_actual) // 10)
            valores = list(range(1, valores_unicos + 1))
            array_duplicados = [random.choice(valores) for _ in range(len(self.array_actual))]
            array_duplicados.sort()
        else:
            array_duplicados = sorted(self.array_actual)
        
        objetivo = random.choice(array_duplicados)
        
        print(Fore.YELLOW + f"Buscando: {objetivo}")
        print(Fore.CYAN + f"Array con duplicados: {array_duplicados[:15]}...")
        
        metodos = {
            "Búsqueda binaria básica": lambda: busqueda_binaria(array_duplicados, objetivo),
            "Primera ocurrencia": lambda: busqueda_binaria_primera_ocurrencia(array_duplicados, objetivo),
            "Última ocurrencia": lambda: busqueda_binaria_ultima_ocurrencia(array_duplicados, objetivo)
        }
        
        self.comparar_metodos(metodos, "búsqueda con duplicados")
    
    def comparar_busqueda_rotados(self):
        if not self.array_actual:
            print(Fore.RED + "Primero genera datos de prueba")
            return
        
        self.limpiar_pantalla()
        self.mostrar_titulo("BÚSQUEDA EN ARRAYS ROTADOS")
        
        # Crear array rotado
        array_ordenado = list(range(1, len(self.array_actual) + 1))
        rotaciones = random.randint(1, len(array_ordenado) - 1)
        array_rotado = array_ordenado[rotaciones:] + array_ordenado[:rotaciones]
        
        objetivo = random.choice(array_ordenado)
        
        print(Fore.YELLOW + f"Buscando: {objetivo}")
        print(Fore.CYAN + f"Array rotado: {array_rotado[:15]}...")
        
        metodos = {
            "Búsqueda binaria en array rotado": lambda: busqueda_binaria_rotated_array(array_rotado, objetivo),
            "Búsqueda lineal (comparación)": lambda: self.busqueda_lineal(array_rotado, objetivo)
        }
        
        self.comparar_metodos(metodos, "búsqueda en arrays rotados")
    
    def comparar_busqueda_2d(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("BÚSQUEDA EN MATRICES 2D")
        
        # Crear matriz 2D ordenada
        filas, columnas = 5, 6
        matriz = []
        valor = 1
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(valor)
                valor += 1
            matriz.append(fila)
        
        objetivo = random.randint(1, filas * columnas)
        
        print(Fore.YELLOW + f"Buscando: {objetivo}")
        print(Fore.CYAN + "Matriz 2D:")
        for fila in matriz:
            print(f"  {fila}")
        
        metodos = {
            "Búsqueda binaria 2D": lambda: busqueda_binaria_2d(matriz, objetivo),
            "Búsqueda lineal 2D": lambda: self.busqueda_lineal_2d(matriz, objetivo)
        }
        
        self.comparar_metodos(metodos, "búsqueda en matrices 2D")
    
    def comparar_arrays_vs_linked_lists(self):
        if not self.array_actual:
            print(Fore.RED + "Primero genera datos de prueba")
            return
        
        self.limpiar_pantalla()
        self.mostrar_titulo("ARRAYS vs LISTAS ENLAZADAS")
        
        array_ordenado = sorted(self.array_actual)
        objetivo = random.choice(array_ordenado)
        
        print(Fore.YELLOW + f"Buscando: {objetivo}")
        print(Fore.CYAN + f"Array: {array_ordenado[:10]}...")
        
        metodos = {
            "Búsqueda binaria en array": lambda: busqueda_binaria(array_ordenado, objetivo),
            "Búsqueda binaria en lista enlazada": lambda: busqueda_binaria_lista_enlazada(self.lista_enlazada_actual, objetivo),
            "Búsqueda lineal en lista enlazada": lambda: self.busqueda_lineal_lista_enlazada(self.lista_enlazada_actual, objetivo)
        }
        
        self.comparar_metodos(metodos, "arrays vs listas enlazadas")
    
    def comparar_busqueda_aproximada(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("BÚSQUEDA APROXIMADA")
        
        # Crear array con números decimales
        array_decimales = [1.1, 2.3, 3.5, 4.7, 5.9, 7.1, 8.3, 9.5]
        objetivo = 6.0
        
        print(Fore.YELLOW + f"Buscando aproximación de: {objetivo}")
        print(Fore.CYAN + f"Array: {array_decimales}")
        
        metodos = {
            "Búsqueda binaria aproximada": lambda: busqueda_binaria_aproximada(array_decimales, objetivo),
            "Búsqueda lineal aproximada": lambda: self.busqueda_lineal_aproximada(array_decimales, objetivo)
        }
        
        self.comparar_metodos(metodos, "búsqueda aproximada")
    
    def comparar_quicksort_variantes(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("QUICKSORT BÁSICO vs VARIANTES")
        
        # Si no hay array actual, generar uno
        if not self.array_actual:
            self.array_actual = [random.randint(1, 1000) for _ in range(1000)]
            print(Fore.YELLOW + "Array generado automáticamente")
        
        print(Fore.YELLOW + f"Array original: {self.array_actual[:10]}...")
        print(Fore.CYAN + f"Tamaño del array: {len(self.array_actual)} elementos")
        print(Fore.CYAN + f"Rango de valores: {min(self.array_actual)} - {max(self.array_actual)}")
        
        metodos = {
            "QuickSort básico": lambda arr: quicksort(arr),
            "QuickSort 3-way": lambda arr: quicksort_3way(arr),
            "Dual-Pivot QuickSort": lambda arr: quicksort_dual_pivot(arr),
            "QuickSort aleatorizado": lambda arr: quicksort_randomized(arr)
        }
        
        self.comparar_metodos_ordenamiento(metodos, "QuickSort variantes")
    
    def comparar_quicksort_duplicados(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("QUICKSORT CON DUPLICADOS")
        
        # Crear array con muchos duplicados
        tamanio = 1000
        valores_unicos = 10
        valores = list(range(1, valores_unicos + 1))
        array_duplicados = [random.choice(valores) for _ in range(tamanio)]
        
        # Guardar el array de duplicados como array actual
        self.array_actual = array_duplicados
        
        print(Fore.YELLOW + f"Array con duplicados: {array_duplicados[:15]}...")
        print(Fore.CYAN + f"Tamaño del array: {len(array_duplicados)} elementos")
        print(Fore.CYAN + f"Valores únicos: {len(set(array_duplicados))} de {valores_unicos}")
        print(Fore.CYAN + f"Duplicados promedio: {len(array_duplicados) // len(set(array_duplicados))} por valor")
        
        metodos = {
            "QuickSort básico": lambda arr: quicksort(arr),
            "QuickSort 3-way": lambda arr: quicksort_3way(arr),
            "QuickSort aleatorizado": lambda arr: quicksort_randomized(arr)
        }
        
        self.comparar_metodos_ordenamiento(metodos, "QuickSort con duplicados")
    
    def comparar_quicksort_casos_especiales(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("QUICKSORT CASOS ESPECIALES")
        
        tamanio = 1000
        
        print(Fore.YELLOW + "Comparando casos especiales:")
        
        # Array ordenado
        array_ordenado = list(range(1, tamanio + 1))
        self.array_actual = array_ordenado
        print(Fore.CYAN + f"1. Array ordenado: {array_ordenado[:10]}...")
        
        metodos = {
            "QuickSort básico": lambda arr: quicksort(arr),
            "QuickSort aleatorizado": lambda arr: quicksort_randomized(arr)
        }
        
        self.comparar_metodos_ordenamiento(metodos, "QuickSort array ordenado")
        
        # Pausa entre casos
        input(Fore.YELLOW + "\nPresiona Enter para continuar con el siguiente caso...")
        
        # Array inverso
        array_inverso = list(range(tamanio, 0, -1))
        self.array_actual = array_inverso
        print(Fore.CYAN + f"\n2. Array inverso: {array_inverso[:10]}...")
        
        self.comparar_metodos_ordenamiento(metodos, "QuickSort array inverso")
    
    def analizar_escalabilidad(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("ANÁLISIS DE ESCALABILIDAD")
        
        tamanios = [100, 1000, 5000, 10000]
        
        print(Fore.YELLOW + "Analizando escalabilidad con diferentes tamaños:")
        
        for i, tamanio in enumerate(tamanios):
            print(Fore.CYAN + f"\nTamaño: {tamanio}")
            print("-" * 30)
            
            # Generar array aleatorio
            array = [random.randint(1, tamanio * 10) for _ in range(tamanio)]
            self.array_actual = array
            
            metodos = {
                "QuickSort básico": lambda arr: quicksort(arr),
                "QuickSort 3-way": lambda arr: quicksort_3way(arr),
                "QuickSort aleatorizado": lambda arr: quicksort_randomized(arr)
            }
            
            self.comparar_metodos_ordenamiento(metodos, f"escalabilidad tamaño {tamanio}")
            
            # Pausa entre tamaños (excepto el último)
            if i < len(tamanios) - 1:
                input(Fore.YELLOW + f"\nPresiona Enter para continuar con tamaño {tamanios[i+1]}...")
    
    def comparar_metodos(self, metodos: Dict[str, Callable], descripcion: str):
        print(Fore.CYAN + f"\nComparando métodos de {descripcion}:")
        print("-" * 50)
        
        resultados = {}
        
        for nombre, metodo in metodos.items():
            inicio = time.time()
            resultado = metodo()
            fin = time.time()
            tiempo = fin - inicio
            
            resultados[nombre] = {
                'tiempo': tiempo,
                'resultado': resultado
            }
            
            print(f"{nombre:30} | {tiempo:.8f}s | Resultado: {resultado}")
        
        # Encontrar el más rápido
        mas_rapido = min(resultados.items(), key=lambda x: x[1]['tiempo'])
        print(Fore.GREEN + f"\n🏆 Más rápido: {mas_rapido[0]} ({mas_rapido[1]['tiempo']:.8f}s)")
        
        # Guardar resultados
        self.resultados_comparacion[descripcion] = resultados
        
        input(Fore.WHITE + "\nPresiona Enter para continuar...")
    
    def comparar_metodos_ordenamiento(self, metodos: Dict[str, Callable], descripcion: str):
        print(Fore.CYAN + f"\nComparando métodos de {descripcion}:")
        print("-" * 50)
        
        resultados = {}
        
        # Usar array_actual si existe, sino generar uno
        array_a_ordenar = self.array_actual if self.array_actual else [random.randint(1, 1000) for _ in range(1000)]
        
        for nombre, metodo in metodos.items():
            try:
                # Crear una copia del array para cada método
                array_copia = array_a_ordenar.copy()
                
                inicio = time.time()
                resultado = metodo(array_copia)
                fin = time.time()
                tiempo = fin - inicio
                
                resultados[nombre] = {
                    'tiempo': tiempo,
                    'resultado': resultado
                }
                
                print(f"{nombre:30} | {tiempo:.8f}s")
                
            except Exception as e:
                print(f"{nombre:30} | ERROR: {str(e)}")
                resultados[nombre] = {
                    'tiempo': float('inf'),
                    'resultado': None,
                    'error': str(e)
                }
        
        # Encontrar el más rápido (excluyendo errores)
        resultados_validos = {k: v for k, v in resultados.items() if v['tiempo'] != float('inf')}
        if resultados_validos:
            mas_rapido = min(resultados_validos.items(), key=lambda x: x[1]['tiempo'])
            print(Fore.GREEN + f"\n🏆 Más rápido: {mas_rapido[0]} ({mas_rapido[1]['tiempo']:.8f}s)")
        else:
            print(Fore.RED + "\n❌ Todos los métodos fallaron")
        
        # Guardar resultados
        self.resultados_comparacion[descripcion] = resultados
        
        # Pausa para que el usuario pueda ver los resultados
        input(Fore.WHITE + "\nPresiona Enter para continuar...")
    
    # Métodos auxiliares para búsquedas
    def busqueda_lineal(self, arr, objetivo):
        for i, elemento in enumerate(arr):
            if elemento == objetivo:
                return i
        return -1
    
    def busqueda_lineal_2d(self, matriz, objetivo):
        for i, fila in enumerate(matriz):
            for j, elemento in enumerate(fila):
                if elemento == objetivo:
                    return (i, j)
        return (-1, -1)
    
    def busqueda_lineal_lista_enlazada(self, lista, objetivo):
        actual = lista.cabeza
        indice = 0
        while actual:
            if actual.valor == objetivo:
                return indice
            actual = actual.siguiente
            indice += 1
        return -1
    
    def busqueda_lineal_aproximada(self, arr, objetivo):
        mejor_indice = -1
        mejor_diferencia = float('inf')
        for i, elemento in enumerate(arr):
            diferencia = abs(elemento - objetivo)
            if diferencia < mejor_diferencia:
                mejor_diferencia = diferencia
                mejor_indice = i
        return (mejor_indice, arr[mejor_indice], mejor_diferencia)
    

    
    def analisis_completo(self):
        self.limpiar_pantalla()
        self.mostrar_titulo("ANÁLISIS COMPLETO DE RENDIMIENTO")
        
        if not self.array_actual:
            print(Fore.RED + "Primero genera datos de prueba")
            input(Fore.WHITE + "\nPresiona Enter para continuar...")
            return
        
        print(Fore.YELLOW + "Realizando análisis completo...")
        
        # Análisis de búsqueda
        print(Fore.CYAN + "\n1. ANÁLISIS DE BÚSQUEDA:")
        self.comparar_busqueda_basica()
        
        # Análisis de ordenamiento
        print(Fore.CYAN + "\n2. ANÁLISIS DE ORDENAMIENTO:")
        self.comparar_quicksort_variantes()
        
        # Resumen
        print(Fore.GREEN + "\n📊 RESUMEN DE RESULTADOS:")
        print("-" * 40)
        
        for descripcion, resultados in self.resultados_comparacion.items():
            print(f"\n{descripcion.upper()}:")
            for nombre, datos in resultados.items():
                print(f"  {nombre}: {datos['tiempo']:.8f}s")
        
        input(Fore.WHITE + "\nPresiona Enter para continuar...")
    
    def ejecutar(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input(Fore.YELLOW + "Selecciona una opción: ")
            
            if opcion == "1":
                self.generar_datos_prueba()
            elif opcion == "2":
                self.ejecutar_menu_busqueda()
            elif opcion == "3":
                self.ejecutar_menu_ordenamiento()
            elif opcion == "4":
                self.analisis_completo()
            elif opcion == "5":
                print(Fore.CYAN + "¡Saliendo del programa!")
                break
            else:
                print(Fore.RED + "Opción no válida. Intenta de nuevo.")
    
    def ejecutar_menu_busqueda(self):
        while True:
            self.mostrar_menu_busqueda()
            opcion = input(Fore.YELLOW + "Selecciona una opción: ")
            
            if opcion == "1":
                self.comparar_busqueda_basica()
            elif opcion == "2":
                self.comparar_busqueda_duplicados()
            elif opcion == "3":
                self.comparar_busqueda_rotados()
            elif opcion == "4":
                self.comparar_busqueda_2d()
            elif opcion == "5":
                self.comparar_arrays_vs_linked_lists()
            elif opcion == "6":
                self.comparar_busqueda_aproximada()
            elif opcion == "7":
                break
            else:
                print(Fore.RED + "Opción no válida. Intenta de nuevo.")
    
    def ejecutar_menu_ordenamiento(self):
        while True:
            self.mostrar_menu_ordenamiento()
            opcion = input(Fore.YELLOW + "Selecciona una opción: ")
            
            if opcion == "1":
                self.comparar_quicksort_variantes()
            elif opcion == "2":
                self.comparar_quicksort_duplicados()
            elif opcion == "3":
                self.comparar_quicksort_casos_especiales()
            elif opcion == "4":
                self.analizar_escalabilidad()
            elif opcion == "5":
                break
            else:
                print(Fore.RED + "Opción no válida. Intenta de nuevo.")
