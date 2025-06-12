from busqueda_binaria import busqueda_binaria
# Lista ordenada para que funcione la búsqueda binaria
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Elemento que queremos buscar
objetivo = 7

# Ejecutar búsqueda binaria
resultado = busqueda_binaria(numeros, objetivo)
if resultado != -1:
  print(f"Elemento {objetivo} encontrado en la posición {resultado}.")
else:
  print(f"Elemento {objetivo} no encontrado en la lista.")