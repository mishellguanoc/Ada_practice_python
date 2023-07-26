# Definición de variables de cada tipo de primitivo
cadena = "Hola, soy una cadena"
entero = 42
flotante = 3.14
booleano = True
caracter = 'A'

# Concatenando las otras variables a la cadena y guardando el resultado
resultado_concatenacion = cadena + str(entero) + str(flotante) + str(booleano) + caracter

#Límites de enteros y flotantes en Python:
""" Los enteros no tienen un límite fijo y en Pyhton 3 dependen del tamaño de la memoria disponible.
Los flotantes siguen el estándar IEEE 754 de punto flotante de doble precisión (64 bits),
lo que les proporciona una precisión de aproximadamente 15 a 17 dígitos decimales."""

# Fórmula de la suma de los primeros n números pares: Suma = n * (n + 1)
# Si tomamos n como un número entero, entonces necesitamos sumar los primeros n números pares.

n = int(input("Ingresa un número entero para calcular la suma de los primeros números pares: "))

suma_pares = n * (n + 1)

# Imprimiendo los resultados
print("Resultado de la concatenación:", resultado_concatenacion)
print("Suma de los primeros", n, "números pares:", suma_pares)
