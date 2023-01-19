class NodoArbol:
    def __init__(self,simbolo,freq):
        self.simbolo = simbolo
        self.freq = freq
        self.izquierda = None
        self.derecha = None
        self.padre = None
    
    def ordenar_nodos(lista_nodos):
        lista_nodos = sorted(lista_nodos,key=lambda x: x.simbolo)
        lista_nodos = sorted(lista_nodos,key=lambda x: x.freq)
        return lista_nodos
    
    def insertar_nodo(lista_nodos,nodo):
        for i in range(len(lista_nodos)):
            if nodo.freq < lista_nodos[i].freq:
                lista_nodos.insert(i,nodo)
            if i == len(lista_nodos)-1:
                lista_nodos.append(nodo)
                break
        return lista_nodos
    
    def crear_arbol(simbolos,frecuencias):
        nodos = []
        for i in range(len(simbolos)):
            nodos.append(NodoArbol(simbolos[i],frecuencias[i]))
        nodos = NodoArbol.ordenar_nodos(nodos)
        while len(nodos) > 1:
            nodo = NodoArbol('XX',nodos[0].freq+nodos[1].freq)')
            nodo.izquierda = nodos[0]
            nodo.izquierda.padre = nodo
            nodo.derecha = nodos[1]
            nodo.derecha.padre = nodo
            nodos = insertar_nodo(nodos,nodo)
            nodos.pop(0)
            nodos.pop(1)
            return nodos[0]
    def buscar(raiz,clave):
        p = 0
        if raiz.simbolo == clave:
            p = raiz
            return p
        elif p is None:
            p = buscar(raiz.izquierda,clave)
        elif p is None:
            p = buscar(raiz.derecha,clave)
        return p
    def codificar(raiz,mensaje):
        codigo = []
        mensaje = mensaje[::-1]
        for m in mensaje:
            nodo = buscar(raiz,m)
            while nodo.padre is not None:
                if nodo.padre.izquierda == nodo:
                    codigo.append(0)
                else:
                    codigo.append(1)
                nodo = nodo.padre
            codigo = codigo[::-1]
        return codigo
    