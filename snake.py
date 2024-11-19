import math
import sys

def mostrar_menu():
    print("\n=== Calculadora Científica ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Logaritmo (base 10)")
    print("8. Logaritmo natural (base e)")
    print("9. Seno")
    print("10. Coseno")
    print("11. Tangente")
    print("12. Factorial")
    print("13. Salir")

def obtener_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-13): ")

        if opcion == "1":  # Suma
            a = obtener_numero("Ingresa el primer número: ")
            b = obtener_numero("Ingresa el segundo número: ")
            print(f"Resultado: {a} + {b} = {a + b}")

        elif opcion == "2":  # Resta
            a = obtener_numero("Ingresa el primer número: ")
            b = obtener_numero("Ingresa el segundo número: ")
            print(f"Resultado: {a} - {b} = {a - b}")

        elif opcion == "3":  # Multiplicación
            a = obtener_numero("Ingresa el primer número: ")
            b = obtener_numero("Ingresa el segundo número: ")
            print(f"Resultado: {a} * {b} = {a * b}")

        elif opcion == "4":  # División
            a = obtener_numero("Ingresa el dividendo: ")
            b = obtener_numero("Ingresa el divisor: ")
            if b != 0:
                print(f"Resultado: {a} / {b} = {a / b}")
            else:
                print("Error: División entre cero no permitida.")

        elif opcion == "5":  # Potencia
            base = obtener_numero("Ingresa la base: ")
            exponente = obtener_numero("Ingresa el exponente: ")
            print(f"Resultado: {base} ^ {exponente} = {math.pow(base, exponente)}")

        elif opcion == "6":  # Raiz cuadrada
            a = obtener_numero("Ingresa el número: ")
            if a >= 0:
                print(f"Resultado: √{a} = {math.sqrt(a)}")
            else:
                print("Error: No se puede calcular la raíz cuadrada de un número negativo.")

        elif opcion == "7":  # Logaritmo (base 10)
            a = obtener_numero("Ingresa el número: ")
            if a > 0:
                print(f"Resultado: log10({a}) = {math.log10(a)}")
            else:
                print("Error: El logaritmo requiere un número mayor que 0.")

        elif opcion == "8":  # Logaritmo natural
            a = obtener_numero("Ingresa el número: ")
            if a > 0:
                print(f"Resultado: ln({a}) = {math.log(a)}")
            else:
                print("Error: El logaritmo natural requiere un número mayor que 0.")

        elif opcion == "9":  # Seno
            a = obtener_numero("Ingresa el ángulo en grados: ")
            print(f"Resultado: sin({a}°) = {math.sin(math.radians(a))}")

        elif opcion == "10":  # Coseno
            a = obtener_numero("Ingresa el ángulo en grados: ")
            print(f"Resultado: cos({a}°) = {math.cos(math.radians(a))}")

        elif opcion == "11":  # Tangente
            a = obtener_numero("Ingresa el ángulo en grados: ")
            print(f"Resultado: tan({a}°) = {math.tan(math.radians(a))}")

        elif opcion == "12":  # Factorial
            a = obtener_numero("Ingresa un número entero: ")
            if a >= 0 and a == int(a):
                print(f"Resultado: {int(a)}! = {math.factorial(int(a))}")
            else:
                print("Error: El factorial solo se define para enteros no negativos.")

        elif opcion == "13":  # Salir
            print("Gracias por usar la calculadora. ¡Adiós!")
            sys.exit()

        else:
            print("Opción inválida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    calculadora()
