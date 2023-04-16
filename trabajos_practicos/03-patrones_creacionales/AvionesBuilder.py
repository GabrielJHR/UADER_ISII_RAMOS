import os

# Define las partes genéricas para un vehículo (sin inicializar)
class Body:
    shape = None

class Wheel:
    size = None

class Wing:
    size = None

class LandingGear:
    size = None

class Turbine:
    rpm = None

# Clase Director orquesta la construcción del objeto indicando el orden en que deben llamarse sus componentes
class Director:
    __builder = None
    
    def setBuilder(self, builder):
        self.__builder = builder
        
    def getVehicle(self):
        vehicle = Vehicle()
        
        # Primero el cuerpo
        body = self.__builder.getBody()
        vehicle.setBody(body)
        
        # Luego el motor
        wing1 = self.__builder.getTurbine()
        wing2 = self.__builder.getTurbine()
        vehicle.attachTurbine(wing1)
        vehicle.attachTurbine(wing2)
        
        # Luego las alas
        wing1 = self.__builder.getWing()
        wing2 = self.__builder.getWing()
        vehicle.attachWing(wing1)
        vehicle.attachWing(wing2)

        # Luego el tren de aterrizaje
        landing_gear = self.__builder.getLandingGear()
        vehicle.attachLandingGear(landing_gear)

        # Retorna el vehiculo completo
        return vehicle

# Esta es la definición de un objeto Vehicle inicializando todos sus atributos
class Vehicle:
    def __init__(self):
        self.__body = None
        self.__turbines = []
        self.__wings = []
        self.__landing_gear = None

    def setBody(self, body):
        self.__body = body

    def attachTurbine(self, turbine):
        self.__turbines.append(turbine)

    def attachWing(self, wing):
        self.__wings.append(wing)

    def attachLandingGear(self, landing_gear):
        self.__landing_gear = landing_gear

    def specification(self):
        print ("Cuerpo: %s" % (self.__body.shape))
        print ("Turbinas RPM: %d" % (self.__turbines[0].rpm))
        print ("Alas: %d\'" % (self.__wings[0].size))
        print ("Tren de aterrizaje: %d\'" % (self.__landing_gear.size))

# Builder
# Clase genérica que solo define la interfaz de los métodos que el Builder específico tiene que implementar
class Builder:
    def getBody(self): pass
    def getTurbine(self): pass
    def getWing(self): pass
    def getLandingGear(self): pass

# Esta es la hoja de ruta para construir un avión
class AirplaneBuilder(Builder):
    def getBody(self):
        body = Body()
        body.shape = "Airplane"
        return body
    
    def getTurbine(self):
        turbine = Turbine()
        turbine.rpm = 10000
        return turbine

    def getWing(self):
        wing = Wing()
        wing.size = 200
        return wing

    def getLandingGear(self):
        landing_gear = LandingGear()
        landing_gear.size = 20
        return landing_gear
    
def main():
    # Instancia el builder para aviones
    airplaneBuilder = AirplaneBuilder()
    director = Director()

    # Pasa al director la hoja de ruta para construir un avión
    director.setBuilder(airplaneBuilder)

    # Ordena al director agregar los componentes de un avión según la hoja de ruta
    airplane = director.getVehicle()

    # Finalizada la construcción verifica que sea completa
    airplane.specification()
    print("\n\n")

if __name__ == "__main__":
    os.system("cls")
    print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avion\n")

    main()