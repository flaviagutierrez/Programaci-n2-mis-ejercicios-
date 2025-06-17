def ordenamiento_burbuja(lista):
    """
    Ordena una lista en orden ascendente utilizando el algoritmo de burbuja.
    Modifica la lista original (in-place) y también la retorna por conveniencia.
    """
    n = len(lista)  # Cantidad de elementos en la lista

    for i in range(n - 1):   # Bucle exterior para las pasadas
        hubo_intercambio = False  # Marca si hubo un intercambio en esta pasada

        # Bucle interior para las comparaciones e intercambios
        for j in range(n - 1 - i):  # Cada pasada evita revisar los últimos ya ordenados
            if lista[j] > lista[j + 1]:
                # ¡Intercambio!
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_intercambio = True

        if not hubo_intercambio:  # Si no hubo ningún intercambio, la lista ya está ordenada
            break

    return lista  # Opcional: también se puede omitir

if __name__ == "__main__":
    numeros = [6, 3, 8, 2, 5]
    print("Antes:", numeros)
    ordenamiento_burbuja(numeros)
    print("Después:", numeros)