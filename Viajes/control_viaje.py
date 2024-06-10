from viaje import Viaje
from tipo_viaje import TipoViaje
from excepciones import ViajeError,FechaError

class ControlViaje:
    def registrar_viaje(self, destino, fecha_inicio, fecha_final, presupuesto_diario, tipo_viaje: TipoViaje):
        """Crea y registra un nuevo viaje."""
        try:
            viaje = Viaje(destino, fecha_inicio, fecha_final, presupuesto_diario, tipo_viaje)
            viaje.registrar_viaje_archivo()
            return viaje
        except (ViajeError, FechaError) as e:
            print(f"Error al registrar el viaje: {e}")
            return None

    def obtener_gastos(self, viaje):
        """Obtiene la lista de gastos de un viaje."""
        return viaje.gastos

    def agregar_gasto(self, viaje, gasto):
        """Agrega un gasto a la lista de gastos de un viaje."""
        try:
            viaje.agregar_gasto(gasto)
        except FechaError as e:
            print(f"Error al agregar el gasto: {e}")
