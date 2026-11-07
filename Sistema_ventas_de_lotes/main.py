from lotes import registrar_lote, listar_lotes, listar_disponibles
from ventas import registrar_venta, mostrar_ventas


# ALMACENAMIENTO DE DATOS
lotes = {}
ventas = []


# DATOS DE PRUEBA OBLIGATORIOS
registrar_lote(
    lotes, "LT-001", "Los Jardines", 120, 450
)

registrar_lote(
    lotes, "LT-002", "Las Palmeras", 90, 500
)


# MENU PRINCIPAL
def menu():

    while True:

        print("\n===================================")
        print(" SISTEMA DE VENTA DE LOTES")
        print(" TERRENOS DEL NORTE S.A.C.")
        print("===================================")

        print("1. Registrar lote")
        print("2. Listar todos los lotes")
        print("3. Listar lotes disponibles")
        print("4. Registrar venta")
        print("5. Mostrar resumen de ventas")
        print("6. Salir")

        opcion = input("\nSeleccione una opcion: ").strip()

        try:

            if opcion == "1":

                print("\n--- REGISTRAR NUEVO LOTE ---")

                codigo = input("Codigo del lote: ")
                urbanizacion = input("Urbanizacion: ")
                area = input("Area en metros cuadrados: ")
                precio = input("Precio por metro cuadrado: ")

                lote = registrar_lote(
                    lotes, codigo, urbanizacion, area, precio
                )

                print("\nLote registrado correctamente.")
                print("Codigo:", lote["codigo"])

            elif opcion == "2":

                listar_lotes(lotes)

            elif opcion == "3":

                listar_disponibles(lotes)

            elif opcion == "4":

                print("\n--- REGISTRAR VENTA ---")

                listar_disponibles(lotes)

                codigo = input("\nCodigo del lote a vender: ")
                nombre = input("Nombre del comprador: ")
                documento = input("Documento de identidad: ")

                venta = registrar_venta(
                    lotes, ventas, codigo, nombre, documento
                )

                print("\nVENTA REGISTRADA CORRECTAMENTE")
                print("--------------------------------")
                print("Lote:", venta["codigo_lote"])
                print("Comprador:", venta["comprador"])
                print("Precio total: S/", round(venta["precio_total"], 2))
                print("Cuota inicial: S/", round(venta["cuota_inicial"], 2))
                print("Saldo: S/", round(venta["saldo"], 2))

            elif opcion == "5":

                mostrar_ventas(ventas)

            elif opcion == "6":

                print("\nGracias por utilizar el sistema.")
                print("Saliendo del programa...")
                break

            else:

                print("\nOpcion incorrecta. Intente nuevamente.")

        except ValueError as error:

            print("\nERROR:", error)


# EJECUTAR SISTEMA
if __name__ == "__main__":
    menu()