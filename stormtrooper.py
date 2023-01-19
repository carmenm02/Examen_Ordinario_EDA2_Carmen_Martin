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
        
