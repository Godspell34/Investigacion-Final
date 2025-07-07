# 🔍 Paquete BusquedaBinaria

Implementaciones completas y optimizadas de algoritmos de búsqueda binaria en Python.

## 📁 Estructura del Proyecto

```
BusquedaBinaria/
├── __init__.py                 # Paquete principal
├── basic_binary_search.py      # Búsqueda binaria básica
├── variants_binary_search.py   # Variantes avanzadas
├── advanced_binary_search.py   # Búsquedas especializadas
├── linked_list_binary_search.py # Búsqueda binaria en listas enlazadas
├── utils.py                    # Utilidades y funciones auxiliares
├── demo.py                     # Demostración completa
├── demo_linked_list.py         # Demostración listas enlazadas
├── comparacion_arrays_vs_linked_lists.py # Comparación de rendimiento
└── README.md                   # Este archivo
```

## 🎯 Algoritmos Implementados

### 1. **Búsqueda Binaria Básica** (`basic_binary_search.py`)
- `busqueda_binaria(arr, objetivo)`: Versión iterativa
- `busqueda_binaria_recursiva(arr, objetivo)`: Versión recursiva
- `busqueda_binaria_con_comparaciones(arr, objetivo)`: Cuenta comparaciones
- `busqueda_binaria_con_trazado(arr, objetivo)`: Muestra proceso paso a paso
- **Complejidad**: O(log n) tiempo, O(1) espacio (iterativa) / O(log n) espacio (recursiva)

### 2. **Variantes Avanzadas** (`variants_binary_search.py`)
- `busqueda_binaria_primera_ocurrencia(arr, objetivo)`: Primera ocurrencia
- `busqueda_binaria_ultima_ocurrencia(arr, objetivo)`: Última ocurrencia
- `busqueda_binaria_menor_mayor_igual(arr, objetivo)`: Primer elemento ≥ objetivo
- `busqueda_binaria_mayor_menor_igual(arr, objetivo)`: Último elemento ≤ objetivo
- `contar_ocurrencias(arr, objetivo)`: Cuenta ocurrencias
- `busqueda_binaria_rango(arr, inicio, fin)`: Busca en rango
- `busqueda_binaria_floor_ceil(arr, objetivo)`: Floor y Ceil

### 3. **Búsquedas Especializadas** (`advanced_binary_search.py`)
- `busqueda_binaria_rotated_array(arr, objetivo)`: Arrays rotados
- `encontrar_punto_rotacion(arr)`: Punto de rotación
- `busqueda_binaria_2d(matriz, objetivo)`: Matrices 2D ordenadas
- `busqueda_binaria_aproximada(arr, objetivo)`: Búsqueda aproximada
- `busqueda_binaria_raiz_cuadrada(n)`: Cálculo de raíz cuadrada
- `busqueda_binaria_potencia(base, exponente)`: Raíz n-ésima

### 4. **Búsqueda Binaria en Listas Enlazadas** (`linked_list_binary_search.py`)
- `busqueda_binaria_lista_enlazada(lista, objetivo)`: Con acceso por índice
- `busqueda_binaria_lista_enlazada_optimizada(lista, objetivo)`: Versión optimizada
- `busqueda_binaria_lista_enlazada_con_salto(lista, objetivo)`: Con saltos exponenciales
- `busqueda_binaria_lista_enlazada_con_comparaciones(lista, objetivo)`: Con conteo de comparaciones
- **⚠️ ADVERTENCIA**: Las listas enlazadas son ineficientes para búsqueda binaria

## 🚨 **¿Por qué las Listas Enlazadas son Ineficientes para Búsqueda Binaria?**

### **Comparación de Rendimiento: Arrays vs Listas Enlazadas**

| Operación | Array Python | Lista Enlazada | Diferencia |
|-----------|-------------|----------------|------------|
| **Acceso por índice** | O(1) | O(n) | **n veces más lento** |
| **Búsqueda binaria** | O(log n) | O(n) | **n/log(n) veces más lento** |
| **Memoria** | Contigua | Fragmentada | **Cache misses** |
| **Overhead** | Mínimo | Punteros extra | **Más lento** |

### **Problemas Fundamentales de las Listas Enlazadas**

#### **1. Acceso por Índice: O(n) vs O(1)**
```python
# Array Python - O(1) - Instantáneo
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento = arr[5]  # Acceso directo

# Lista Enlazada - O(n) - Debe recorrer nodos
lista = ListaEnlazada()
nodo = lista.obtener_nodo_en_indice(5)  # Recorre 5 nodos
```

#### **2. Búsqueda Binaria Perdida**
```python
# Array: O(log n) - Real búsqueda binaria
# Lista Enlazada: O(n) - ¡Simula búsqueda binaria pero es lineal!
```

#### **3. Localidad de Cache Pobre**
- **Array**: Datos contiguos en memoria ✅
- **Lista Enlazada**: Datos dispersos, saltos de memoria ❌

### **¿Cuándo Usar Cada Estructura?**

#### **✅ Arrays de Python (Listas) - PARA:**
- Búsqueda binaria
- Acceso frecuente por índice
- Algoritmos que requieren acceso aleatorio
- Cuando el tamaño es conocido

