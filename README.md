<h1 align="center">	Examen Ordinario</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/carmenm02/Examen_Ordinario_EDA2_Carmen_Martin.git)

## Ejercicio 1:

**SOLUCION**
```
from enum import Enum
class TipoStrom(Enum):
    FL = 0
    TF = 1
    TK = 2
    CT = 3
    FN = 4
    FO = 5
class Stormtrooper(Enum):      
    def __init__(self,name,rango,x,y,z,t) :
        self.name = name
        self.rango = rango
        self.identificador_cohoerte = x
        self.identificador_siglo = y
        self.identificador_escuadra = z
        self.numero_trooper = t

        print("Stormtrooper creado con éxito")
    def calificacion(self,a):
        legion = a.lower()
        e = None
        for i in TipoStrom:
            if legion == i.name:
                a = i.value.split("-")
                e = Stormtrooper(a[0],a[1].append(0),a[1].append(1),a[1].append(2),a[1].append(3))
                break
        if type(e) != Stormtrooper:
            print("Legion no encontrada")
        return e

stormtrooper_lista = [Stormtrooper("AK-3654",7),Stormtrooper("LF-2564",7),Stormtrooper("TK-8154",7),Stormtrooper("TL-8654",7)]
for stormtrooper in stormtrooper_lista:
    stormtrooper.calificacion()
  
```
## Ejercicio 2:

**SOLUCION**
```
from enum import Enum
class TipoStrom(Enum):
    FL = 0
    TF = 1
    TK = 2
    CT = 3
    FN = 4
    FO = 5
class Stormtrooper(Enum):      
    def __init__(self,name,rango,x,y,z,t) :
        self.name = name
        self.rango = rango
        self.identificador_cohoerte = x
        self.identificador_siglo = y
        self.identificador_escuadra = z
        self.numero_trooper = t

        print("Stormtrooper creado con éxito")
    def calificacion(self,a):
        legion = a.lower()
        e = None
        for i in TipoStrom:
            if legion == i.name:
                a = i.value.split("-")
                e = Stormtrooper(a[0],a[1].append(0),a[1].append(1),a[1].append(2),a[1].append(3))
                break
        if type(e) != Stormtrooper:
            print("Legion no encontrada")
        return e
    def __str__(self):
        return '\nNombre: ' + self.name + '\nRango: ' + self.rango + '\nIdentificador Cohorte: ' + self.identificador_cohoerte + '\nIdentificador Siglo: ' + self.identificador_siglo + '\nIdentificador Escuadra: ' + self.identificador_escuadra + '\nNumero de Trooper: ' + self.numero_trooper
    

stormtrooper_lista = [Stormtrooper("AK-3654",7),Stormtrooper("LF-2564",7),Stormtrooper("TK-8154",7),Stormtrooper("TL-8654",7)]
for stormtrooper in stormtrooper_lista:
    stormtrooper.calificacion()

 
```
## Ejercicio 3:

**SOLUCION**
```
from datetime import datetime

class ArtefactosValiosos:
    def __init__(self, nombre, peso, precio, fecha):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio
        self.fecha = fecha
        print("Artefacto creado con éxito")
    
    def __str__(self):
        return '\nNombre: ' + self.nombre + '\nPeso: ' + self.peso + '\nPrecio: ' + self.precio + '\nFecha: ' + self.fecha
    
    def sortByDate(self, elem):
        return datetime.strptime(elem.fechaCaducidad, '%d/%m/%Y')
    
lista = [ArtefactosValiosos("Artefacto 1", "10kg", "1000$", "01/01/2020"), ArtefactosValiosos("Artefacto 2", "20kg", "2000$", "02/02/2020"), ArtefactosValiosos("Artefacto 3", "30kg", "3000$", "03/03/2020"), ArtefactosValiosos("Artefacto 4", "40kg", "4000$", "04/04/2020")]
lista.sort(key=sortByDate)
for stormtrooper in lista:
    print(stormtrooper)
print("Precio cambiado")
lista[0].precio = 4000
print(lista[0])
```
## Ejercicio 4:

