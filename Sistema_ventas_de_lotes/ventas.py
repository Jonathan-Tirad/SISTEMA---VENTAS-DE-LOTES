from validaciones import validar_comprador
from calculos import calcular_venta


def registrar_venta(lotes, ventas, codigo, nombre, documento):

    codigo = codigo.strip().upper()

    if codigo not in lotes:
        raise ValueError("El lote no existe.")

    lote = lotes[codigo]

    if lote["estado"] != "Disponible":
        raise ValueError("Este lote ya fue vendido.")

    nombre, documento = validar_comprador(nombre, documento)

    total, cuota, saldo = calcular_venta(
        lote["area"],
        lote["precio_m2"]
    )

    venta = {
        "codigo_lote": codigo,
        "urbanizacion": lote["urbanizacion"],
        "comprador": nombre,
        "documento": documento,
        "precio_total": total,
        "cuota_inicial": cuota,
        "saldo": saldo
    }

    ventas.append(venta)

    lote["estado"] = "Vendido"

    return venta


def mostrar_ventas(ventas):

    if not ventas:
        print("\nNo existen ventas registradas.")
        return

    print("\n========== RESUMEN DE VENTAS ==========")

    for venta in ventas:
        print("--------------------------------")
        print("Lote:", venta["codigo_lote"])
        print("Urbanizacion:", venta["urbanizacion"])
        print("Comprador:", venta["comprador"])
        print("Documento:", venta["documento"])
        print("Precio total: S/", round(venta["precio_total"], 2))
        print("Cuota inicial: S/", round(venta["cuota_inicial"], 2))
        print("Saldo: S/", round(venta["saldo"], 2))