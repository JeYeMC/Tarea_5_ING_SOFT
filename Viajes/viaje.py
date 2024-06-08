from datetime import datetime
from tipo_viaje import TipoViaje
from divisas import Divisa
from tipo_gasto import TipoGasto

class Viaje:
    def __init__(self, destino, fechaInicio, fechaFinal, presupuestoDiario, tipoViaje: TipoViaje):
        """Inicializa un nuevo viaje con destino, fechas, presupuesto diario y tipo de viaje."""
        self.destino = destino
        self.fechaInicio = fechaInicio
        self.fechaFinal = fechaFinal
        self.presupuestoDiario = presupuestoDiario
        self.tipoViaje = tipoViaje
        self.gastos = []
        self.divisa = self.obtenerDivisa()

    def registrarViaje(self):
        """Registra el viaje guardando la información en un archivo."""
        with open('gastosViaje.txt', 'a') as file:
            file.write(f"Destino: {self.destino}\n")
            file.write(f"Fecha de Inicio: {self.fechaInicio.strftime('%Y-%m-%d')}\n")
            file.write(f"Fecha Final: {self.fechaFinal.strftime('%Y-%m-%d')}\n")
            file.write(f"Presupuesto Diario: {self.presupuestoDiario}\n")
            file.write(f"Tipo de Viaje: {self.tipoViaje.value}\n")
            file.write(f"Divisa: {self.divisa.value}\n\n")
        print(f"Viaje a {self.destino} registrado.")

    def obtenerDivisa(self):
        """Determina la divisa en función del destino y tipo de viaje."""
        if self.tipoViaje == TipoViaje.INTERNACIONAL:
            if self.destino.lower() == 'estados unidos':
                return Divisa.USD
            elif self.destino.lower() == 'europa':
                return Divisa.EUR
        return Divisa.COP

    def calcularPresupuestoRestante(self):
        """Calcula el presupuesto restante del viaje."""
        total_gastado = sum(gasto.valor for gasto in self.gastos)
        dias_viaje = (self.fechaFinal - self.fechaInicio).days + 1
        presupuesto_restante = self.presupuestoDiario * dias_viaje - total_gastado
        return presupuesto_restante

    def agregarGasto(self, gasto):
        """Agrega un gasto a la lista de gastos del viaje."""
        self.gastos.append(gasto)

    def eliminarGasto(self, gasto):
        """Elimina un gasto de la lista de gastos del viaje."""
        self.gastos.remove(gasto)

    def obtenerGastosPorFecha(self, fecha):
        """Obtiene los gastos del viaje para una fecha específica."""
        return [gasto for gasto in self.gastos if gasto.fecha == fecha]

    def obtenerGastosPorTipo(self, tipo: TipoGasto):
        """Obtiene los gastos del viaje para un tipo de gasto específico."""
        return [gasto for gasto in self.gastos if gasto.tipoGasto == tipo]
