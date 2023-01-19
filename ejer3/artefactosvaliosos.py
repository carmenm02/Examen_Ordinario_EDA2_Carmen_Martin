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