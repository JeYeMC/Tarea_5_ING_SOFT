import requests
from divisas import Divisa
from tipo_gasto import TipoGasto
from metodo_pago import MetodoPago



class Gasto:
    def __init__(self, fecha, valor, metodoPago: MetodoPago, tipoGasto: TipoGasto, divisa: Divisa):
        """Inicializa un nuevo gasto con la fecha, valor, método de pago, tipo de gasto y divisa."""
        self.fecha = fecha
        self.valor = valor
        self.metodoPago = metodoPago
        self.tipoGasto = tipoGasto
        self.divisa = divisa



    def registrarGasto(self):
        """Registra el gasto guardando la información en un archivo."""
        with open('gastosViaje.txt', 'a') as file:
            file.write(f"Fecha: {self.fecha.strftime('%Y-%m-%d')}, Valor: {self.valor}, Método de Pago: {self.metodoPago.value}, Tipo de Gasto: {self.tipoGasto.value}, Divisa: {self.divisa.value}\n\n\n\n")
        print(f"Gasto de {self.valor} registrado en {self.tipoGasto.value}.")



    def convertirDivisa(self):
        """Convierte el valor del gasto a pesos colombianos si la divisa no es COP."""
        if self.divisa != Divisa.COP:
            response = requests.get("https://csrng.net/csrng/csrng.php?min=3500&max=4500")
            tasa_cambio = response.json()[0]['random']
            if self.divisa == Divisa.USD:
                self.valor *= tasa_cambio
            elif self.divisa == Divisa.EUR:
                self.valor *= (tasa_cambio + 200)
        return self.valor



    def actualizarValor(self, valor):
        """Actualiza el valor del gasto."""
        self.valor = valor



    def actualizarMetodoPago(self, metodo: MetodoPago):
        """Actualiza el método de pago del gasto."""
        self.metodoPago = metodo



    def actualizarTipoGasto(self, tipo: TipoGasto):
        """Actualiza el tipo de gasto."""
        self.tipoGasto = tipo
