from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}\n"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""

class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass

class Hamburguesa(Product):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """
    @abstractmethod
    def operation(self) -> str:
        pass

class EntregaMostrador(Hamburguesa):
    def operation(self) -> str:
        return "Hamburguesa entregada en mostrador"


class RetiroCliente(Hamburguesa):
    def operation(self) -> str:
        return "Hamburguesa lista para retirar por el cliente"


class EntregaDelivery(Hamburguesa):
    def operation(self) -> str:
        return "Hamburguesa entregada por delivery"


class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """
    def factory_method(self) -> Product:
        return EntregaMostrador()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return RetiroCliente()


class ConcreteCreator3(Creator):
    def factory_method(self) -> Product:
        return EntregaDelivery()

if __name__ == "__main__":
    creator = ConcreteCreator1()
    hamburguesa = creator.factory_method()
    print(hamburguesa.operation())  # Hamburguesa entregada en mostrador
    print(creator.some_operation())

    creator = ConcreteCreator2()
    hamburguesa = creator.factory_method()
    print(hamburguesa.operation())  # Hamburguesa lista para retirar por el cliente
    print(creator.some_operation())

    creator = ConcreteCreator3()
    hamburguesa = creator.factory_method()
    print(hamburguesa.operation())  # Hamburguesa lista para entregar por delivery
    print(creator.some_operation())