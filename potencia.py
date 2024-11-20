def potencia():
    base = obtener_numero("Ingresa la base: ")
    exponente = obtener_numero("Ingresa el exponente: ")
    print(f"Resultado: {base} ^ {exponente} = {math.pow(base, exponente)}")
