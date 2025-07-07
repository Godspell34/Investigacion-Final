# 🚀 Paquete QuickSort

Implementaciones completas y optimizadas de algoritmos de ordenamiento QuickSort en Python.

## 📁 Estructura del Proyecto

```
QuickSort/
├── __init__.py              # Paquete principal
├── basic_quicksort.py       # QuickSort básico e in-place
├── three_way_quicksort.py   # QuickSort con partición de 3 vías
├── dual_pivot_quicksort.py  # QuickSort con dos pivotes
├── randomized_quicksort.py  # QuickSort aleatorizado y mediana de tres
├── utils.py                 # Utilidades y funciones auxiliares
├── demo.py                  # Demostración completa
└── README.md               # Este archivo
```

## 🎯 Algoritmos Implementados

### 1. **QuickSort Básico** (`basic_quicksort.py`)
- `quicksort(arr)`: Retorna una nueva lista ordenada
- `quicksort_inplace(arr)`: Modifica la lista original
- **Complejidad**: O(n log n) promedio, O(n²) peor caso

### 2. **QuickSort 3-Way** (`three_way_quicksort.py`)
- `quicksort_3way(arr)`: Partición de 3 vías
- **Ventaja**: Excelente para arrays con muchos duplicados
- **Complejidad**: O(n log n) promedio

### 3. **Dual-Pivot QuickSort** (`dual_pivot_quicksort.py`)
- `quicksort_dual_pivot(arr)`: Usa dos pivotes
- **Ventaja**: Mejor rendimiento en la práctica
- **Complejidad**: O(n log n) promedio

### 4. **QuickSort Aleatorizado** (`randomized_quicksort.py`)
- `quicksort_randomized(arr)`: Selección aleatoria del pivote
- `quicksort_median_of_three(arr)`: Mediana de tres elementos
- **Ventaja**: Evita casos degenerados

## 🛠️ Instalación y Uso

### Uso Básico
```python
from QuickSort import quicksort, quicksort_3way, quicksort_dual_pivot

# Array de ejemplo
numeros = [64, 34, 25, 12, 22, 11, 90]

# QuickSort básico
resultado = quicksort(numeros)
print(resultado)  # [11, 12, 22, 25, 34, 64, 90]

# QuickSort 3-way (in-place)
quicksort_3way(numeros)
print(numeros)  # [11, 12, 22, 25, 34, 64, 90]
```

### Demostración Completa
```python
# Ejecutar la demostración
python QuickSort/demo.py
```

## 📊 Comparación de Rendimiento

El archivo `demo.py` incluye una comparación completa de rendimiento:

- **Arrays aleatorios**: Prueba general
- **Arrays con duplicados**: Evalúa 3-way QuickSort
- **Arrays ordenados**: Prueba casos degenerados
- **Arrays inversos**: Prueba casos degenerados

## 🎨 Características

- ✅ **Código limpio y bien documentado**
- ✅ **Múltiples implementaciones optimizadas**
- ✅ **Funciones de utilidad para pruebas**
- ✅ **Demostración interactiva**
- ✅ **Comparación de rendimiento**
- ✅ **Manejo de casos especiales**

## 🔧 Funciones de Utilidad

### Generación de Arrays de Prueba
```python
from QuickSort.utils import *

# Arrays de prueba
aleatorio = generar_array_aleatorio(1000)
duplicados = generar_array_duplicados(1000, 50)
ordenado = generar_array_ordenado(1000)
inverso = generar_array_inverso(1000)
```

### Medición de Rendimiento
```python
from QuickSort.utils import medir_tiempo, comparar_algoritmos

# Medir tiempo de un algoritmo
tiempo = medir_tiempo(quicksort_3way, numeros)

# Comparar múltiples algoritmos
algoritmos = {
    "Básico": quicksort,
    "3-Way": quicksort_3way,
    "Dual-Pivot": quicksort_dual_pivot
}
comparar_algoritmos(algoritmos, arrays)
```

## 🎯 Casos de Uso Recomendados

| Algoritmo | Mejor Para | Evitar En |
|-----------|------------|-----------|
| **Básico** | Arrays pequeños, aprendizaje | Arrays grandes con duplicados |
| **3-Way** | Arrays con muchos duplicados | Arrays únicos pequeños |
| **Dual-Pivot** | Arrays grandes en general | Arrays muy pequeños |
| **Aleatorizado** | Arrays que pueden estar ordenados | Arrays con patrones específicos |

## 🚀 Ejecutar Demostración

```bash
cd QuickSort
python demo.py
```
