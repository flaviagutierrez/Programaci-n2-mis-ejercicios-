
# Pedir al usuario un número entero
numero = int(input("Ingresa un número entero para ver su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:")
print("-" * 30)

# Usar bucle for con range() para mostrar la tabla del 1 al 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print("-" * 30)

