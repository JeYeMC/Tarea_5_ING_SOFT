from gasto import Gasto
from divisas import Divisa
from tipo_gasto import TipoGasto
from metodo_pago import MetodoPago

class ControlGasto:
    def registrarGasto(self, fecha, valor, metodoPago: MetodoPago, tipoGasto: TipoGasto, divisa: Divisa):
        """Crea y registra un nuevo gasto."""
        gasto = Gasto(fecha, valor, metodoPago, tipoGasto, divisa)
        gasto.convertirDivisa()
        gasto.registrarGasto()
        return gasto

    def convertirDivisa(self, gasto):
        """Convierte la divisa de un gasto."""
        return gasto.convertirDivisa()
