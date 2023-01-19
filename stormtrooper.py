class Stormtrooper:      
    def __init__(self,name,rango) :
        self.name = name
        self.rango = rango
        print("Stormtrooper creado con éxito")

    def calificacion(self):
        rangos = {"cadete": 1, "cabo": 2, "sargento": 3, "teniente": 4, "capitan": 5}
        if self.rango in rangos:
            return rangos[self.rango]
        else:
            return "Rango desconocido"