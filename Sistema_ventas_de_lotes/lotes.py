
from validaciones import (
    validar_texto,
    validar_numero_positivo,
    validar_codigo
)


def registrar_lote(lotes, codigo, urbanizacion, area, precio_m2):

    codigo = validar_codigo(codigo, lotes)
    urbanizacion = validar_texto(urbanizacion, "urbanizacion")
    area = validar_numero_positivo(area, "area")
    precio_m2 = validar_numero_positivo(precio_m2, "precio por m2")

    lote = {
        "codigo": codigo,
        "urbanizacion": urbanizacion,
        "area": area,
        "precio_m2": precio_m2,
        "estado": "Disponible"
    }

    lotes[codigo] = lote

    return lote


def listar_lotes(lotes):
    if not lotes:
        print("\nNo hay lotes registrados.")
        return

    print("\n========== LISTA DE LOTES ==========")

    for lote in lotes.values():
        print("--------------------------------")
        print("Codigo:", lote["codigo"])
        print("Urbanizacion:", lote["urbanizacion"])
        print("Area:", lote["area"], "m2")
        print("Precio por m2: S/", lote["precio_m2"])
        print("Estado:", lote["estado"])


def listar_disponibles(lotes):
    disponibles = [
        lote for lote in lotes.values()
        if lote["estado"] == "Disponible"
    ]

    if not disponibles:
        print("\nNo hay lotes disponibles.")
        return

    print("\n======= LOTES DISPONIBLES =======")

    for lote in disponibles:
        print("--------------------------------")
        print("Codigo:", lote["codigo"])
        print("Urbanizacion:", lote["urbanizacion"])
        print("Area:", lote["area"], "m2")
        print("Precio por m2: S/", lote["precio_m2"])
