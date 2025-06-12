# ... (definición de la función aquí arriba) ...
from busqueda_binaria import busqueda_binaria

mi_lista_desordenada = [10, 5, 42, 8, 17, 30, 25]
print("Probando busqueda_lineal...")
assert busqueda_binaria(mi_lista_desordenada, 42) == 2
assert busqueda_binaria(mi_lista_desordenada, 10) == 0 # Al inicio
assert busqueda_binaria(mi_lista_desordenada, 25) == 6 # Al final
assert busqueda_binaria(mi_lista_desordenada, 99) == -1 # No existe
assert busqueda_binaria([], 5) == -1
print("¡Pruebas para busqueda_lineal pasaron! ")