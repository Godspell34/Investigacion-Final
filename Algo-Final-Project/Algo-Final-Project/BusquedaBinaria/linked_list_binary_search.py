"""
Implementación de búsqueda binaria para listas enlazadas.
Incluye diferentes estrategias para manejar la falta de acceso directo por índice.
"""

class Nodo:
    """
    Nodo de una lista enlazada.
    """
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    """
    Lista enlazada simple ordenada.
    """
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
    
    def insertar_ordenado(self, valor):
        """
        Inserta un valor en la lista manteniendo el orden.
        
        Args:
            valor: Valor a insertar
        """
        nuevo_nodo = Nodo(valor)
        
        # Si la lista está vacía o el valor es menor que la cabeza
        if not self.cabeza or valor <= self.cabeza.valor:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            # Buscar la posición correcta
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.valor < valor:
                actual = actual.siguiente
            
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
        
        self.tamanio += 1
    
    def obtener_nodo_en_indice(self, indice):
        """
        Obtiene el nodo en un índice específico.
        
        Args:
            indice: Índice del nodo
            
        Returns:
            Nodo en el índice especificado, None si no existe
        """
        if indice < 0 or indice >= self.tamanio:
            return None
        
        actual = self.cabeza
        for _ in range(indice):
            actual = actual.siguiente
        
        return actual
    
    def obtener_tamanio(self):
        """
        Retorna el tamaño de la lista.
        
        Returns:
            Número de nodos en la lista
        """
        return self.tamanio
    
    def mostrar_lista(self):
        """
        Muestra la lista enlazada.
        """
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        return " -> ".join(elementos)

def busqueda_binaria_lista_enlazada(lista, objetivo):
    """
    Búsqueda binaria en lista enlazada usando acceso por índice.
    
    Args:
        lista: ListaEnlazada ordenada
        objetivo: Valor a buscar
        
    Returns:
        Nodo que contiene el objetivo, None si no se encuentra
        
    Complejidad:
        - Tiempo: O(n) debido al acceso por índice
        - Espacio: O(1)
    """
    if not lista.cabeza:
        return None
    
    izquierda = 0
    derecha = lista.obtener_tamanio() - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nodo_medio = lista.obtener_nodo_en_indice(medio)
        
        if nodo_medio.valor == objetivo:
            return nodo_medio
        elif nodo_medio.valor < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return None

def busqueda_binaria_lista_enlazada_optimizada(lista, objetivo):
    """
    Búsqueda binaria optimizada para listas enlazadas.
    Usa dos punteros que se mueven a diferentes velocidades.
    
    Args:
        lista: ListaEnlazada ordenada
        objetivo: Valor a buscar
        
    Returns:
        Nodo que contiene el objetivo, None si no se encuentra
        
    Complejidad:
        - Tiempo: O(n) en el peor caso
        - Espacio: O(1)
    """
    if not lista.cabeza:
        return None
    
    # Si el objetivo es menor que la cabeza
    if objetivo < lista.cabeza.valor:
        return None
    
    # Si el objetivo es igual a la cabeza
    if objetivo == lista.cabeza.valor:
        return lista.cabeza
    
    # Buscar usando dos punteros
    lento = lista.cabeza
    rapido = lista.cabeza.siguiente
    
    while rapido and rapido.siguiente:
        # Mover el puntero rápido dos pasos
        rapido = rapido.siguiente.siguiente
        
        # Si encontramos el objetivo en el camino
        if lento.siguiente and lento.siguiente.valor == objetivo:
            return lento.siguiente
        
        # Si el siguiente valor es mayor que el objetivo
        if lento.siguiente and lento.siguiente.valor > objetivo:
            break
        
        # Mover el puntero lento un paso
        lento = lento.siguiente
    
    # Buscar en la sección restante
    actual = lento
    while actual.siguiente:
        if actual.siguiente.valor == objetivo:
            return actual.siguiente
        elif actual.siguiente.valor > objetivo:
            break
        actual = actual.siguiente
    
    return None

def busqueda_binaria_lista_enlazada_con_salto(lista, objetivo):
    """
    Búsqueda binaria usando saltos exponenciales.
    
    Args:
        lista: ListaEnlazada ordenada
        objetivo: Valor a buscar
        
    Returns:
        Nodo que contiene el objetivo, None si no se encuentra
        
    Complejidad:
        - Tiempo: O(log n) en el mejor caso
        - Espacio: O(1)
    """
    if not lista.cabeza:
        return None
    
    # Si el objetivo es menor que la cabeza
    if objetivo < lista.cabeza.valor:
        return None
    
    # Si el objetivo es igual a la cabeza
    if objetivo == lista.cabeza.valor:
        return lista.cabeza
    
    # Encontrar el rango usando saltos exponenciales
    inicio = lista.cabeza
    fin = None
    salto = 1
    
    # Buscar el final del rango
    actual = lista.cabeza
    while actual.siguiente:
        if actual.siguiente.valor > objetivo:
            fin = actual
            break
        
        # Hacer saltos exponenciales
        for _ in range(salto):
            if actual.siguiente:
                actual = actual.siguiente
            else:
                fin = actual
                break
        
        salto *= 2
    
    if not fin:
        fin = actual
    
    # Búsqueda binaria en el rango encontrado
    return busqueda_binaria_en_rango(inicio, fin, objetivo)

