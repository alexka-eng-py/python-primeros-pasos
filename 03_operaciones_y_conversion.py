# Ejercicio 1: Cálculo de descuento en tienda
precio_original = float(input("Ingresa el precio del producto: "))
descuento = float(input("Ingresa el monto del descuento: "))
precio_final = precio_original - descuento
print(f"El precio final con ${descuento} de descuento es: ${precio_final}")

# Ejercicio 2: Operaciones matemáticas (División)
valor_a = int(input("\nIngresa el primer número: "))
valor_b = int(input("Ingresa el segundo número: "))

if valor_b != 0:
    valor_c = valor_a / valor_b
    print(f"El resultado de dividir {valor_a} entre {valor_b} es: {valor_c}")
else:
    print("Error: No se puede dividir entre cero.")

# Ejercicio 3: Verificación de edad de nacimiento
año_nacimiento = int(input("\nAño de nacimiento: "))
edad = 2026 - año_nacimiento
verifica_edad = edad >= 18

print(f"Tienes {edad} años.")
print(f"¿Es mayor de edad?: {verifica_edad}")