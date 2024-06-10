"""Módulo principal que simula el registro de un viaje y sus gastos"""
from datetime import datetime
import logging
from control_viaje import ControlViaje
from control_gasto import ControlGasto
from control_reporte import ControlReporte
from tipo_viaje import TipoViaje
from tipo_gasto import TipoGasto
from metodo_pago import MetodoPago
from excepciones import ViajeError, FechaError, GastoError, DivisaError

def solicitar_fecha(mensaje):
    """Solicita una fecha al usuario hasta que se ingrese una fecha válida"""
    while True:
        fecha_str = input(mensaje)
        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            return fecha
        except ValueError:
            print("Fecha inválida. Por favor, ingrese la fecha en formato YYYY-MM-DD.")

def solicitar_float(mensaje):
    """Solicita un número flotante al usuario hasta que se ingrese un valor válido"""
    while True:
        valor_str = input(mensaje)
        try:
            valor = float(valor_str)
            return valor
        except ValueError:
            print("Valor inválido. Por favor, ingrese un número válido.")

def solicitar_enum(mensaje, enum_class):
    """Solicita una opción de un Enum al usuario hasta que se ingrese una opción válida"""
    while True:
        opcion_str = input(mensaje)
        try:
            opcion = enum_class[opcion_str.upper()]
            return opcion
        except KeyError:
            print(f"Opción inválida. Por favor, ingrese una de las siguientes opciones: {', '.join([e.name for e in enum_class])}.")

def main():
    """Función principal que simula el registro de un viaje y sus gastos"""
    control_viaje = ControlViaje()
    control_gasto = ControlGasto()
    control_reporte = ControlReporte()

    # Configuración del logger
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    # Registro de un viaje
    destino = input("Ingrese el destino: ")
    fecha_inicio = solicitar_fecha("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_final = solicitar_fecha("Ingrese la fecha final (YYYY-MM-DD): ")
    presupuesto_diario = solicitar_float("Ingrese el presupuesto diario: ")
    tipo_viaje = solicitar_enum("Ingrese el tipo de viaje (NACIONAL/INTERNACIONAL): ", TipoViaje)

    while True:
        try:
            viaje = control_viaje.registrar_viaje(destino, fecha_inicio, fecha_final, presupuesto_diario, tipo_viaje)
            if viaje is None:
                raise ViajeError("No se pudo registrar el viaje.")
            break
        except (FechaError, ViajeError) as e:
            logging.error(e)
            print(f"Error: {e}. Por favor, intente registrar el viaje nuevamente.")
            fecha_inicio = solicitar_fecha("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_final = solicitar_fecha("Ingrese la fecha final (YYYY-MM-DD): ")
            presupuesto_diario = solicitar_float("Ingrese el presupuesto diario: ")
            tipo_viaje = solicitar_enum("Ingrese el tipo de viaje (NACIONAL/INTERNACIONAL): ", TipoViaje)

    while True:
        try:
            # Registro de un gasto
            fecha = solicitar_fecha("Ingrese la fecha del gasto (YYYY-MM-DD): ")

            if fecha < fecha_inicio or fecha > fecha_final:
                print("La fecha del gasto no está dentro del rango del viaje")
                continue

            valor = solicitar_float("Ingrese el valor del gasto: ")
            metodo_pago = solicitar_enum("Ingrese el método de pago (EFECTIVO/TARJETA): ", MetodoPago)
            tipo_gasto = solicitar_enum("Ingrese el tipo de gasto "
                                        "(TRANSPORTE/ALOJAMIENTO/ALIMENTACION/ENTRETENIMIENTO/COMPRAS): ",
                                        TipoGasto)
            gasto = control_gasto.registrar_gasto(fecha, valor, metodo_pago, tipo_gasto, viaje.divisa)
            if gasto is None:
                raise GastoError("No se pudo registrar el gasto.")
            control_viaje.agregar_gasto(viaje, gasto)

            print(f"Presupuesto restante para el día {fecha.strftime('%Y-%m-%d')}: "
                  f"{viaje.calcular_presupuesto_restante_dia(fecha)}")
            print(f"Presupuesto total: {viaje.calcular_presupuesto_total()}")

            otra_entrada = input("¿Desea registrar otro gasto? (sí/no): ")
            if otra_entrada.lower() != 'si':
                break

        except (FechaError, GastoError, DivisaError, ValueError) as e:
            logging.error(e)
            print(f"Error: {e}. Por favor, intente registrar el gasto nuevamente.")
        except Exception as e:
            logging.error(f"Error inesperado: {e}")
            print(f"Error inesperado: {e}. Por favor, intente registrar el gasto nuevamente.")

    while True:
        try:
            # Generar reportes
            control_reporte.generar_reporte_diario(viaje)
            control_reporte.generar_reporte_por_tipo(viaje)
            break
        except ViajeError as e:
            logging.error(e)
            print(f"Error al generar reportes: {e}. Por favor, intente nuevamente.")
        except Exception as e:
            logging.error(f"Error inesperado al generar reportes: {e}")
            print(f"Error inesperado al generar reportes: {e}. Por favor, intente nuevamente.")

if __name__ == '__main__':
    main()
