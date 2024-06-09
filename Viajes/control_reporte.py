from reporte import Reporte

class ControlReporte:
    def generar_reporte_diario(self, viaje):
        """Genera un reporte diario de los gastos."""
        reporte = Reporte(viaje)
        reporte.generarReporteDiario()
        return reporte

    def generarr_reporte_por_tipo(self, viaje):
        """Genera un reporte de los gastos por tipo."""
        reporte = Reporte(viaje)
        reporte.generarReportePorTipo()
        return reporte
