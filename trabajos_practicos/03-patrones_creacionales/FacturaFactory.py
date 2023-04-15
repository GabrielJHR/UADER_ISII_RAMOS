from __future__ import annotations
from abc import ABC, abstractmethod

# Creamos una clase abstracta Creator, que define la interfaz para la creación
# de objetos Product.
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    # La clase Creator también puede definir una implementación por defecto de
    # algunas operaciones para sus creadores concretos.
    def some_operation(self) -> str:
        # Llama al método de fábrica para crear un objeto Product.
        product = self.factory_method()

        # Ahora, utiliza el objeto Product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}\n"

        return result

# La clase Product también es una clase abstracta. Define la interfaz para los
# objetos que la fábrica crea.
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Creamos una clase concreta Factura, que es una subclase de Product. Las
# subclases de Product son los objetos que la fábrica crea.
class Factura(Product):
    @abstractmethod
    def operation(self) -> str:
        pass

# Creamos tres subclases de Factura que representan diferentes tipos de facturas.
# Estas subclases son los objetos que la fábrica creará.
class IVAResponsable(Factura):
    """Esta clase contiene la sobreescritura de los métodos de la clase producto
    y puede contener otras operaciones como el cálculo total de la factura"""

    def operation(self) -> str:
        return "La factura corresponde a la condicion de IVA Responsable"

class IVANoInscripto(Factura):
    def operation(self) -> str:
        return "La factura corresponde a la condicion de IVA no inscripto"

class IVAExcento(Factura):
    def operation(self) -> str:
        return "La factura corresponde a la condicion de IVA exento"

# Creamos tres clases concretas de Creator, cada una de las cuales implementa el
# método factory_method para crear una instancia de una de las subclases de Factura.
class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return IVAResponsable()

class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return IVANoInscripto()

class ConcreteCreator3(Creator):
    def factory_method(self) -> Product:
        return IVAExcento()
    
if __name__ == "__main__":
    creator = ConcreteCreator1()
    factura = creator.factory_method()
    print(factura.operation())  # factura IVA inscripto
    print(creator.some_operation())

    creator = ConcreteCreator2()
    factura = creator.factory_method()
    print(factura.operation())  # factura IVA no inscripto
    print(creator.some_operation())

    creator = ConcreteCreator3()
    factura = creator.factory_method()
    print(factura.operation())  # factura IVA exento
    print(creator.some_operation())
