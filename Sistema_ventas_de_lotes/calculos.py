
def calcular_precio_total(area, precio_m2):
    return area * precio_m2


def calcular_cuota_inicial(precio_total):
    return precio_total * 0.20


def calcular_saldo(precio_total, cuota_inicial):
    return precio_total - cuota_inicial


def calcular_venta(area, precio_m2):
    total = calcular_precio_total(area, precio_m2)
    cuota = calcular_cuota_inicial(total)
    saldo = calcular_saldo(total, cuota)

    return total, cuota, saldo
