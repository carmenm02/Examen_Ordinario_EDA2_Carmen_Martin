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