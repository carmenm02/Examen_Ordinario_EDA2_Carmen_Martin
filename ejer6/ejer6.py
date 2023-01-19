import random

class Stormtrooper:
    def __init__(self, name, rango):
        self.name = name
        self.rango = rango
        print("Stormtrooper creado")
    
    def clasificacion(self):
        legion = self.name.split("-")[0]
        print("Codigo de legion: " + legion)
        print("Identificdor de cohoerte: " + self.name.split("-")[1][0])
        print("Identificador de siglo: " + self.name.split("-")[1][1])
        print("Identificador de escuadra: " + self.name.split("-")[1][2])
        print("Numero de trooper: " + self.name.split("-")[1][3])
    