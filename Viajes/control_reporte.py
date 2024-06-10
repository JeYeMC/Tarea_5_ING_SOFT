from reporte import Reporte
from excepciones import ViajeError

class ControlReporte:
    def generar_reporte_diario(self, viaje):
        """Genera un reporte diario de los gastos."""
        try:
            reporte = Reporte(viaje)
            reporte.generar_reporte_diario()
            return reporte
        except ViajeError as e:
            print(f"Error al generar el reporte diario: {e}")
            return None

    def generar_reporte_por_tipo(self, viaje):
        """Genera un reporte de los gastos por tipo."""
        try:
            reporte = Reporte(viaje)
            reporte.generar_reporte_por_tipo()
            return reporte
        except ViajeError as e:
            print(f"Error al generar el reporte por tipo: {e}")
            return None
