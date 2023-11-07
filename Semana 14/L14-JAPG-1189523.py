class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = True
        self.tipoCambioDolar = 0.0
        self.descuentoAplicado = 0.0

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"
        
    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        self.precio -= self.descuentoAplicado
        self.DefinirPrecio(self.precio)

    def MostrarInformacion(self):
        precio_en_dolares = self.precio / self.tipoCambioDolar
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}. Precio en dólares: ${precio_en_dolares}. {self.MostrarDisponibilidad()}. Descuento aplicado: Q{self.descuentoAplicado}"

automovil1 = Automovil()
automovil1.DefinirMarca("Toyota")
automovil1.DefinirModelo(2023)
automovil1.DefinirPrecio(50000.0)
automovil1.DefinirTipoCambio(7.0)
automovil1.CambiarDisponibilidad()
automovil1.AplicarDescuento(5000.0)

print(automovil1.MostrarInformacion())