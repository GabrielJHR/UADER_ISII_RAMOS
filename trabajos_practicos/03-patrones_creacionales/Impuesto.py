# Define la clase "Impuesto"
class Impuesto():
    """Define la clase impuesto la cual recibe una base inponible y calcula la cantidad
    de impuesto"""

    # Constructor de la clase, recibe un parámetro "base"
    def __init__(self, base) -> None:
        self.base = base  # Inicializa el atributo "base" con el valor recibido
        self.iva = 21  # Inicializa el atributo "iva" con el valor 21%
        self.iibb = 5  # Inicializa el atributo "iibb" con el valor 5%
        self.municipal = 1.2  # Inicializa el atributo "municipal" con el valor 1.2%

    # Método "calcular_impuesto" que calcula el impuesto total a partir de la base
    def calcular_impuesto(self):
        """Multiplica la base por la suma del IVA, IIBB y el impuesto municipal
        y divide el resultado por 100 para obtener el valor en porcentaje."""
        return self.base * (self.iva + self.iibb + self.municipal) / 100


# Crea una instancia de la clase "Impuesto" con una base de 100
im = Impuesto(100)

# Llama al método "calcular_impuesto" de la instancia "im" e imprime el resultado en pantalla
print(im.calcular_impuesto())
