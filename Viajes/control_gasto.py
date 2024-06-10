"""Módulo que controla la creación y conversión de gastos"""
from gasto import Gasto
from divisas import Divisa
from tipo_gasto import TipoGasto
from metodo_pago import MetodoPago


class ControlGasto:
    """Clase que controla la creación y conversion de gastos"""

    def registrar_gasto(self, fecha, valor, metodo_pago: MetodoPago, tipo_gasto: TipoGasto, divisa: Divisa):
        """Crea y registra un nuevo gasto."""
        gasto = Gasto(fecha, valor, metodo_pago, tipo_gasto, divisa)
        gasto.convertirDivisa()
        gasto.registrarGastoArchivo()
        return gasto

    def convertir_divisa(self, gasto):
        """Convierte la divisa de un gasto."""
        return gasto.convertirDivisa()
