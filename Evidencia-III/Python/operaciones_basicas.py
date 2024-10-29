import math

def suma(a, b):
    print("Opción: Suma")
    return a + b

def resta(a, b):
    print("Opción: Resta")
    return a - b

def multiplicacion(a, b):
    print("Opción: Multiplicación")
    return a * b

def division(a, b):
    print("Opción: División")
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def potencia(base, exponente):
    print("Opción: Potencia")
    return base ** exponente

def raiz_cuadrada(a):
    print("Opción: Raíz Cuadrada")
    return math.sqrt(a)

def seno(angulo_grados):
    print("Opción: Seno")
    return math.sin(math.radians(angulo_grados))

def coseno(angulo_grados):
    print("Opción: Coseno")
    return math.cos(math.radians(angulo_grados))

def tangente(angulo_grados):
    print("Opción: Tangente")
    return math.tan(math.radians(angulo_grados))

def logaritmo_natural(a):
    print("Opción: Logaritmo Natural")
    return math.log(a)

def logaritmo_base_10(a):
    print("Opción: Logaritmo Base 10")
    return math.log10(a)

def factorial(a):
    print("Opción: Factorial")
    return math.factorial(a)