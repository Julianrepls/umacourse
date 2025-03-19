box = []
# Crear una lista vacía para almacenar las palabras

# Abrir el archivo en modo de lectura
file = open('romeo.txt')
    # Leer cada línea del archivo
for linea in file:
    # Dividir la línea en palabras
    palabras = linea.split()
    # Agregar cada palabra a la lista
    box.extend(palabras)
#palabras.sort()
# Imprimir la lista con todas las palabras
#print(nox)
for i in range(len(box)):
    box[i] = box[i].lower()
box.sort()
print(box)


