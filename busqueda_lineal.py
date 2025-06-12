def busqueda_lineal(lista, objetivo):
  for i, elemento in enumerate(lista):
      if elemento == objetivo:
          return i  # Retorna el índice donde se encontró
  return -1  # Retorna -1 si no encontró el elemento
