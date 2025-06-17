def ordenamiento_insercion(lista):
  # Empezamos desde el segundo elemento (índice 1)
  for i in range(1, len(lista)):
      valor_actual = lista[i]  # La "carta" que vamos a insertar
      posicion_actual = i

      # Desplazar elementos mayores hacia la derecha
      # mientras la posición sea válida y el elemento a la izquierda sea mayor
      while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
          lista[posicion_actual] = lista[posicion_actual - 1]  # Desplazamiento
          posicion_actual -= 1

      # Insertar la "carta" en su hueco correcto
      lista[posicion_actual] = valor_actual

  return lista

if __name__ == "__main__":
  numeros = [8, 4, 6, 2, 7]
  print("Antes:", numeros)
  ordenamiento_insercion(numeros)
  print("Después:", numeros)