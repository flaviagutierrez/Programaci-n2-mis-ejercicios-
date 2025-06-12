def contar_elemento(lista, elemento_buscado):
  contador=0
  for elemento in lista:
    if elemento==elemento_buscado:
      contador += 1
  return contador