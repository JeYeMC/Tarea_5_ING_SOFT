class GastoError(Exception):
    """Excepción base para errores relacionados con gastos."""
    pass

class DivisaError(Exception):
    """Excepción para errores relacionados con la conversión de divisas."""
    pass

class ViajeError(Exception):
    """Excepción base para errores relacionados con viajes."""
    pass

class FechaError(Exception):
    """Excepción para errores relacionados con fechas."""
    pass