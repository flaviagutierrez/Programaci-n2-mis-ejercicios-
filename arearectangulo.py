def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura

def mostrar_area_rectangulo(numero, base, altura):
    """Muestra el área de un rectángulo."""
    area = calcular_area_rectangulo(base, altura)
    print(f"El área del rectángulo {numero} ({base}x{altura}) es: {area}")

# Rectángulo 1
mostrar_area_rectangulo(1, 10, 5)
# Rectángulo 2
mostrar_area_rectangulo(2, 7, 3)