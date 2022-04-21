#  Desarrolle indicadas: los siguientes patrones para las situaciones.
import singleton_empresa as singleton
import factory_remito as factory
import factura_builder

#  • Obtener el CUIT de la empresa.
if __name__ == "__main__":
    s1 = singleton.Singleton()
    s2 = singleton.Singleton()

    if(id(s1) == id(s2)):
        print('El cuit de la empresa es', s1.obtener_cuit())



    # Implementar un remito que tenga en cuenta distribución por correo, 
    # por mensajería o por portal de ventas.
    creador1 = factory.CorreoCreator()
    print(creador1.enviar_remito())

    creador2 = factory.MensajeriaCreator()
    print(creador2.enviar_remito())

    creador3 = factory.PortalVentaCreator()
    print(creador3.enviar_remito())


    # Generar una clase genérica para crear distintos tipos de factura de 
    # ventas a medida que se vaya necesitando.
    builder = factura_builder.FacturaVentaBuilder()
    builder.producto_a()
    builder.producto_b()

    print("Lista de productos custom")
    builder.factura.lista_productos()
    print()
    print("Lista de todos los productos")
    director = factura_builder.Director()
    director.builder = builder
    director.factura_venta_todos()

    builder.factura.lista_productos()
