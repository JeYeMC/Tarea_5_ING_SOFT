from reporte import Reporte
from excepciones import ViajeError

class ControlReporte:
    def generarReporteDiario(self, viaje):
        """Genera un reporte diario de los gastos."""
        try:
            reporte = Reporte(viaje)
            reporte.generarReporteDiario()
            return reporte
        except ViajeError as e:
            print(f"Error al generar el reporte diario: {e}")
            return None

    def generarReportePorTipo(self, viaje):
        """Genera un reporte de los gastos por tipo."""
        try:
            reporte = Reporte(viaje)
            reporte.generarReportePorTipo()
            return reporte
        except ViajeError as e:
            print(f"Error al generar el reporte por tipo: {e}")
            return None
