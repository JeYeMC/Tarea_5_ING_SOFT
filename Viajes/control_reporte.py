from reporte import Reporte

class ControlReporte:
    def generar_reporte_diario(self, gastos):
        """Genera un reporte diario de los gastos."""
        reporte = Reporte(gastos)
        reporte.generarReporteDiario()
        return reporte

    def generarr_reporte_por_tipo(self, gastos):
        """Genera un reporte de los gastos por tipo."""
        reporte = Reporte(gastos)
        reporte.generarReportePorTipo()
        return reporte
