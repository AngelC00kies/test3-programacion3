def raiz_cuadrada():
    a = obtener_numero("Ingresa el número: ")
    if a >= 0:
        print(f"Resultado: √{a} = {math.sqrt(a)}")
    else:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
