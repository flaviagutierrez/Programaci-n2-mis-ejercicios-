# 1. Definir el número secreto
numero_secreto = 7

# 2. Pedir al usuario que adivine el número
adivinanza = int(input("Adivina el número secreto (entre 1 y 10): "))

# 3. Mientras no adivine
while adivinanza != numero_secreto:
    if adivinanza > numero_secreto:
        print("Demasiado alto")
    else:
        print("Demasiado bajo")
    # Pedir otra vez
    adivinanza = int(input("Intenta de nuevo: "))

# 4. Cuando adivine
print(f"¡Correcto!")