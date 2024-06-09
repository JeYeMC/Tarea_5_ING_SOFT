from datetime import datetime

class Reporte:
    def __init__(self, viaje):
        """Inicializa un nuevo reporte con la lista de gastos."""
        self.gastos = viaje.gastos
        self.destino = viaje.destino

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

            fecha_formateada = str(fecha).split(' ')
            filename = f"reporteDiario_{fecha_formateada[0]}.txt"

            with open(filename, 'a') as file:
                file.write(f"Viaje a: {self.destino}\n")
                file.write(f"Fecha: {fecha}, Efectivo: {valores['efectivo']}, Tarjeta: {valores['tarjeta']}, Total: {valores['efectivo'] + valores['tarjeta']}\n\n")
                

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
            with open(f'reportePorTipo{str(tipo)}.txt', 'a') as file:
                file.write(f"Viaje a: {self.destino}\n")
                file.write(f"Tipo: {tipo}, Efectivo: {valores['efectivo']}, Tarjeta: {valores['tarjeta']}, Total: {valores['efectivo'] + valores['tarjeta']}\n\n")
