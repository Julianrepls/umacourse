# En este ejericio se nos pide reescribir el programa de pagos para incrementar en un factor de 1.5 las horas que se trabajen por encima de 40.
# Hasta 40 horas todas se cobran a precio normal
print("- Calculo de salario incrementando en 1.5 las horas trabajadas por encima de 40 -")
print()
while True:
    horas = int(input("Introduzca las horas> "))
    precio = float(input("Introduzca el precio/hora> "))

    if horas > 40:
        precio_extras = precio * 1.5
        extras = (40*precio) + ((horas - 40)*precio_extras)
        print(f"Total: {extras}")
    else:
        total = horas * precio
        print("Total: ", round(total, 2))

