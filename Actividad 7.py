#Sergio José Santizo Barraza - 1018723
#Introducción a la Programación (Trabajo Supervidado)
#Pensamiento computacional Trabajo Supervidado Semana 11
#19 de octubre de 2023
#Objetivo: Crear un programa que realice varias operaciones con cadenas de texto.
#Entrada: Palabra o texto.
#Procesos principales: Realizar operaciones en las cadenas de texto proporcionadas por el usuario y mostrar los resultados en pantalla.
#Salida: Mostrar en pantalla las primeras tres letras de la palabra ingresadad por el usuario, una a la vez.

palabra = input("Ingrese una palabra: ")

print("Las primeras 3 letras de la palabra que ingresó son: ")
for letra in palabra[:3]:
    print(letra)

nueva_subcadena = palabra[:3]
print("La nueva subcadena formada por las primeras tres letras de su texto ingresado es: ", nueva_subcadena)

texto = input("Ingrese un nuevo texto: ")

texto_formado = ""
for caracter in texto:
    if caracter == "o":
        texto_formado += "X"
    else: 
        texto_formado += caracter

print("El texto formado es: ", texto_formado)

#Funciones de Python para el manejo de cadenas
#Función No. 1: Concatenar cadenas
#Dicha función crea una nueva cadena combinando dos cadenas mediante la concatenación.
#Ejemplo: 
adjetivo = "increíble"
sustantivo = "aventura"
frase = "¡Esta " + sustantivo + " fue muy " + adjetivo + "!"
print("Ejemplo de concatenación: ", frase)

#Función No. 2: Multiplicar cadenas
#Dicha función crea una nueva cadena repitiendo una cadena original múltiples veces.
#Ejemplo:
texto_original = "¡Fiesta! "
texto_repetido = texto_original[:8] * 4
print("Ejemplo de multiplicación: ", texto_repetido)