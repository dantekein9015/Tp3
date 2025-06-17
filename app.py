# TP 3 - Condicionales
# Estudiante: Enrique Alejandro Juarez
# Materia: Programación - UTN A Distancia

# 1. Ver si es mayor de edad
edad = int(input("¿Qué edad tenés? "))
if edad > 18:
    print("Es mayor de edad")  # Si tiene más de 18, es mayor
else:
    print("Es menor de edad")

# 2. Ver si aprobó
nota = int(input("Ingresá tu nota: "))
if nota >= 6:
    print("Aprobado 😎")
else:
    print("Desaprobado 😥")

# 3. Verificar si el número es par
numero = int(input("Ingresá un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par ✌️")
else:
    print("Por favor, ingrese un número par")

# 4. Clasificación por edad
edad = int(input("Ingresá tu edad: "))
if edad < 12:
    print("Sos un niño/a 👶")
elif edad < 18:
    print("Sos adolescente 🧒")
elif edad < 30:
    print("Sos un adulto/a joven 🧑")
else:
    print("Sos un adulto/a 👨‍🦳")

# 5. Verificar longitud de contraseña
contraseña = input("Ingresá tu contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Contraseña correcta 🔐")
else:
    print("La contraseña debe tener entre 8 y 14 caracteres")

# 6. Calcular media, mediana y moda
import random
from statistics import mean, median, mode

numeros = [random.randint(1, 100) for _ in range(50)]
print("Lista generada:", numeros)

media = mean(numeros)
mediana = median(numeros)
moda = mode(numeros)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("Sesgo positivo ➕")
elif media < mediana < moda:
    print("Sesgo negativo ➖")
else:
    print("Sin sesgo 😐")

# 7. Agregar "!" si termina en vocal
frase = input("Ingresá una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

# 8. Transformar nombre según opción
nombre = input("Ingresá tu nombre: ")
print("Elegí una opción:")
print("1 - Nombre en MAYÚSCULAS")
print("2 - Nombre en minúsculas")
print("3 - Nombre con la primera letra en mayúscula")
opcion = int(input("Opción: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")

# 9. Clasificar magnitud de terremoto
magnitud = float(input("Ingresá la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (se siente pero no daña)")
elif magnitud < 6:
    print("Fuerte (daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy fuerte (daños importantes)")
else:
    print("Extremo (daños graves a gran escala)")

# 10. Detectar estación según hemisferio y fecha
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Mes? (1 al 12): "))
dia = int(input("¿Día? (1 al 31): "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
else:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

if hemisferio == "N":
    print(f"Estás en {estacion_norte} 🌍")
else:
    print(f"Estás en {estacion_sur} 🌎")
