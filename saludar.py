def saludar(nombre_persona): # "nombre_persona" es un PARÁMETRO
 """Esta función recibe un nombre y muestra un saludo personalizado.""" # Docstring (opcional pero es buena práctica)
 mensaje = f"¡Hola, {nombre_persona}! ¡Qué bueno tenerte aquí!"
 print(mensaje)

# Pedir el nombre al usuario y llamar la función
nombre = input("¿Cómo te llamas? ")
saludar(nombre)
