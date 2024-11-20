def calculadora():
    """Controla el flujo principal de la calculadora."""
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-7): ")

        # Diccionario para mapear opciones con funciones
        operaciones = {
            "1": suma,
            "2": resta,
            "3": multiplicacion,
            "4": division,
            "5": potencia,
            "6": raiz_cuadrada
        }

        if opcion == "7":  # Salir
            print("Gracias por usar la calculadora. ¡Adiós!")
            sys.exit()
        elif opcion in operaciones:
            operaciones[opcion]()  # Llama a la función correspondiente
        else:
            print("Opción inválida. Por favor, elige una opción del menú.")
