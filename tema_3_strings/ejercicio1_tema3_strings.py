import random
print("""A partir de este String: 'X-DSPAM-Confidence: 0.6178' 
vamos a extraer el número que se encuentra después de los dos puntos y convertirlo a un número flotante.""")
print()
data = "X-DSPAM-Confidence: 0.6178"
place_1 = data.find(" ")
#print(place_1)

place_2 = data[19+1:]
print(f"El número que extraemos es: {place_2}")
n = float(place_2)
print(f"Y su conversión a flotante es: {n}")
print()

while True:
    gen = input("¿Desea generar un número aleatorio entre 0 y 1? (yes/no): ")
    gen = gen.lower()
    if gen == "yes":
        a = random.uniform(0.0, 1)
        a_round = round(a, 4)
        print()
        print(f"Vamos a extraer ahora otro número aleatorio")
        data2 = f'X-DSPAM-Confidence: {a_round}'
        place_3 = data2.find(" ")

        print(data2)
        #print(place_3)
        place_4 = data2[19+1:]
        print(f"El número que extraemos es: {place_4}")
        #print(type(place_4))

        n2 = float(place_4)

        #print(type(n2))
        print(f"Y su conversión a flotante es: {n2}")
        print()
        
    elif gen == "no":
        print("El programa se ha cerrado, hasta luego")
        exit()
    else:
        print("Por favor, introduzca una respuesta válida (yes o no)")
        continue



