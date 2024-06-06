from gasto import Gasto

class Reporte:
    def __init__(self, gastos):
        """Inicializa un nuevo reporte con la lista de gastos."""
        self.gastos = gastos

    def generarReporteDiario(self):
        """Genera un reporte diario de los gastos."""
        reporte = {}
        for gasto in self.gastos:
            if gasto.fecha not in reporte:
                reporte[gasto.fecha] = {'efectivo': 0, 'tarjeta': 0}
            if gasto.metodoPago.value == 'efectivo':
                reporte[gasto.fecha]['efectivo'] += gasto.valor
            else:
                reporte[gasto.fecha]['tarjeta'] += gasto.valor
        for fecha, valores in reporte.items():
            print(f"Fecha: {fecha}, Efectivo: {valores['efectivo']}, Tarjeta: {valores['tarjeta']}, Total: {valores['efectivo'] + valores['tarjeta']}")

    def generarReportePorTipo(self):
        """Genera un reporte de los gastos por tipo."""
        reporte = {}
        for gasto in self.gastos:
            if gasto.tipoGasto.value not in reporte:
                reporte[gasto.tipoGasto.value] = {'efectivo': 0, 'tarjeta': 0}
            if gasto.metodoPago.value == 'efectivo':
                reporte[gasto.tipoGasto.value]['efectivo'] += gasto.valor
            else:
                reporte[gasto.tipoGasto.value]['tarjeta'] += gasto.valor
        for tipo, valores in reporte.items():
            print(f"Tipo: {tipo}, Efectivo: {valores['efectivo']}, Tarjeta: {valores['tarjeta']}, Total: {valores['efectivo'] + valores['tarjeta']}")
