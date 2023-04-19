from __future__ import annotations
from abc import ABC, abstractmethod


class FabricaPersonajes(ABC):
    @abstractmethod
    def crear_guerrero(self) -> Guerrero:
        pass

    @abstractmethod
    def crear_mago(self) -> Mago:
        pass

    @abstractmethod
    def crear_arquero(self) -> Arquero:
        pass


class Guerrero:
    def __init__(self, nombre: str, fuerza: int):
        self.nombre = nombre
        self.fuerza = fuerza

    def atacar(self):
        print(f"{self.nombre} ataca con una espada y causa {self.fuerza} de daño")


class Mago:
    def __init__(self, nombre: str, inteligencia: int):
        self.nombre = nombre
        self.inteligencia = inteligencia

    def lanzar_hechizo(self):
        print(f"{self.nombre} lanza una bola de fuego y causa {self.inteligencia} de daño")


class Arquero:
    def __init__(self, nombre: str, destreza: int):
        self.nombre = nombre
        self.destreza = destreza

    def disparar_flecha(self):
        print(f"{self.nombre} dispara una flecha y causa {self.destreza} de daño")


class FabricaNivelFacil(FabricaPersonajes):
    def crear_guerrero(self) -> Guerrero:
        return Guerrero("Guerrero Fácil", 10)

    def crear_mago(self) -> Mago:
        return Mago("Mago Fácil", 10)

    def crear_arquero(self) -> Arquero:
        return Arquero("Arquero Fácil", 10)


class FabricaNivelDificil(FabricaPersonajes):
    def crear_guerrero(self) -> Guerrero:
        return Guerrero("Guerrero Difícil", 20)

    def crear_mago(self) -> Mago:
        return Mago("Mago Difícil", 20)

    def crear_arquero(self) -> Arquero:
        return Arquero("Arquero Difícil", 20)


def jugar_juego(fabrica: FabricaPersonajes):
    guerrero = fabrica.crear_guerrero()
    mago = fabrica.crear_mago()
    arquero = fabrica.crear_arquero()

    guerrero.atacar()
    mago.lanzar_hechizo()
    arquero.disparar_flecha()


if __name__ == "__main__":
    print("Jugando el juego con la fábrica de nivel fácil:")
    jugar_juego(FabricaNivelFacil())

    print()

    print("Jugando el juego con la fábrica de nivel difícil:")
    jugar_juego(FabricaNivelDificil())
