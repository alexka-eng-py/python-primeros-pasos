# Ejercicio 1: Control de acceso por edad
edad = int(input("¿Cuál es tu edad?: "))
if edad >= 18:
    print(f"Tienes {edad} años. ¡Bienvenido, puedes pasar!")
else:
    print(f"Tienes {edad} años. ¡Lo siento, eres menor de edad!")

# Ejercicio 2: Límite de velocidad
velocidad = int(input("\n¿Cuál es tu velocidad actual?: "))
if velocidad > 80:
    print("¡Vas a exceso de velocidad, puedes recibir una multa!")
elif velocidad == 80:
    print("¡Estás llegando al límite!")
else:
    print("¡Buena velocidad, que tengas buen viaje!")

# Ejercicio 3: Semaforo
color = input("\n¿De qué color está el semáforo? (rojo, amarillo, verde): ").strip().lower()
if color == "rojo":
    print("¡Alto! Detén el vehículo.")
elif color == "amarillo":
    print("Precaución, reduzca la velocidad.")
elif color == "verde":
    print("Sigue adelante, tienes pase libre.")
else:
    print("Color no reconocido.")

# Ejercicio 4: Verificación de descuento por membresía u edad
edad_cliente = int(input("\n¿Cuál es tu edad?: "))
tiene_membresia = input("¿Tienes membresía? (si/no): ").strip().lower()

if edad_cliente > 65 or tiene_membresia == "si":
    print("¡Felicidades! Tienes un 20% de descuento.")
else:
    print("Pagas tarifa normal.")