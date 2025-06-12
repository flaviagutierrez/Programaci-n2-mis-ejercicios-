def busqueda_binaria(lista, elemento):
  inicio=0
  fin=len(lista) - 1
  while inicio<=fin:
    medio=(inicio+fin)//2
    valor_medio=lista[medio]
    if valor_medio==elemento:
      return medio
    elif elemento<valor_medio:
      fin=medio-1
    else:
      inicio=medio+1
  return -1
  