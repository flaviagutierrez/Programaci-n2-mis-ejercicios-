from sumar_lista import sumar_lista
from mayor_lista import encontrar_mayor
from conteo_lista import contar_elemento
from invertir_lista import invertir_lista

numeros = [2,4,8,9,2,8,2]

print("Suma:", sumar_lista(numeros))
print("Mayor:", encontrar_mayor(numeros))
print("Conteo de 3:", contar_elemento(numeros, 3))
print("Lista invertida:", invertir_lista(numeros))