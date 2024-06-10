import unittest
from datetime import datetime
from viaje import Viaje
from tipo_viaje import TipoViaje
from gasto import Gasto
from tipo_gasto import TipoGasto
from divisas import Divisa
from metodo_pago import MetodoPago
from excepciones import ViajeError, FechaError

class TestViaje(unittest.TestCase):

    def setUp(self):
        self.viaje_nacional = Viaje("Bogota", datetime(2024, 6, 1), datetime(2024, 6, 10), 100000, TipoViaje.NACIONAL)
        self.viaje_internacional = Viaje("Europa", datetime(2024, 6, 1), datetime(2024, 6, 10), 200, TipoViaje.INTERNACIONAL)

    def test_registrar_viaje_nacional(self):
        try:
            self.viaje_nacional.registrar_viaje_archivo()
            with open('gastosViaje.txt', 'r') as file:
                contenido = file.read()
            self.assertIn("Destino: Bogota", contenido)
            self.assertIn("Tipo de Viaje: nacional", contenido)
        except ViajeError as e:
            self.fail(f"Error al registrar viaje nacional: {e}")

    def test_obtener_divisa_internacional(self):
        self.assertEqual(self.viaje_internacional.divisa, Divisa.EUR)

    def test_calcular_presupuesto_restante_diario(self):
        gasto = Gasto(datetime(2024, 6, 2), 50000, MetodoPago.EFECTIVO, TipoGasto.TRANSPORTE, Divisa.COP)
        self.viaje_nacional.agregar_gasto(gasto)
        self.assertEqual(self.viaje_nacional.calcular_presupuesto_restante_dia(datetime(2024, 6, 2)), 50000)

    def test_agregar_gasto(self):
        gasto = Gasto(datetime(2024, 6, 2), 50000, MetodoPago.EFECTIVO, TipoGasto.TRANSPORTE, Divisa.COP)
        try:
            self.viaje_nacional.agregar_gasto()
            self.assertIn(gasto, self.viaje_nacional.gastos)
        except FechaError as e:
            self.fail(f"Error al agregar gasto: {e}")

    def test_fecha_inicio_posterior_fecha_final(self):
        with self.assertRaises(FechaError):
            Viaje("Bogota", datetime(2024, 6, 10), datetime(2024, 6, 1), 100000, TipoViaje.NACIONAL)

    def test_gasto_fuera_de_rango_fecha(self):
        with self.assertRaises(FechaError):
            gasto = Gasto(datetime(2024, 6, 12), 50000, MetodoPago.EFECTIVO, TipoGasto.TRANSPORTE, Divisa.COP)
            self.viaje_nacional.agregar_gasto(gasto)

if __name__ == '__main__':
    unittest.main()
