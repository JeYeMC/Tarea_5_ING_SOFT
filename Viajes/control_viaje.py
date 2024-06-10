from viaje import Viaje
from tipo_viaje import TipoViaje
from excepciones import ViajeError,FechaError

class ControlViaje:
    def registrarViaje(self, destino, fechaInicio, fechaFinal, presupuestoDiario, tipoViaje: TipoViaje):
        """Crea y registra un nuevo viaje."""
        try:
            viaje = Viaje(destino, fechaInicio, fechaFinal, presupuestoDiario, tipoViaje)
            viaje.registrarViajeArchivo()
            return viaje
        except (ViajeError, FechaError) as e:
            print(f"Error al registrar el viaje: {e}")
            return None

    def obtenerGastos(self, viaje):
        """Obtiene la lista de gastos de un viaje."""
        return viaje.gastos

    def agregarGasto(self, viaje, gasto):
        """Agrega un gasto a la lista de gastos de un viaje."""
        try:
            viaje.agregarGasto(gasto)
        except FechaError as e:
            print(f"Error al agregar el gasto: {e}")
