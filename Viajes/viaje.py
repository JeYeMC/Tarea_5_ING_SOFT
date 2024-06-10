from tipo_viaje import TipoViaje
from divisas import Divisa
from tipo_gasto import TipoGasto
from excepciones import ViajeError, FechaError

class Viaje:
    def __init__(self, destino, fecha_inicio, fecha_final, presupuesto_diario, tipo_viaje: TipoViaje):
        """Inicializa un nuevo viaje con destino, fechas, presupuesto diario y tipo de viaje."""
        if presupuesto_diario < 0:
            raise ViajeError("El presupuesto diario no puede ser negativo.")
        if fecha_inicio >= fecha_final:
            raise FechaError("La fecha de inicio debe ser anterior a la fecha final.")
        self.destino = destino
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.presupuesto_diario = presupuesto_diario
        self.tipo_viaje = tipo_viaje
        self.gastos = []
        self.divisa = self.obtener_divisa()


    def registrar_viaje_archivo(self):
        """Registra el viaje guardando la información en un archivo."""
        try:
            with open('gastosViaje.txt', 'w') as file:
                file.write("\n\n\nDatos Viaje:\n")
                file.write(f"Destino: {self.destino}\n")
                file.write(f"Fecha de Inicio: {self.fecha_inicio.strftime('%Y-%m-%d')}\n")
                file.write(f"Fecha Final: {self.fecha_final.strftime('%Y-%m-%d')}\n")
                file.write(f"Presupuesto Diario: {self.presupuesto_diario}\n")
                file.write(f"Tipo de Viaje: {self.tipo_viaje.value}\n")
                file.write(f"Divisa: {self.divisa.value}\n")
        except IOError as e:
            raise ViajeError(f"Error al registrar el viaje: {e}")

        
    def obtener_divisa(self):
        """Determina la divisa en función del destino y tipo de viaje."""
        if self.tipo_viaje == TipoViaje.INTERNACIONAL:
            if self.destino.lower() == 'estados unidos':
                return Divisa.USD
            elif self.destino.lower() == 'europa':
                return Divisa.EUR
        return Divisa.COP

    def validar_fecha_gasto(self, fecha):
        """Valida que la fecha del gasto esté dentro del rango del viaje."""
        if not (self.fecha_inicio <= fecha <= self.fecha_final):
            raise FechaError("La fecha del gasto debe estar dentro del rango del viaje.")

    def calcular_presupuesto_restante_dia(self, fecha):
        """Calcula el presupuesto restante para un día específico."""
        total_gastado = sum(gasto.valor for gasto in self.gastos if gasto.fecha == fecha)
        presupuesto_restante = self.presupuesto_diario - total_gastado
        return presupuesto_restante

    def calcular_presupuesto_total(self):
        """Calcula el presupuesto total del viaje."""
        dias_viaje = (self.fecha_final - self.fecha_inicio).days + 1
        presupuesto_total = self.presupuesto_diario * dias_viaje
        return presupuesto_total

    def agregar_gasto(self, gasto):
        """Agrega un gasto a la lista de gastos del viaje."""
        self.validar_fecha_gasto(gasto.fecha)
        self.gastos.append(gasto)

    def eliminar_gasto(self, gasto):
        """Elimina un gasto de la lista de gastos del viaje."""
        self.gastos.remove(gasto)


    def obtener_gastos_por_fecha(self, fecha):
        """Obtiene los gastos del viaje para una fecha específica."""
        return [gasto for gasto in self.gastos if gasto.fecha == fecha]

    def obtener_gastos_por_tipo(self, tipo: TipoGasto):
        """Obtiene los gastos del viaje para un tipo de gasto específico."""
        return [gasto for gasto in self.gastos if gasto.tipo_gasto== tipo]
