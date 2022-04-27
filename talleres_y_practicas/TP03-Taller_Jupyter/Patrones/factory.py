#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    La clase Creator declara el método de fábrica que se supone que devolverá 
    un objeto de una clase Product. Las subclases de Creator generalmente 
    proporcionan la implementación de este método.
    """

    @abstractmethod
    def factory_method(self):
        """
        Tenga en cuenta que el Creador también puede proporcionar alguna 
        implementación predeterminada del método de fábrica.
        """
        pass

    def some_operation(self) -> str:
        """
        También tenga en cuenta que, a pesar de su nombre, la responsabilidad 
        principal del Creador no es crear productos. Por lo general, 
        contiene alguna lógica comercial central que se basa en los objetos 
        Producto, devueltos por el método de fábrica.
		Las subclases pueden cambiar indirectamente esa lógica empresarial 
		anulando el método de fábrica y devolviendo un tipo diferente de producto.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creadora: El mismo código del creador acaba de funcionar con {product.operation()}\n"

        return result


"""
Concrete Creators anula el método de fábrica para cambiar el tipo de producto resultante.
"""


class ConcreteCreator1(Creator):
    """
	Tenga en cuenta que la firma del método todavía utiliza el tipo de 
	producto abstracto, aunque el método devuelve el producto concreto. 
	De esta manera, el Creador puede mantenerse independiente de 
	las clases de productos concretos.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    La interfaz Producto declara las operaciones que todos los 
    productos concretos deben implementar.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products proporciona varias implementaciones de la interfaz del Producto.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Resultado del ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Resultado del ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Cliente: No conozco la clase del creador, pero aún asi funciona.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":

    print("\n\n")
    print("App: Lanzada con ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Lanzada con ConcreteCreator2.")
    client_code(ConcreteCreator2())
