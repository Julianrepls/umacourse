# En este ejercicio se nos pide reescribir el programa de pagos con try y except para que se manejen adecuadamente
# entradas no numéricas.
print("- Calculadora de pagos con Try y Except para manejar errores de entrada no numérica -")
print()
while True:
    horas = input("Introduzca las horas trabajadas> ")
    precio = input("Introduzca el precio por hora> ")

    try:
        horasCheck = int(horas)
        precioCheck = float(precio)
    except ValueError:
        horasCheck = -1
        precioCheck = -1

    if horasCheck > 0 or precioCheck > 0:
        
        if horasCheck > 40:
            precio_extra = precioCheck * 1.5
            extras = (40*precioCheck) + ((horasCheck - 40)*precio_extra)
            print(f"Total: {extras}")
            
        else:
            total = horasCheck * precioCheck
            print("Total: ", round(total, 2))
            
    else:
        print()
        print("Error, por favor introduzca un número")
        print()