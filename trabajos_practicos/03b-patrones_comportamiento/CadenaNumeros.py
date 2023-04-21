from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Devuelve un manejador para que se pueda encadenar métodos.
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class PrimoHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        # Si el número es primo, lo manejamos.
        if self.es_primo(request):
            return f"{request} es primo"
        # De lo contrario, lo pasamos al siguiente manejador en la cadena.
        else:
            return super().handle(request)

    def es_primo(self, n):
        # Comprobamos si el número es primo.
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


class ParHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        # Si el número es par, lo manejamos.
        if request % 2 == 0:
            return f"{request} es par"
        # De lo contrario, lo pasamos al siguiente manejador en la cadena.
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for i in range(1, 101):
        # Enviamos la solicitud al primer manejador de la cadena.
        print(f"\nCliente: ¿Es {i} primo o par?")
        result = handler.handle(i)
        if result:
            # Si el resultado no es nulo, lo imprimimos.
            print(f"  {result}", end="")
        else:
            # De lo contrario, imprimimos que no es ni primo ni par.
            print(f"  {i} no es ni primo ni par.", end="")


if __name__ == "__main__":
    primo = PrimoHandler()
    par = ParHandler()

    # Configuramos la cadena de responsabilidad: Primo -> Par.
    primo.set_next(par)

    print("Cadena de responsabilidad: Primo > Par")
    # Enviamos la solicitud al primer manejador de la cadena.

    client_code(primo)
