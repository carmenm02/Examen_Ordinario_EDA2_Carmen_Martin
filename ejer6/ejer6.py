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
    
    hashtresdigitos = {}
    lista = ["FL","TF","TK","CT","FN","FO"]
    for i in range(2000):
        numRandom = random.randint(0,5)
        listanum = []
        for j in range(4):
            listanum.append(random.randint(0,9))

        num = "".join(listanum)
        tresdigitos ="".join(listanum[1:])
        codlegion = lista[numRandom]
        Stormtrooper = Stormtrooper(codlegion + "-" + num, 7)
        if hashtresdigitos.get(tresdigitos):
            hashtresdigitos[tresdigitos][codlegion] = Stormtrooper
        else:
            hashtresdigitos[tresdigitos] = {}
            hashtresdigitos[tresdigitos][codlegion] = Stormtrooper
        
        s = Stormtrooper("FN-2187",7)
        hashtresdigitos['187']['FN'] = s
        if hashtresdigitos.get('187').get('FN').nombre == "FN-2187":
            print("Eliminado FN-2187")
        
        misionDesalto = []
        misionExplorar = []

        if (hashtresdigitos('781')):
            for i in hashtresdigitos('781'.keys():
                misionDesalto.append(i)
        if (hashtresdigitos('537')):
            for i in hashtresdigitos('537'.keys():
                misionExplorar.append(i)
        print("Mision desalto")
        print(misionDesalto)
        print("Mision explorar")
        print(misionExplorar)
        
