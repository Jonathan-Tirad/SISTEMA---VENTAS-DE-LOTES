
def validar_texto(texto, campo):
    if not texto.strip():
        raise ValueError(f"El campo {campo} no puede estar vacio.")

    return texto.strip()


def validar_numero_positivo(valor, campo):
    try:
        numero = float(valor)
    except ValueError:
        raise ValueError(f"{campo} debe ser un numero.")

    if numero <= 0:
        raise ValueError(f"{campo} debe ser mayor que cero.")

    return numero


def validar_codigo(codigo, lotes):
    codigo = validar_texto(codigo, "codigo").upper()

    if codigo in lotes:
        raise ValueError("El codigo del lote ya existe.")

    return codigo


def validar_comprador(nombre, documento):
    nombre = validar_texto(nombre, "nombre del comprador")
    documento = validar_texto(documento, "documento de identidad")

    if not documento.isdigit():
        raise ValueError("El documento debe contener solo numeros.")

    return nombre, documento
