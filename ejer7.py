class NodoArbol:
    def __init__(self,simbolo,freq):
        self.simbolo = simbolo
        self.freq = freq
        self.izquierda = None
        self.derecha = None
        self.padre = None