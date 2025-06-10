def sumar(a, b): # "a" y "b" son PARÁMETROS
 """Esta función recibe dos números y devuelve su suma."""
 resultado_suma = a + b
 return resultado_suma # La palabra clave "return" devuelve un valor

# Pedir números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Llamar la función y mostrar el resultado
resultado = sumar(num1, num2)
print(f"La suma de {num1} + {num2} = {resultado}")