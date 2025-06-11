comidas_favoritas = ["Salteñas", "Pique Macho", "Sopa de Maní"]

# Imprimir lista inicial enumerada
print("Lista inicial:")
for i, comida in enumerate(comidas_favoritas, start=1):
    print(f"{i}. {comida}")

# Mostrar la segunda comida favorita
print(f"\nMi segunda comida favorita es: {comidas_favoritas[1]}")

# Cambiar la primera comida
comidas_favoritas[0] = "Api con pastel"

# Imprimir lista actualizada enumerada
print("\nLista actualizada:")
for i, comida in enumerate(comidas_favoritas, start=1):
    print(f"{i}. {comida}")

# Mostrar la cantidad de elementos en la lista
print(f"\nMi lista de comidas favoritas tiene {len(comidas_favoritas)} elementos.")