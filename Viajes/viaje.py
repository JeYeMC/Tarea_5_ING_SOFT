from datetime import datetime
from tipo_viaje import TipoViaje
from divisas import Divisa
from tipo_gasto import TipoGasto
from excepciones import ViajeError, FechaError




class Viaje:
    def __init__(self, destino, fechaInicio, fechaFinal, presupuestoDiario, tipoViaje: TipoViaje):
        """Inicializa un nuevo viaje con destino, fechas, presupuesto diario y tipo de viaje."""
        if presupuestoDiario < 0:
            raise ViajeError("El presupuesto diario no puede ser negativo.")
        if fechaInicio >= fechaFinal:
            raise FechaError("La fecha de inicio debe ser anterior a la fecha final.")
        self.destino = destino
        self.fechaInicio = fechaInicio
        self.fechaFinal = fechaFinal
        self.presupuestoDiario = presupuestoDiario
        self.tipoViaje = tipoViaje
        self.gastos = []
        self.divisa = self.obtenerDivisa()


    def registrarViajeArchivo(self):
        """Registra el viaje guardando la información en un archivo."""
        try:
            with open('gastosViaje.txt', 'a') as file:
                file.write(f"\n\n\nDestino: {self.destino}\n")
                file.write(f"Fecha de Inicio: {self.fechaInicio.strftime('%Y-%m-%d')}\n")
                file.write(f"Fecha Final: {self.fechaFinal.strftime('%Y-%m-%d')}\n")
                file.write(f"Presupuesto Diario: {self.presupuestoDiario}\n")
                file.write(f"Tipo de Viaje: {self.tipoViaje.value}\n")
                file.write(f"Divisa: {self.divisa.value}\n")
        except IOError as e:
            raise ViajeError(f"Error al registrar el viaje: {e}")
        
    def obtenerDivisa(self):
        """Determina la divisa en función del destino y tipo de viaje."""
        if self.tipoViaje == TipoViaje.INTERNACIONAL:
            if self.destino.lower() == 'estados unidos':
                return Divisa.USD
            elif self.destino.lower() == 'europa':
                return Divisa.EUR
        return Divisa.COP

    def validarFechaGasto(self, fecha):
        """Valida que la fecha del gasto esté dentro del rango del viaje."""
        if not (self.fechaInicio <= fecha <= self.fechaFinal):
            raise FechaError("La fecha del gasto debe estar dentro del rango del viaje.")

    def calcularPresupuestoRestanteDia(self, fecha):
        """Calcula el presupuesto restante para un día específico."""
        total_gastado = sum(gasto.valor for gasto in self.gastos if gasto.fecha == fecha)
        presupuesto_restante = self.presupuestoDiario - total_gastado
        return presupuesto_restante

    def calcularPresupuestoTotal(self):
        """Calcula el presupuesto total del viaje."""
        dias_viaje = (self.fechaFinal - self.fechaInicio).days + 1
        presupuesto_total = self.presupuestoDiario * dias_viaje
        return presupuesto_total

    def agregarGasto(self, gasto):
        """Agrega un gasto a la lista de gastos del viaje."""
        self.validarFechaGasto(gasto.fecha)
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
