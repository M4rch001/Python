import math

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

c = a // b
raiz_cuadrada_a = math.sqrt(a)
raiz_cuadrada_b = math.sqrt(b)

print("El resultado de la división es:", c)
print("La raíz cuadrada de", a, "es:", raiz_cuadrada_a)
print("La raíz cuadrada de", b, "es:", raiz_cuadrada_b)