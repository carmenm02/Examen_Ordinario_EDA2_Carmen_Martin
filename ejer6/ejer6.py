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
    def __str__(self):
        return '\nNombre: ' + self.name + '\nRango: ' + str(self.rango)
    
    lista = ["FL","TF","TK","CT","FN","FO"]
    for i in range(2000):
        numRandom = random.randint(0,5)
        listanum = []
        for j in range(4):
            listanum.append(random.randint(0,9))

        num = "".join(listanum)
        codlegion = lista[numRandom]
        Stormtrooper = Stormtrooper(codlegion + "-" + num, 7)
        print(Stormtrooper)