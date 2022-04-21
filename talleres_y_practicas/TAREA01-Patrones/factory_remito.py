from __future__ import annotations
from abc import ABC, abstractmethod

# Clases creadoras
class Creator(ABC):
    @abstractmethod
    def crear_producto(self):
        pass

    def enviar_remito(self) -> str:
        medio = self.crear_producto()
        return "El remito fue distribuido mediante " + medio.obtener_medio() + "."

class CorreoCreator(Creator):
    def crear_producto(self) -> Product:
        return ConcreteCorreo()

class MensajeriaCreator(Creator):
    def crear_producto(self) -> Product:
        return ConcreteMensajeria()

class PortalVentaCreator(Creator):
    def crear_producto(self) -> Product:
        return ConcretePortalVentas()

# Clases de productos
class Product(ABC):
    @abstractmethod
    def obtener_medio(self) -> str:
        pass

class ConcreteCorreo(Product):
    def obtener_medio(self) -> str:
        return "Correo"

class ConcreteMensajeria(Product):
    def obtener_medio(self) -> str:
        return "Mensajeria"

class ConcretePortalVentas(Product):
    def obtener_medio(self) -> str:
        return "Portal de ventas"
