def saludar(nombre_persona): # "nombre_persona" es un PARÁMETRO
 """Esta función recibe un nombre y muestra un saludo personalizado.""" # Docstring (opcional pero es buena práctica)
 mensaje = f"¡Hola, {nombre_persona}! ¡Qué bueno tenerte aquí!"
 print(mensaje)
 # Esta función no devuelve un valor explícito (retorna None por defecto)
def sumar(a, b): # "a" y "b" son PARÁMETROS
 """Esta función recibe dos números y devuelve su suma."""
 resultado_suma = a + b
 return resultado_suma # La palabra clave "return" devuelve un valor