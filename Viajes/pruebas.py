import unittest
from datetime import datetime
from viaje import Viaje
from tipo_viaje import TipoViaje
from gasto import Gasto
from tipo_gasto import TipoGasto
from divisas import Divisa
from metodo_pago import MetodoPago

class TestViaje(unittest.TestCase):

    def setUp(self):
        self.viaje_nacional = Viaje("Bogota", datetime(2024, 6, 1), datetime(2024, 6, 10), 100000, TipoViaje.NACIONAL)
        self.viaje_internacional = Viaje("Europa", datetime(2024, 6, 1), datetime(2024, 6, 10), 200, TipoViaje.INTERNACIONAL)

    def test_registrar_viaje_nacional(self):
        self.viaje_nacional.registrarViaje()
        with open('gastosViaje.txt', 'r') as file:
            contenido = file.read()
        self.assertIn("Destino: Bogota", contenido)
        self.assertIn("Tipo de Viaje: nacional", contenido)

    def test_obtener_divisa_internacional(self):
        self.assertEqual(self.viaje_internacional.divisa, Divisa.EUR)

    def test_calcular_presupuesto_restante(self):
        gasto = Gasto(datetime(2024, 6, 2), 50000, MetodoPago.EFECTIVO, TipoGasto.TRANSPORTE, Divisa.COP)
        self.viaje_nacional.agregarGasto(gasto)
        self.assertEqual(self.viaje_nacional.calcularPresupuestoRestante(), 950000)

    def test_agregar_gasto(self):
        gasto = Gasto(datetime(2024, 6, 2), 50000, MetodoPago.EFECTIVO, TipoGasto.TRANSPORTE, Divisa.COP)
        self.viaje_nacional.agregarGasto(gasto)
        self.assertIn(gasto, self.viaje_nacional.gastos)

    def test_obtener_gastos_por_fecha(self):
        gasto = Gasto(datetime(2024, 6, 2), 50000, MetodoPago.EFECTIVO, TipoGasto.TRANSPORTE, Divisa.COP)
        self.viaje_nacional.agregarGasto(gasto)
        self.assertEqual(len(self.viaje_nacional.obtenerGastosPorFecha(datetime(2024, 6, 2))), 1)

    def test_obtener_gastos_por_tipo(self):
        gasto_transporte = Gasto(datetime(2024, 6, 2), 50000, MetodoPago.EFECTIVO, TipoGasto.TRANSPORTE, Divisa.COP)
        gasto_alojamiento = Gasto(datetime(2024, 6, 3), 150000, MetodoPago.TARJETA, TipoGasto.ALOJAMIENTO, Divisa.COP)
        self.viaje_nacional.agregarGasto(gasto_transporte)
        self.viaje_nacional.agregarGasto(gasto_alojamiento)
        self.assertEqual(len(self.viaje_nacional.obtenerGastosPorTipo(TipoGasto.TRANSPORTE)), 1)
        self.assertEqual(len(self.viaje_nacional.obtenerGastosPorTipo(TipoGasto.ALOJAMIENTO)), 1)

if __name__ == '__main__':
    unittest.main()