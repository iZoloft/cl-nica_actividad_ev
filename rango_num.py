from random import randint

num1 = int(input("Ingrese límite inferior\n"))
num2 = int(input("Ingrese límite superior\n"))
numero = randint(num1, num2)

try:

    if numero % 2 != 0:
        numero = numero + 1
        if numero > num2:
            numero = numero - 2
    adivina = int(input("Adivine el número \n"))
    if adivina >= num1 and adivina <= num2:
        if adivina == numero:
            print("Adivinaste!")
        else:
            print("Intente otra vez")
            if numero > adivina:
                print("El número es mayor")
            else:
                print("El número es menor")
            adivina2 = int(input("Intente denuevo\n"))
            if adivina2 == numero:
                print("Adivinaste")
            else:
                print("Intente otra vez")
                if numero > adivina2:
                    print("El número es mayor")
                else:
                    print("El número es menor")
                if numero > adivina:
                    distancia1 = numero - adivina
                else:
                    distancia1 = adivina - numero
                if numero > adivina2:
                    distancia2 = numero - adivina2
                else:
                    distancia2 = adivina2 - numero
                
                if distancia1 < distancia2:
                    print(f"El número esta más cerca de {adivina}")
                else:
                    print(f"El número esta más cerca de {adivina2}")
                adivina3 = int(input("Intente la última vez \n"))
                if adivina3 == numero:
                    print("Adivinaste")
                else:
                    print(f"El número era {numero}")
    else:
        print("el número adivinado debe estar dentro de los limites")
except:
    print("debe ser un número entero")