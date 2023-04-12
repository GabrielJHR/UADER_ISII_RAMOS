#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class FactorialSingleton(metaclass=SingletonMeta):
    """
    Una clase para calcular el factorial de un numero.
    """
    def calcular_factorial(self, num):
        """
        Calcula el factorial de un numero usando recursividad.
        """
        if num == 0:
            return 1
        else:
            return num * self.calcular_factorial(num-1)
        
s1 = FactorialSingleton()
s2 = FactorialSingleton()

if s1 == s2:
    print("Las instancias son iguales")
else:
    print("Las instancias son distintas")

num = int(input("Ingresa un numero para calcular su factorial: "))

print(f"El factorial de {num} es {s1.calcular_factorial(num)}")