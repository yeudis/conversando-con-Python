# Programa: Conversando con Python
# Autor: Yeudis cabarcas algarin
print("¡Hola mundo!")

# Primera conversación
saludo = input("Tú: ")

if saludo.lower().strip() in ["hola", "hola python", "buenas", "hey"]:
    print("Python: ¡Hola! Mucho gusto en saludarte")
else:
    print("Python: ¡Hola! Es un placer hablar contigo.")


# Pregunta: ¿Quién eres?
pregunta = input("Tú: ")

if pregunta.lower().strip() in ["quien eres", "quien eres?", "¿quién eres?", "quien eres ?"]:
    print("Python: Soy Python.")
else:
    print("Python: No entendí tu pregunta.")


# Pregunta: ¿Python?
pregunta = input("Tú: ")

if pregunta.lower().strip() in ["python", "python, el lenguaje de programacion ?"]:
    print("Python: Yes, soy Monty Python.")
else:
    print("Python: Yes, soy Monty Python!")


# Pregunta: ¿Qué haces en realidad?
pregunta = input("Tú: ")

if pregunta.lower().strip() in [
    "que haces",
    "que haces?",
    "¿qué haces?",
    "¿qué haces",
    "que bien, y que haces en realidad python ?",
    "que haces en realidad?",
    "¿qué haces en realidad?",
    "¿qué haces en realidad"
]:
    print("""
Python: En realidad...

Soy un lenguaje que permite a las personas escribir instrucciones
para que un computador pueda realizar diferentes tareas.

Con Python puedes crear programas, automatizar procesos,
trabajar con datos, desarrollar aplicaciones, crear páginas web,
utilizar inteligencia artificial, realizar cálculos científicos
y muchas otras cosas.

Mi principal objetivo es permitir que los programadores puedan
crear soluciones de una manera sencilla, clara y eficiente.
""")
else:
    print("Python: No entendí tu pregunta.")

print("Python: ¡ahora ya sabes quién soy y cual es mi funcion!")

    
