import os

# *--------------------------------------------------------------------
# * Ejemplo de design pattern de tipo state
# *--------------------------------------------------------------------
"""State class: Base State class"""


class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

    def setMemory(self, memory):
        print("Guardando estación {} en M{}".format(self.stations[self.pos], memory))
        self.memory[memory] = self.stations[self.pos]

    def clearMemory(self, memory):
        print("Borrando M{}".format(memory))
        self.memory[memory] = None

    def goToMemory(self, memory):
        if self.memory[memory] == None:
            print("M{} no tiene estación guardada".format(memory))
        else:
            print("Yendo a M{}...".format(memory))
            print("Sintonizando... Estación {} {}".format(self.memory[memory], self.name))
            self.pos = self.stations.index(self.memory[memory])


# *------- Implementa como barrer las estaciones de AM
class AmState(State):

    def __init__(self, radio):

        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"
        self.memory = [None] * 4

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate


#*------- Implementa como barrer las estaciones de FM
"""Separate class for FM state"""
class FmState(State):

    def __init__(self, radio):

        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.memory = [None] * 4
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate


#*--------- Construye la radio con todas sus formas de sintonía
class Radio:


    def __init__(self):

        self.fmstate = FmState(self)
        self.amstate = AmState(self)

        #*--- Inicialmente en FM

        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

    def setMemory(self, memory):
        self.state.setMemory(memory)
    
    def clearMemory(self, memory):
        self.state.clearMemory(memory)
    
    def goToMemory(self, memory):
        self.state.goToMemory(memory)


if __name__ == "__main__":
    radio = Radio()

    radio.scan()
    radio.scan()
    radio.setMemory(1)
    radio.scan()
    radio.goToMemory(1)
    radio.scan()
    print()

    # Cambia a AM y sintoniza 3 estaciones AM
    radio.toggle_amfm()
    radio.scan()
    radio.setMemory(1)
    radio.scan()
    radio.scan()
    radio.goToMemory(1)
    print()

    # Cambia a FM y va a la memoria 1
    radio.toggle_amfm()
    radio.goToMemory(1)
    radio.toggle_amfm()
    radio.goToMemory(1)
    radio.goToMemory(2)