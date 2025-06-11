vector_misterioso = [12, 7, 19, 5, 3]

print("¡Bienvenido al juego del Vector Misterioso!")
print("Puedes hacer preguntas sobre la lista secreta usando comandos de Python.")
print("Por ejemplo:")
print(" - print(len(vector_misterioso))")
print(" - print(vector_misterioso[2])")
print(" - print(vector_misterioso[0] > 10)")
print("Escribe 'salir' para terminar el juego.\n")

while True:
    pregunta = input("Escribe tu pregunta sobre vector_misterioso: ").strip()

    if pregunta.lower() == "salir":
        print("Gracias por jugar. ¡Hasta luego!")
        break

    # Solo permitimos preguntas que empiezan con print para seguridad básica
    if not pregunta.startswith("print"):
        print("Por favor, escribe una pregunta que comience con print()")
        continue

    try:
        # Ejecutar la pregunta y mostrar resultado
        exec(pregunta)
    except Exception as e:
        print(f"Error al ejecutar la pregunta: {e}")