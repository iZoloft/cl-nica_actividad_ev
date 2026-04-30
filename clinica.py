PLAN_DENTAL = 80000
RADIOGRAFIA_DENTAL = 12000

try:
    nombre = input("Ingrese su nombre \n")
    edad= int(input("Ingrese su edad \n"))
    quintil = int(input("Ingrese el quintil en el que se encuentra (1 a 5)\n"))
    if edad > 0 and (quintil >= 1 and quintil < 5):
        if edad <= 25 and (quintil == 1 or quintil == 2):
            descuento_plan = .18
        elif edad <= 25 and (quintil == 3 or quintil == 4):
            descuento_plan = .12
        elif (edad >= 26 and edad <= 45) and (quintil == 1 or quintil == 2):
            descuento_plan = .12
        elif (edad >= 26 and edad <= 45) and (quintil == 3 or quintil == 4):
            descuento_plan = .08
        else:
            descuento_plan = 0
        
        if quintil == 1 or quintil == 2 or quintil == 3:
            descuento_radiografia = .10
            if edad >= 40:
                descuento_edad = .05
            else:
                descuento_edad = 0
        else:
            descuento_edad = 0
            descuento_radiografia = 0
        
        total_plan = PLAN_DENTAL - (PLAN_DENTAL * descuento_plan)
        total_radiografia = RADIOGRAFIA_DENTAL - (RADIOGRAFIA_DENTAL * descuento_radiografia) - (RADIOGRAFIA_DENTAL * descuento_edad)
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Quintil: {quintil}")
        print(f"Valor plan: {total_plan}")
        print(f"Valor radiografia: {total_radiografia}")
except:
    print("Valor debe ser numérico")
