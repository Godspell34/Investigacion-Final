# 🚀 Menú Dinámico de Análisis de Algoritmos

## 📋 Descripción

El **Menú Dinámico** es una herramienta interactiva y completa que permite comparar diferentes métodos de búsqueda y ordenamiento, analizando cuál es el más eficiente según el caso específico. Proporciona análisis de rendimiento en tiempo real y recomendaciones basadas en los resultados.

## ✨ Características Principales

### 🎯 **Análisis Inteligente**
- Comparación automática de algoritmos
- Medición de tiempo de ejecución
- Identificación del método más rápido
- Análisis de casos especiales

### 🔍 **Métodos de Búsqueda Analizados**
- Búsqueda binaria iterativa vs recursiva
- Búsqueda en arrays con duplicados
- Búsqueda en arrays rotados
- Búsqueda en matrices 2D
- Arrays vs Listas Enlazadas
- Búsqueda aproximada

### 📊 **Métodos de Ordenamiento Analizados**
- QuickSort básico vs variantes
- Análisis con arrays con duplicados
- Análisis con arrays ya ordenados
- Análisis con arrays inversos
- Análisis de escalabilidad

## 🛠️ Instalación y Uso

### Requisitos
```bash
pip install colorama
```

### Ejecución
```bash
python Menu_Dinamico.py
```

## 📖 Guía de Uso

### 1. **Generar Datos de Prueba**
```
Tipos disponibles:
- Array aleatorio
- Array con duplicados  
- Array ordenado
- Array inverso
- Array rotado
```

### 2. **Comparar Métodos de Búsqueda**

#### 🔍 **Búsqueda Binaria Básica vs Recursiva**
- Compara la implementación iterativa vs recursiva
- Muestra diferencias de rendimiento
- Identifica cuál es más eficiente

#### 🔍 **Búsqueda en Arrays con Duplicados**
- Búsqueda binaria básica
- Primera ocurrencia
- Última ocurrencia
- Análisis de eficiencia con duplicados

#### 🔍 **Búsqueda en Arrays Rotados**
- Búsqueda binaria especializada para arrays rotados
- Comparación con búsqueda lineal
- Análisis de casos complejos

#### 🔍 **Búsqueda en Matrices 2D**
- Búsqueda binaria en matrices ordenadas
- Comparación con búsqueda lineal 2D
- Análisis de eficiencia espacial

#### 🔍 **Arrays vs Listas Enlazadas**
- Búsqueda binaria en arrays
- Búsqueda binaria en listas enlazadas
- Búsqueda lineal en listas enlazadas
- Demostración de ineficiencia de listas enlazadas

#### 🔍 **Búsqueda Aproximada**
- Búsqueda binaria aproximada
- Búsqueda lineal aproximada
- Análisis de precisión vs velocidad

### 3. **Comparar Métodos de Ordenamiento**

#### 📊 **QuickSort Básico vs Variantes**
- QuickSort básico
- QuickSort 3-way partition
- Dual-Pivot QuickSort
- QuickSort aleatorizado

#### 📊 **Análisis con Duplicados**
- Eficiencia con arrays con muchos duplicados
- Comparación de variantes especializadas

#### 📊 **Casos Especiales**
- Arrays ya ordenados
- Arrays en orden inverso
- Análisis de casos extremos

#### 📊 **Análisis de Escalabilidad**
- Comparación con diferentes tamaños
- Análisis de crecimiento temporal
- Identificación de patrones de rendimiento

### 4. **Análisis Completo de Rendimiento**
- Ejecuta múltiples comparaciones automáticamente
- Genera resumen de resultados
- Proporciona recomendaciones

## 📈 Resultados y Análisis

### 🏆 **Identificación del Ganador**
El menú automáticamente identifica el método más rápido:
```
🏆 Más rápido: [Nombre del método] (tiempo)
```

### 📊 **Métricas de Comparación**
- **Tiempo de ejecución**: Medición precisa en segundos
- **Resultado**: Valor retornado por cada método
- **Eficiencia relativa**: Comparación entre métodos

### 🎯 **Recomendaciones Automáticas**
Basadas en los resultados, el sistema puede recomendar:
- El método más rápido para el caso específico
- Cuándo usar cada variante
- Consideraciones de escalabilidad

## 🔧 Funcionalidades Técnicas

### 🎨 **Interfaz de Usuario**
- Menús coloridos y intuitivos
- Navegación fácil entre opciones
- Limpieza automática de pantalla
- Formato consistente de resultados

### ⚡ **Medición de Rendimiento**
- Uso de `time.time()` para medición precisa
- Múltiples ejecuciones para consistencia
- Manejo de errores y casos edge

### 🧪 **Generación de Datos**
- Arrays aleatorios
- Arrays con patrones específicos
- Control de tamaño y distribución
- Casos de prueba realistas

## 📋 Estructura del Código

```python
class MenuDinamico:
    def __init__(self):
        self.array_actual = []
        self.lista_enlazada_actual = None
        self.resultados_comparacion = {}
    
    # Métodos principales
    - generar_datos_prueba()
    - comparar_metodos()
    - comparar_metodos_ordenamiento()
    - analisis_completo()
    
    # Menús específicos
    - ejecutar_menu_busqueda()
    - ejecutar_menu_ordenamiento()
```

## 🎯 Casos de Uso

### 👨‍💻 **Para Estudiantes**
- Aprender diferencias entre algoritmos
- Ver el impacto de la implementación
- Entender casos especiales

### 🔬 **Para Investigadores**
- Comparar variantes de algoritmos
- Analizar rendimiento en casos específicos
- Validar hipótesis sobre eficiencia

### 🛠️ **Para Desarrolladores**
- Elegir el algoritmo correcto
- Optimizar código existente
- Tomar decisiones informadas

## 📊 Ejemplos de Salida

### Comparación de Búsqueda Binaria
```
BÚSQUEDA BINARIA BÁSICA vs RECURSIVA
==================================================
Búsqueda binaria iterativa    | 0.00001234s | Resultado: 5
Búsqueda binaria recursiva    | 0.00001567s | Resultado: 5

🏆 Más rápido: Búsqueda binaria iterativa (0.00001234s)
```

### Comparación de QuickSort
```
QUICKSORT BÁSICO vs VARIANTES
==================================================
QuickSort básico              | 0.00123456s
QuickSort 3-way               | 0.00098765s
Dual-Pivot QuickSort          | 0.00112345s
QuickSort aleatorizado        | 0.00134567s

🏆 Más rápido: QuickSort 3-way (0.00098765s)
```

## 🚀 Ventajas del Menú Dinámico

### ✅ **Completamente Automatizado**
- No requiere configuración manual
- Generación automática de datos de prueba
- Comparación automática de métodos

### ✅ **Análisis Exhaustivo**
- Cubre múltiples casos de uso
- Incluye casos especiales y edge cases
- Análisis de escalabilidad

### ✅ **Interfaz Intuitiva**
- Menús coloridos y fáciles de usar
- Navegación clara entre opciones
- Resultados bien formateados

### ✅ **Educativo**
- Explicaciones claras de cada comparación
- Identificación del método más eficiente
- Aprendizaje práctico de algoritmos

## 🔮 Futuras Mejoras

- [ ] Gráficos de rendimiento
- [ ] Exportación de resultados a CSV
- [ ] Más algoritmos de ordenamiento
- [ ] Análisis de complejidad espacial
- [ ] Comparación de múltiples lenguajes

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

**¡Explora el poder del análisis dinámico de algoritmos! 🚀✨** 