#### **✅ Listas Enlazadas - PARA:**
- Inserción/eliminación frecuente al inicio
- Tamaño dinámico desconocido
- Implementación de pilas/colas
- Cuando la memoria es muy limitada

#### **❌ Listas Enlazadas - NO PARA:**
- Búsqueda binaria
- Acceso frecuente por índice
- Algoritmos que requieren acceso aleatorio

### **Conclusión**
Las listas enlazadas para búsqueda binaria son como **usar un Ferrari para ir a la esquina caminando** - es una **mala elección de herramienta**. 

**Para búsqueda binaria: siempre usa arrays/listas de Python.**

## 🛠️ Instalación y Uso

### Uso Básico
```python
from BusquedaBinaria import busqueda_binaria, busqueda_binaria_primera_ocurrencia

# Array ordenado
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Búsqueda básica
resultado = busqueda_binaria(numeros, 11)
print(resultado)  # 5

# Primera ocurrencia en array con duplicados
arr_duplicados = [1, 2, 2, 2, 3, 4, 4, 5]
primera = busqueda_binaria_primera_ocurrencia(arr_duplicados, 2)
print(primera)  # 1
```

### Demostración Completa
```python
# Ejecutar la demostración
python BusquedaBinaria/demo.py

# Demostración de listas enlazadas (con advertencias)
python BusquedaBinaria/demo_linked_list.py

# Comparación de rendimiento
python BusquedaBinaria/comparacion_arrays_vs_linked_lists.py
```

## 📊 Características de los Algoritmos

| Algoritmo | Mejor Para | Casos Especiales |
|-----------|------------|------------------|
| **Básica** | Arrays ordenados únicos | Arrays pequeños |
| **Primera/Última** | Arrays con duplicados | Conteo de ocurrencias |
| **Floor/Ceil** | Búsquedas de límites | Rangos y aproximaciones |
| **Arrays Rotados** | Arrays rotados | Búsqueda en datos desordenados |
| **Matrices 2D** | Matrices ordenadas | Búsqueda en estructuras 2D |
| **Aproximada** | Números decimales | Búsquedas con tolerancia |
| **Listas Enlazadas** | ⚠️ **NO RECOMENDADO** | Solo para aprendizaje |

## 🎨 Funcionalidades Avanzadas

### Búsqueda en Arrays Rotados
```python
from BusquedaBinaria import busqueda_binaria_rotated_array

# Array original: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Array rotado: [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
arr_rotado = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
resultado = busqueda_binaria_rotated_array(arr_rotado, 7)
print(resultado)  # 3
```

### Búsqueda en Matrices 2D
```python
from BusquedaBinaria import busqueda_binaria_2d

# Matriz ordenada
matriz = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15]
]

resultado = busqueda_binaria_2d(matriz, 13)
print(resultado)  # (2, 2)
```

### Cálculos Matemáticos
```python
from BusquedaBinaria import busqueda_binaria_raiz_cuadrada

raiz = busqueda_binaria_raiz_cuadrada(25)
print(raiz)  # 5.0
```

## 🔧 Funciones de Utilidad

### Generación de Datos de Prueba
```python
from BusquedaBinaria.utils import *

# Arrays de prueba
ordenado = generar_array_ordenado(1000)
con_duplicados = generar_array_con_duplicados(100, 20)
rotado = generar_array_rotado(20, 7)
matriz_2d = generar_matriz_2d_ordenada(5, 6)
```

### Comparación de Rendimiento
```python
from BusquedaBinaria.utils import comparar_busquedas_binarias

algoritmos = {
    "Básica": busqueda_binaria,
    "Primera ocurrencia": busqueda_binaria_primera_ocurrencia,
    "Última ocurrencia": busqueda_binaria_ultima_ocurrencia
}

comparar_busquedas_binarias(algoritmos, arrays, objetivos)
```

## 🎯 Casos de Uso Comunes

### 1. **Búsqueda en Arrays Ordenados**
```python
# Caso típico
indice = busqueda_binaria(array_ordenado, valor)
```

### 2. **Conteo de Elementos**
```python
# Contar ocurrencias de un elemento
count = contar_ocurrencias(array_con_duplicados, elemento)
```

### 3. **Búsqueda de Rangos**
```python
# Encontrar elementos en un rango
inicio, fin = busqueda_binaria_rango(array, valor_min, valor_max)
```

### 4. **Búsqueda Aproximada**
```python
# Encontrar el elemento más cercano
indice, valor, diferencia = busqueda_binaria_aproximada(array, objetivo)
```

## 🚀 Ejecutar Demostración

```bash
cd BusquedaBinaria
python demo.py
```

## 📈 Ventajas de la Búsqueda Binaria

- **Eficiencia**: O(log n) en el peor caso
- **Versatilidad**: Múltiples variantes para diferentes casos
- **Aplicabilidad**: Útil en muchos problemas de programación
- **Optimización**: Mejor que búsqueda lineal O(n)

## 🎨 Características del Paquete

- ✅ **Código limpio y bien documentado**
- ✅ **Múltiples implementaciones optimizadas**
- ✅ **Funciones de utilidad para pruebas**
- ✅ **Demostración interactiva completa**
- ✅ **Comparación de rendimiento**
- ✅ **Manejo de casos especiales**
- ✅ **Aplicaciones matemáticas**
- ⚠️ **Advertencias sobre listas enlazadas**
