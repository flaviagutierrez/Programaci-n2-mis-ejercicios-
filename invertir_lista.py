def invertir_lista(lista):
  lista_invertida=[]
  for i in range(len(lista)-1,-1,-1):
    lista_invertida.append(lista[i])
  return lista_invertida 