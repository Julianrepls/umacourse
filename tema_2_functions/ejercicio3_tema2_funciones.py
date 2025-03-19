print("- Calculadora de salario con Definiciones de Funciones y Return -")
print()
def calcula_pago(x, y):
    if x > 0 or y > 0:   
        if x > 40:
            precio_extra = y * 1.5
            extras = (40*y) + ((x - 40)*precio_extra)
            return extras    
        else:
            total = x * y
            return total         
    else:
        print()
        return -1
        
while True:
    horas = input("Introduzca las horas trabajadas> ")
    precio = input("Introduzca el precio por hora> ")
    try:
        horasCheck = int(horas)
        precioCheck = float(precio)
    except ValueError:
        horasCheck = -1
        precioCheck = -1
        if horasCheck == -1:
            print("Error: Introduzca un número de HORAS válido!")
        elif precioCheck == -1:
            print("Error: Introduzca un número de PRECIO válido!")
            print()
        else:
            print("Error: Introduzca un número de HORAS y PRECIO válido!")
            print()

    # print(calcula_pago(horasCheck, precioCheck))
    calcula = calcula_pago(horasCheck, precioCheck)
    if calcula == -1:
        pass
    else:
        print(f"El salario total es: {calcula}")
        print()