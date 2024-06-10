from gasto import Gasto
from divisas import Divisa
from tipo_gasto import TipoGasto
from metodo_pago import MetodoPago
from excepciones import GastoError,DivisaError

class ControlGasto:
    def registrarGasto(self, fecha, valor, metodoPago: MetodoPago, tipoGasto: TipoGasto, divisa: Divisa):
        """Crea y registra un nuevo gasto."""
        try:
            gasto = Gasto(fecha, valor, metodoPago, tipoGasto, divisa)
            gasto.convertirDivisa()
            gasto.registrarGastoArchivo()
            return gasto
        except (GastoError, DivisaError) as e:
            print(f"Error al registrar el gasto: {e}")
            return None

    def convertirDivisa(self, gasto):
        """Convierte la divisa de un gasto."""
        try:
            return gasto.convertirDivisa()
        except DivisaError as e:
            print(f"Error al convertir la divisa: {e}")
            return gasto.valor
