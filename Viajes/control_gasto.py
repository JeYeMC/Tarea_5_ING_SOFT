from gasto import Gasto
from divisas import Divisa
from tipo_gasto import TipoGasto
from metodo_pago import MetodoPago
from excepciones import GastoError,DivisaError

class ControlGasto:
    def registrar_gasto(self, fecha, valor, metodo_pago: MetodoPago, tipo_gasto: TipoGasto, divisa: Divisa):
        """Crea y registra un nuevo gasto."""
        try:
            gasto = Gasto(fecha, valor, metodo_pago, tipo_gasto, divisa)
            gasto.convertir_divisa()
            gasto.registrar_gasto_archivo()
            return gasto
        except (GastoError, DivisaError) as e:
            print(f"Error al registrar el gasto: {e}")
            return None

    def convertir_divisa(self, gasto):
        """Convierte la divisa de un gasto."""
        try:
            return gasto.convertirDivisa()
        except DivisaError as e:
            print(f"Error al convertir la divisa: {e}")
            return gasto.valor
