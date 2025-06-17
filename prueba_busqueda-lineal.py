def busqueda_lineal(lista, objetivo):
  for i, elemento in enumerate(lista):
      if elemento == objetivo:
          return i  # Retorna el índice donde se encontró
  return -1  # Retorna -1 si no encontró el elemento

# Pruebas
lista = [4, 2, 7, 1, 9, 3]

# Caso 1: El objetivo está en la lista
objetivo1 = 7
resultado1 = busqueda_lineal(lista, objetivo1)
print(f"Buscando {objetivo1} en la lista: Índice encontrado = {resultado1}")

# Caso 2: El objetivo NO está en la lista
objetivo2 = 5
resultado2 = busqueda_lineal(lista, objetivo2)
print(f"Buscando {objetivo2} en la lista: Índice encontrado = {resultado2}")