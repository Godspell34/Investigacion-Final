"""
Paquete BusquedaBinaria - Implementaciones de algoritmos de búsqueda binaria
"""

from .basic_binary_search import busqueda_binaria, busqueda_binaria_recursiva
from .variants_binary_search import (
    busqueda_binaria_primera_ocurrencia,
    busqueda_binaria_ultima_ocurrencia,
    busqueda_binaria_menor_mayor_igual,
    busqueda_binaria_mayor_menor_igual
)
from .advanced_binary_search import (
    busqueda_binaria_rotated_array,
    busqueda_binaria_2d,
    busqueda_binaria_aproximada
)
from .linked_list_binary_search import (
    Nodo,
    ListaEnlazada,
    busqueda_binaria_lista_enlazada,
    busqueda_binaria_lista_enlazada_optimizada,
    busqueda_binaria_lista_enlazada_con_salto,
    busqueda_binaria_lista_enlazada_con_comparaciones,
    crear_lista_enlazada_desde_array,
    comparar_busquedas_lista_enlazada
)

__all__ = [
    'busqueda_binaria',
    'busqueda_binaria_recursiva',
    'busqueda_binaria_primera_ocurrencia',
    'busqueda_binaria_ultima_ocurrencia', 
    'busqueda_binaria_menor_mayor_igual',
    'busqueda_binaria_mayor_menor_igual',
    'busqueda_binaria_rotated_array',
    'busqueda_binaria_2d',
    'busqueda_binaria_aproximada',
    'Nodo',
    'ListaEnlazada',
    'busqueda_binaria_lista_enlazada',
    'busqueda_binaria_lista_enlazada_optimizada',
    'busqueda_binaria_lista_enlazada_con_salto',
    'busqueda_binaria_lista_enlazada_con_comparaciones',
    'crear_lista_enlazada_desde_array',
    'comparar_busquedas_lista_enlazada'
] 