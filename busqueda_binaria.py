def busqueda_binaria(lista, objetivo):
  inicio = 0
  fin = len(lista) - 1

  while inicio <= fin:
      medio = (inicio + fin) // 2

      if lista[medio] == objetivo:
          return medio  # Retorna el índice donde se encontró el objetivo
      elif lista[medio] < objetivo:
          inicio = medio + 1
      else:
          fin = medio - 1

  return -1  # Retorna -1 si el objetivo no está en la lista

# Ejemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13]
objetivo = 7

resultado = busqueda_binaria(lista_ordenada, objetivo)
if resultado != -1:
  print(f"Elemento encontrado en el índice {resultado}")
else:
  print("Elemento no encontrado")