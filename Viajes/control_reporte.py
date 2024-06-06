from reporte import Reporte

class ControlReporte:
    def generarReporteDiario(self, gastos):
        """Genera un reporte diario de los gastos."""
        reporte = Reporte(gastos)
        reporte.generarReporteDiario()
        return reporte

    def generarReportePorTipo(self, gastos):
        """Genera un reporte de los gastos por tipo."""
        reporte = Reporte(gastos)
        reporte.generarReportePorTipo()
        return reporte
