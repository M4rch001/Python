#calculadora basica 
import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def raiz_cuadrada(a):
    return math.sqrt(a)

def logaritmo(a, base=10):
    return math.log10(a)

print("Calculadora básica en Python")
print("------------------------")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Raíz cuadrada")
print("6. Logaritmo")

opcion = input("Elige una opción: ")

if opcion == "1":
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print("El resultado es:", suma(a, b))
elif opcion == "2":
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print("El resultado es:", resta(a, b))
elif opcion == "3":
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print("El resultado es:", multiplicacion(a, b))
elif opcion == "4":
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print("El resultado es:", division(a, b))
elif opcion == "5":
    a = float(input("Número: "))
    print("El resultado es:", raiz_cuadrada(a))
elif opcion == "6":
    a = float(input("Número: "))
    print("El resultado es:", logaritmo(a))
else:
    print("Opción incorrecta")
