# while True:
    
#     fname = input('Enter the file name: ')#con esto estamos preguntando al usuario que ingrese el nombre del archivo que quiere abrir si existe me lo abre y cuenta las linesas y sino da un error de que no existe el archivo
#     try:
#         fhand = open(fname)
#     except:
#         print('El archivo no pudo abrirse', fname)
#         fhand1 = open(fname)
#         count = 0   # contador de lineas
#         for line in fhand1:
#             count = count + 1 
#         print('Line Count:', count)


handfile = open('mbox.txt')
for line in handfile:
    if line.startswith('From:'): # "startswith" es un metodo que se usa para buscar una palabra en especifico, en este caso nos va buscar la palabra "From:" linea a linea.    
        print(line)

file = open('mbox.txt')
for line in file:
    line = line.rstrip() # "r.strip" esto lo que hace es quitar los espacios en blanco al final de la linea
    if line.startswith('From:'):
        print(line)
    if not line.startswith('From:'): #si la linea no empieza por "From:" entonces no la imprime y continua con la siguiente linea
        continue

# imaginamos que ahora queremos imprimir solo las lineas que contienen "@uct.ac.za"
# esto hace que si la linea no coniene "@uct.ac.za" entonces continua con la siguiente linea y si la linea si contiene "@uct.ac.za" entonces la imprime
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

# """ahora como apunte vamos a ver el modo "w" que es para escribir en un archivo 
# pero hay que tener cuidado porque si el archivo ya existe y escribimos algo nuevo en el archivo,
# entonces lo que escribimos nuevo en el archivo va a reemplazar todo lo que ya estaba en el archivo"""""
wescribir = open('mbox.txt', 'w')
line1 = "Hola, esto va a escribirse en el archivo\n"
wescribir.write(line1) # si usamos esta linea de código nos devuelve el numero de caracteres que tiene la linea que acabamos de escribir
wescribir.close()

# """ahora vamos a ver el modo "a" que es para escribir en un archivo pero si el archivo ya existe y escribimos algo nuevo en el archivo,
# entonces lo que escribimos nuevo en el archivo va a ser agregado al final del archivo"""
aescrbir = open('mbox.txt', 'a')
line2 = "y esto se añade\n"
aescrbir.write(line2)
aescrbir.close()