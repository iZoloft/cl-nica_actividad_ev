from random import randint

num1 = int(input("Ingrese límite inferior\n"))
num2 = int(input("Ingrese límite superior\n"))
numero = randint(num1, num2)

adivine = int(input("Adivina el número \n"))

if numero % 2 != 0:
    numero = numero +1
if numero > num2:
    numero = numero -1

if adivine < num1 and adivine > num2:
    print("Número esta fuera del rango, intente otra vez")

if adivine == numero:
    print("Has adivinado el número")
else:
    print("Aún no adivinas el número")

if adivine > numero:
    print("El número a adivinar es menor")
else:
    print("El número a adivinar es mayor")

adivine2 = int(input("Intente otra vez\n"))

if adivine2 < num1 and adivine > num2:
    print("Número esta fuera del rango, intente otra vez")

if adivine2 == numero:
    print("Has adivinado el número")
else:
    print("Aún no adivinas el número")

if adivine2 > numero:
    print("El número a adivinar es menor")
else:
    print("El número a adivinar es mayor")

cercania1 = numero - adivine
cercania2 = numero - adivine2

if cercania1 < cercania2:
    print(f"El número esta mas cerca de {adivine} que de {adivine2}")
else:
    print(f"El número esta mas cerca de {adivine2} que de {adivine}")
adivine3 = int(input("Intente una ultima vez\n"))

if adivine3 < num1 and adivine > num2:
    print("Número esta fuera del rango, intente otra vez")

if adivine3 == numero:
    print("Has adivinado el número")
else:
    print(f"No adivinaste el número, el número era {numero}")