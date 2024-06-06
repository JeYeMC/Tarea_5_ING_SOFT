from viaje import Viaje
from tipo_viaje import TipoViaje

class ControlViaje:
    def registrarViaje(self, destino, fechaInicio, fechaFinal, presupuestoDiario, tipoViaje: TipoViaje):
        """Crea y registra un nuevo viaje."""
        viaje = Viaje(destino, fechaInicio, fechaFinal, presupuestoDiario, tipoViaje)
        viaje.registrarViaje()
        return viaje

    def obtenerGastos(self, viaje):
        """Obtiene la lista de gastos de un viaje."""
        return viaje.gastos

    def agregarGasto(self, viaje, gasto):
        """Agrega un gasto a la lista de gastos de un viaje."""
        viaje.agregarGasto(gasto)