**SOLUCION**
```
from datatime import datetime
class ArtefactosValiosos:
    def __init__(self, nombre, peso, precio, fecha):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio
        self.fecha = fecha
        print("Artefacto creado con éxito")
    
    def __str__(self):
        return '\nNombre: ' + self.nombre + '\nPeso: ' + self.peso + '\nPrecio: ' + self.precio + '\nFecha: ' + self.fecha
    
    def sortByDate(self, elem):
        return datetime.strptime(elem.fechaCaducidad, '%d/%m/%Y')
    
    def usarFuerza(mochila,numObjetos):
        if (len(mochila)>0):
            if mochila[len(mochila) - 1].nombre == "Sable de luz":
                print("Se han sacado" + str(numObjetos) + "objetos de la mochila")
            else:
                print("No hay mas objetos en la mochila")
numObjetos = 0
mochila = [ArtefactosValiosos("Linterna", 500, 20, "05/28/2022"), ArtefactosValiosos("Sable de Luz", 500, 20, "05/28/2022"), ArtefactosValiosos("Esmeralda", 500, 20, "05/28/2022") ,ArtefactosValiosos("Diamante", 500, 20, "05/28/2022")]
usarFuerza(mochila,numObjetos)
```
## Ejercicio 5:

**SOLUCION**
```
def mochila(n,w,v,peso):
    if n == 0 or peso == 0:
        return 0
    if peso[n-1] > w:
        return mochila(n-1,w,v,peso)
    else:
        return max(v[n-1] + mochila(n-1,w-peso[n-1],v,peso), mochila(n-1,w,v,peso))
def main():
    precio = [103,60,70,5,15]
    pesos = [12,23,11,15,7]
    pesomax = 100
    n = len(precio)
    valor_maximo = mochila(n,pesomax,precio,pesos)

if __name__ == '__main__':
    main()
```
## Ejercicio 6:

**SOLUCION**
```

```
## Ejercicio 7:

**SOLUCION**
```
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
    def decodificar(raiz,codigo):
        mensaje = []
        nodo = raiz
        for c in codigo:
            if c == 0:
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha
            if nodo.simbolo != 'XX':
                mensaje.append(nodo.simbolo)
                nodo = raiz
        return mensaje
    
```
## Ejercicio 8:

**SOLUCION**
```
import networkx as nx
import random

g = nx.Graph()
planetas = ['Alderaan', 'Endor', 'Dagobah', 'Hoth', 'Tatooine', 'Kamino', 'Naboo', 'Mustafar', 'Scarif', 'Bespin', 'Cantonica', 'DQar', 'Dantooine', 'Atollon', 'Jedha', 'Corellia', 'Coruscant']

g.add_node('Alderaan')
g.add_node('Endor')
g.add_node('Dagobah')
g.add_node('Hoth')
g.add_node('Tatooine')
g.add_node('Kamino')
g.add_node('Naboo')
g.add_node('Mustafar')
g.add_node('Scarif')
g.add_node('Bespin')
g.add_node('Cantonica')
g.add_node('DQar')
g.add_node('Dantooine')
g.add_node('Atollon')
g.add_node('Jedha')
g.add_node('Corellia')
g.add_node('Coruscant')

for node in g.nodes():
    for i in range(4):
        other_node = random.choice(list(g.nodes()))
        while other_node == node:
            other_node = random.choice(list(g.nodes()))
        weight = random.randint(1, 10)
        g.add_edge(node, other_node, weight=weight)

t = nx.minimum_spanning_tree(g)

dist1 = nx.shortest_path_length(t, 'Tatoine', 'Endor')
dist2 = nx.shortest_path_length(t, 'Tatoine', 'Dagobah')
dist3 = nx.shortest_path_length(t, 'Tatoine', 'Hoth')

print(dist1)
print(dist2)
print(dist3)

neighbors = list(t.neighbors('Tatoine'))
print(neighbors)
```

