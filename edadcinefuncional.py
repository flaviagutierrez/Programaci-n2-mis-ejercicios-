def obtener_clasificacion_pelicula(edad_persona):
  if edad_persona < 0:
      return "Edad no válida. Por favor, ingresa un número positivo."
  elif edad_persona >= 18:
      return "¡Puedes ver películas clasificadas R!"
  elif edad_persona >= 13:
      return "Puedes ver películas clasificadas PG-13."
  else:
      return "Te recomendamos películas clasificadas G o PG."

# Programa Principal:
edad_str = input("Bienvenido al cine, ¿cuál es tu edad?: ")
edad = int(edad_str)

mensaje_cine = obtener_clasificacion_pelicula(edad)
print(mensaje_cine)