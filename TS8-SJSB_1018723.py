#Sergio José Santizo Barraza - 1018723
#Introducción a la Programación (Laboratorio)
#Ejercicio 1 (Ts semana 8) Uso de ciclos FOR y WHILE.
#28 de septiembre de 2023

#Objetivo: Utilizar, tanto FOR como WHILE, para mostrar una secuencia en pantalla de los rangos solicitados en cada inciso.
#Entrada: En este caso no hay entrada, solo salida.
#Procesos principales: Tomar un número, incrementar o decrementar, según lo que se pide.
#Salida: Mostrar en pantalla las secuencias de los rangos solicitados.

#Inciso 1: Mostrar la secuencia de números en un rango de 1 a 25, incrementando de 1 en 1 con FOR.
for i in range(1, 26):
    print(i, end=', ')
print()  #Imprimir un salto de línea.

#Inciso 3: Mostrar la secuencia de números en un rango de 5 a 50, incrementando de 5 en 5 con FOR.
for i in range(5, 51, 5):
    print(i, end=', ')
print()  #Imprimir un salto de línea.

#Inciso 5: Mostrar la secuencia de números en un rango de 20 a 0, decrementando de 2 en 2 con FOR.
for i in range(20, -1, -2):
    print(i, end=', ')
print()  #Imprimir un salto de línea.

#Inciso 2: Mostrar la secuencia de números en un rango de 1 a 25, incrementando de 1 en 1 con WHILE.
n = 1
while n <= 25:
    print(n, end=', ')
    n += 1
print()  #Imprimir un salto de línea.

#Inciso 4: Mostrar la secuencia de números en un rango de 5 a 50, incrementando de 5 en 5 con WHILE.
n = 5
while n <= 50:
    print(n, end=', ')
    n += 5
print()  #Imprimir un salto de línea.

#Inciso 6: Mostrar la secuencia de números en un rango de 20 a 0, decrementando de 2 en 2 con WHILE.
n = 20
while n >= 0:
    print(n, end=', ')
    n -= 2
print()  #Imprimir un salto de línea.