print("""
-   En este ejercicio se nos pide escribir un programa que pregunte por el nombre del archivo (en este caso lo hice con
el archivo 'mbox-short.txt' que nos proporcionas en el aula virtual, tema 3)

-   Abrimos el archivo y mostramos las lineas en las que aparezca 'X-DSPAM-Confidence: 0.84750',
extraer los valores flotantes de cada una de ellas calculando el promedio y mostrándolo al final.


""")

def file_exists(file):
    a = False
    suma_total = 0
    word = "X-DSPAM-Confidence:"
    count = 0

    with open(file, 'r') as f:
        for line in f:
                line = line.rstrip()
                if 'X-DSPAM-Confidence:' in line:
                    a = True
                    print(line)
                    
    with open(file, "r") as archivo:
        for linea in archivo:
            if word in linea:
                numero = float(linea.split(word,1)[1].strip())
                suma_total += numero
                count += 1
                # print(numero)
        # print(count)
        total = suma_total / count
        print()
        return total
                   
    if a:
        return True

while True:
    file = input('Introduce el nombre del archivo: ')
    try:
        # file = input('Introduce el nombre del archivo: ')
        with open(file, 'r') as f:
            fread = f.read()
            print()
            print(f"El archivo '{file}' existe y estas son las filas donde aparece 'X-DSPAM-Confidence':")
            print()
            if file:
                llamada = file_exists(file)
                print(f"El promedio resultante es: {llamada}")
                print()
            f.close()

    except FileNotFoundError:
        print(f"El archivo {file} no existe, inténtelo de nuevo")
        

