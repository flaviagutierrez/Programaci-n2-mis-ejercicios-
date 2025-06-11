mis_notas=[100, 78, 84, 69.9, 80, 99.9, 78, 100, 96]

suma_total=0
for nota in mis_notas:
    suma_total += nota

promedio=suma_total/len(mis_notas)
print(f"La suma total de mis notas es: {suma_total}")
print(f"El promedio de mis notas es: {promedio:1f}")
print("Flavia Gutierrez")