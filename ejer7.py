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