def  encontrar_mayor(lista):
  if not lista:
    return None
  mayor_temporal=lista [0]
  for numero in lista[1:]:
    if numero>mayor_temporal:
      mayor_temporal=numero
  return mayor_temporal