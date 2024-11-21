def obtener_numero(mensaje):
    """Solicita un número al usuario y valida la entrada."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")
