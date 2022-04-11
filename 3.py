from enum import Enum


class Naturaleza(Enum):
    ALIMENTARIA = 0.055
    SERVICIO = 0.2

class Producto():
    def __init__(self, tipo) -> None:
        self.porcentaje = tipo.value
        self.precio = 100
    
    def facturar(self):
        return self.precio + (self.precio * self.porcentaje)

class FactoryFactura():
    def crear(self, producto):
        self.producto = producto
        return self.producto

    


producto = Producto(Naturaleza.SERVICIO)
factura = FactoryFactura()
precio_neto = factura.crear(producto).facturar()
print(precio_neto)

