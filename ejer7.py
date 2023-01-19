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
