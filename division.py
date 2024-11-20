def division():
    a = obtener_numero("Ingresa el dividendo: ")
    b = obtener_numero("Ingresa el divisor: ")
    if b != 0:
        print(f"Resultado: {a} / {b} = {a / b}")
    else:
        print("Error: División entre cero no permitida.")
