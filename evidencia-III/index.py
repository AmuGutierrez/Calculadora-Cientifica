from operaciones_basicas import *

def calculadora():
    print("Bienvenido a la Calculadora Científica")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Seno")
    print("8. Coseno")
    print("9. Tangente")
    print("10. Logaritmo Natural")
    print("11. Logaritmo Base 10")
    print("12. Factorial")
    print("0. Salir")

    while True:
        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == "0":
            print("¡Hasta luego!")
            break
        elif opcion in {"1", "2", "3", "4", "5"}:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            if opcion == "1":
                print("Resultado:", suma(num1, num2))
            elif opcion == "2":
                print("Resultado:", resta(num1, num2))
            elif opcion == "3":
                print("Resultado:", multiplicacion(num1, num2))
            elif opcion == "4":
                print("Resultado:", division(num1, num2))
            elif opcion == "5":
                print("Resultado:", potencia(num1, num2))
        elif opcion in {"6", "7", "8", "9", "10", "11", "12"}:
            num = float(input("Ingrese el número: "))
            if opcion == "6":
                print("Resultado:", raiz_cuadrada(num))
            elif opcion == "7":
                print("Resultado:", seno(num))
            elif opcion == "8":
                print("Resultado:", coseno(num))
            elif opcion == "9":
                print("Resultado:", tangente(num))
            elif opcion == "10":
                print("Resultado:", logaritmo_natural(num))
            elif opcion == "11":
                print("Resultado:", logaritmo_base_10(num))
            elif opcion == "12":
                print("Resultado:", factorial(int(num)))
        else:
            print("Opción no válida. Por favor ingrese un número del 0 al 12.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()