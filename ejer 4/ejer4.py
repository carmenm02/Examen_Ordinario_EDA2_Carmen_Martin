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
    
    