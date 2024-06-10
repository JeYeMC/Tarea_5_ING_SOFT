"""Módulo que contiene la clase ControlViaje"""
from viaje import Viaje
from tipo_viaje import TipoViaje

class ControlViaje:
    """Clase que controla la creación de viajes"""

    def registrarViaje(self, destino, fechaInicio, fechaFinal, presupuestoDiario, tipoViaje: TipoViaje):
        """Crea y registra un nuevo viaje."""
        if fechaInicio > fechaFinal:
            raise ValueError("La fecha de inicio debe ser anterior a la fecha final.")
        
        viaje = Viaje(destino, fechaInicio, fechaFinal, presupuestoDiario, tipoViaje)
        viaje.registrarViajeArchivo()
        return viaje

    def obtenerGastos(self, viaje):
        """Obtiene la lista de gastos de un viaje."""
        return viaje.gastos

    def agregarGasto(self, viaje, gasto):
        """Agrega un gasto a la lista de gastos de un viaje."""
        viaje.agregarGasto(gasto)
