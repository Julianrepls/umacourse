print("""A partir del documento 'mbox-short.txt' vamos a leer las líneas que empiezan por 'From '.
Luego vamos a imprimir los correos que aparecen en esas líneas.
Por último daremos la posibilidad de no mostrar los repetidos """)
n = open('mbox-short.txt')
repeat = set()  # Para almacenar los elementos ya vistos
count = 0
for line in n:
    if not line.startswith('From '): 
        continue
    word = line.strip().split()  # Dividir la línea en elementos
#        HASTA AQUI vemos todos los emails y después vamos a eliminar los repetidos con las siguientes líneas de código  
    segundo_elemento = word[1]  # Tomar el segundo elemento
       
    if segundo_elemento not in repeat:
        print(segundo_elemento)  # Mostrar el elemento si no está repetido
        count += 1
        repeat.add(segundo_elemento)  # Agregarlo al conjunto
print()
print(f"Enviaron el correo {count} usuarios.")




# ============== EXPLICACION ===============
n = open('mbox-short.txt')
repeat = set()  # Para almacenar los elementos ya vistos
count = 0
print("""A partir del documento 'mbox-short.txt' vamos a leer las líneas que empiezan por 'From '.
Luego vamos a imprimir los correos que aparecen en esas líneas.
Por último daremos la posibilidad de no mostrar los repetidos """)
print()
for line in n:
    if not line.startswith('From '):
        continue
    word = line.strip().split()  # Dividir la línea en elementos   
    count += 1
    print(word[1])
print()
print(f"Enviaron {count}")
print()

while True:
    ask = input("DESEAS ELIMINAR LOS REPETIDOS?(YES/NO)")
    ask = ask.lower()
    if ask == 'yes':
        n = open('mbox-short.txt')
        repeat = set()  # Para almacenar los elementos ya vistos
        count = 0

        for line in n:
            if not line.startswith('From '): 
                continue
            word = line.strip().split()  # Dividir la línea en elementos   
            segundo_elemento = word[1]  # Tomar el segundo elemento
        
            if segundo_elemento not in repeat:
                print(segundo_elemento)  # Mostrar el elemento si no está repetido
                count += 1
                repeat.add(segundo_elemento)  # Agregarlo al conjunto
        print()    
        print(f"Enviaron el correo {count} usuarios.")
    else:
        print("Hasta pronto")
        break