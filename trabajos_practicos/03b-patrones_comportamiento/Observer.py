from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Método abstracto para adjuntar un observador."""

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Método abstracto para separar un observador."""

    @abstractmethod
    def notify(self) -> None:
        """Método abstracto para notificar a los observadores."""


class ConcreteSubject(Subject):
    _id: str = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """Método para adjuntar un observador a la lista de observadores."""
        print("Sujeto: Adjuntando un observador.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Método para separar un observador de la lista de observadores."""
        self._observers.remove(observer)

    def notify(self) -> None:
        """Método para notificar a todos los observadores en la lista."""
        print("Sujeto: Notificando a los observadores...")
        for observer in self._observers:
            observer.update(self)

    def actualizar_id(self, id) -> None:
        """Método para actualizar el ID del sujeto y notificar a los observadores."""
        print("\nSujeto: Estableciendo un ID...")
        self._id = id
        print(f"Sujeto: Mi ID ha cambiado a: {self._id}")
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        """Método abstracto para actualizar el estado del observador en respuesta a una notificación."""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        """Método para imprimir un mensaje si el ID del sujeto es 'ISII'."""
        if subject._id == 'ISII':
            print("ConcreteObserverA: El ID del sujeto es ISII")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        """Método para imprimir un mensaje si el ID del sujeto es 'LESS'."""
        if subject._id == 'LESS':
            print("ConcreteObserverB: El ID del sujeto es LESS")

class ConcreteObserverC(Observer):
    def update(self, subject: Subject) -> None:
        """Método para imprimir un mensaje si el ID del sujeto es 'AJHR'."""
        if subject._id == 'AJHR':
            print("ConcreteObserverC: El ID del sujeto es AJHR")

class ConcreteObserverD(Observer):
    def update(self, subject: Subject) -> None:
        """Método para imprimir un mensaje si el ID del sujeto es 'KJFB'."""
        if subject._id == 'KJFB':
            print("ConcreteObserverD: El ID del sujeto es KJFB")


if __name__ == "__main__":

    # Crear un objeto ConcreteSubject.
    subject = ConcreteSubject()

    # Agregar cuatro observadores al objeto ConcreteSubject.
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    observer_c = ConcreteObserverC()
    subject.attach(observer_c)

    observer_d = ConcreteObserverD()
    subject.attach(observer_d)

    # Lista de posibles IDs.
    ids = ['ISII', 'LESS', 'AJHR', 'KJFB', 'ADSA']

    # Actualizar el ID del objeto
    for i in range(8):
        # Seleccionar un ID aleatorio.
        subject.actualizar_id(choice(ids))