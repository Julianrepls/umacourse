print("""En este ejercicio vamos leer linea a linea el archivo 'Romeo.txt'
Después vamos a crear una única lista con todas las palabras del archivo y las vamos ordenar afabéticamente.
Por último la vamos a mostrar en pantalla""")
print()

box = []
file = open('romeo.txt')
    
for linea in file:
    words = linea.split()
    box.extend(words)

for i in range(len(box)):
    box[i] = box[i].lower()
box.sort()
file.close()
print(box)
# print(len(box))