def busqueda_binaria_en_rango(inicio, fin, objetivo):
    """
    Búsqueda binaria en un rango específico de la lista enlazada.
    
    Args:
        inicio: Nodo inicial del rango
        fin: Nodo final del rango
        objetivo: Valor a buscar
        
    Returns:
        Nodo que contiene el objetivo, None si no se encuentra
    """
    if not inicio or not fin:
        return None
    
    # Si el rango es muy pequeño, hacer búsqueda lineal
    if inicio == fin:
        return inicio if inicio.valor == objetivo else None
    
    # Encontrar el medio del rango
    lento = inicio
    rapido = inicio
    previo_lento = None
    
    # Usar técnica de tortuga y liebre para encontrar el medio
    while rapido != fin and rapido.siguiente != fin:
        previo_lento = lento
        lento = lento.siguiente
        rapido = rapido.siguiente.siguiente
    
    medio = lento
    
    # Comparar con el medio
    if medio.valor == objetivo:
        return medio
    elif medio.valor < objetivo:
        # Buscar en la mitad derecha
        return busqueda_binaria_en_rango(medio.siguiente, fin, objetivo)
    else:
        # Buscar en la mitad izquierda
        return busqueda_binaria_en_rango(inicio, previo_lento, objetivo)

def busqueda_binaria_lista_enlazada_con_comparaciones(lista, objetivo):
    """
    Búsqueda binaria que cuenta el número de comparaciones realizadas.
    
    Args:
        lista: ListaEnlazada ordenada
        objetivo: Valor a buscar
        
    Returns:
        Tupla (nodo, número_de_comparaciones)
    """
    if not lista.cabeza:
        return (None, 0)
    
    comparaciones = 0
    izquierda = 0
    derecha = lista.obtener_tamanio() - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        nodo_medio = lista.obtener_nodo_en_indice(medio)
        comparaciones += 1
        
        if nodo_medio.valor == objetivo:
            return (nodo_medio, comparaciones)
        elif nodo_medio.valor < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return (None, comparaciones)

def crear_lista_enlazada_desde_array(arr):
    """
    Crea una lista enlazada ordenada desde un array.
    
    Args:
        arr: Array de números
        
    Returns:
        ListaEnlazada ordenada
    """
    lista = ListaEnlazada()
    for valor in sorted(arr):
        lista.insertar_ordenado(valor)
    return lista

def comparar_busquedas_lista_enlazada(lista, objetivo):
    """
    Compara diferentes métodos de búsqueda en lista enlazada.
    
    Args:
        lista: ListaEnlazada ordenada
        objetivo: Valor a buscar
    """
    print(f"Buscando {objetivo} en: {lista.mostrar_lista()}")
    print("-" * 50)
    
    # Método 1: Búsqueda binaria con acceso por índice
    resultado1 = busqueda_binaria_lista_enlazada(lista, objetivo)
    print(f"Búsqueda binaria (índice): {resultado1.valor if resultado1 else 'No encontrado'}")
    
    # Método 2: Búsqueda binaria optimizada
    resultado2 = busqueda_binaria_lista_enlazada_optimizada(lista, objetivo)
    print(f"Búsqueda binaria (optimizada): {resultado2.valor if resultado2 else 'No encontrado'}")
    
    # Método 3: Búsqueda binaria con saltos
    resultado3 = busqueda_binaria_lista_enlazada_con_salto(lista, objetivo)
    print(f"Búsqueda binaria (saltos): {resultado3.valor if resultado3 else 'No encontrado'}")
    
    # Método 4: Con comparaciones
    resultado4, comparaciones = busqueda_binaria_lista_enlazada_con_comparaciones(lista, objetivo)
    print(f"Búsqueda binaria (comparaciones): {resultado4.valor if resultado4 else 'No encontrado'} ({comparaciones} comparaciones)")
    
    # Método 5: Búsqueda lineal (para comparación)
    comparaciones_lineal = 0
    actual = lista.cabeza
    while actual:
        comparaciones_lineal += 1
        if actual.valor == objetivo:
            print(f"Búsqueda lineal: {actual.valor} ({comparaciones_lineal} comparaciones)")
            break
        elif actual.valor > objetivo:
            print(f"Búsqueda lineal: No encontrado ({comparaciones_lineal} comparaciones)")
            break
        actual = actual.siguiente
    else:
        print(f"Búsqueda lineal: No encontrado ({comparaciones_lineal} comparaciones)") 
