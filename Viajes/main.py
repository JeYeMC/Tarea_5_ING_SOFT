from control_viaje import ControlViaje
from control_gasto import ControlGasto
from control_reporte import ControlReporte
from datetime import datetime
from tipo_viaje import TipoViaje
from tipo_gasto import TipoGasto
from metodo_pago import MetodoPago



def main():
    control_viaje = ControlViaje()
    control_gasto = ControlGasto()
    control_reporte = ControlReporte()


    # Registro de un viaje
    destino = input("Ingrese el destino: ")
    fechaInicio = datetime.strptime(input("Ingrese la fecha de inicio (YYYY-MM-DD): "), '%Y-%m-%d')
    fechaFinal = datetime.strptime(input("Ingrese la fecha final (YYYY-MM-DD): "), '%Y-%m-%d')
    presupuestoDiario = float(input("Ingrese el presupuesto diario: "))
    tipoViaje = TipoViaje[input("Ingrese el tipo de viaje (NACIONAL/INTERNACIONAL): ").upper()]
    viaje = control_viaje.registrarViaje(destino, fechaInicio, fechaFinal, presupuestoDiario, tipoViaje)



    while True:
        # Registro de un gasto
        fecha = datetime.strptime(input("Ingrese la fecha del gasto (YYYY-MM-DD): "), '%Y-%m-%d')
        valor = float(input("Ingrese el valor del gasto: "))
        metodoPago = MetodoPago[input("Ingrese el método de pago (EFECTIVO/TARJETA): ").upper()]
        tipoGasto = TipoGasto[input("Ingrese el tipo de gasto (TRANSPORTE/ALOJAMIENTO/ALIMENTACION/ENTRETENIMIENTO/COMPRAS): ").upper()]
        gasto = control_gasto.registrar_gasto(fecha, valor, metodoPago, tipoGasto, viaje.divisa)
        control_viaje.agregarGasto(viaje, gasto)
        print(f"Presupuesto restante: {viaje.calcularPresupuestoRestanteDia(fecha)}")

        otraEntrada = input("¿Desea registrar otro gasto? (sí/no): ")
        if otraEntrada.lower() != 'si':
            break


    # Generar reportes
    control_reporte.generar_reporte_diario(viaje)
    control_reporte.generarr_reporte_por_tipo(viaje)

if __name__ == '__main__':
    main()

#Falta hacer pruebas y excepciones

