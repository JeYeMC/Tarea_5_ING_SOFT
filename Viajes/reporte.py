from excepciones import ViajeError

class Reporte:
    def __init__(self, viaje):
        """Inicializa un nuevo reporte con la lista de gastos."""
        self.gastos = viaje.gastos
        self.destino = viaje.destino

    def generarReporteDiario(self):
        """Genera un reporte diario de los gastos."""
        try:
            reporte = {}
            for gasto in self.gastos:
                if gasto.fecha not in reporte:
                    reporte[gasto.fecha] = {'efectivo': 0, 'tarjeta': 0}
                if gasto.metodoPago.value == 'efectivo':
                    reporte[gasto.fecha]['efectivo'] += gasto.valor
                else:
                    reporte[gasto.fecha]['tarjeta'] += gasto.valor

            with open("reporteDiario.txt", 'a') as file:
                file.write(f"Viaje a: {self.destino}\n")

            for fecha, valores in reporte.items():
                with open("reporteDiario.txt", 'a') as file:
                    file.write(f"Fecha: {fecha}, Efectivo: {valores['efectivo']}, Tarjeta: {valores['tarjeta']}, Total: {valores['efectivo'] + valores['tarjeta']}\n\n")
        except IOError as e:
            raise ViajeError(f"Error al generar el reporte diario: {e}")

    def generarReportePorTipo(self):
        """Genera un reporte de los gastos por tipo."""
        try:
            reporte = {}
            for gasto in self.gastos:
                if gasto.tipoGasto.value not in reporte:
                    reporte[gasto.tipoGasto.value] = {'efectivo': 0, 'tarjeta': 0}
                if gasto.metodoPago.value == 'efectivo':
                    reporte[gasto.tipoGasto.value]['efectivo'] += gasto.valor
                else:
                    reporte[gasto.tipoGasto.value]['tarjeta'] += gasto.valor

            with open("reportePorTipo.txt", 'a') as file:
                file.write(f"Viaje a: {self.destino}\n")

            for tipo, valores in reporte.items():
                with open('reportePorTipo.txt', 'a') as file:
                    file.write(f"Tipo: {tipo}, Efectivo: {valores['efectivo']}, Tarjeta: {valores['tarjeta']}, Total: {valores['efectivo'] + valores['tarjeta']}\n\n")
        except IOError as e:
            raise ViajeError(f"Error al generar el reporte por tipo: {e}")
