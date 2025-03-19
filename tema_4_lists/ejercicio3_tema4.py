print("""
1) A partir de nuestro documento 'mbox-short.txt' vamos a leer las líneas que empiezan por 'From '.
2) Luego vamos a imprimir los correos que aparecen en esas líneas. Tomando la segunda palabra de la línea From como la persona que envió el email.
3) A continuación vamos a crear un diccionario, contar los correos y mostrar cual es la persona que mas emails ha enviado y cuantos ha enviado.
""")

n = open('mbox-short.txt')
counts = dict()

for line in n:
    if not line.startswith('From '):
        continue
    words = line.split()  # Dividir las líneas  que empiecen por 'From ' en palabras
    correo = words[1]
    counts[correo] = counts.get(correo, 0) + 1

print('Veamos los emails y el nº de emails enviados:')
print()
for clave, valor in counts.items():
    print(f"{clave}: {valor}")
#print(counts)

bigcount= None
bigword = None
for word, count in counts.items(): # vamos iterando sobre los diferentes valores de nuestro diccionario counts para quedarnos con el valor máximo
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print()
print(f"""
Este es el correo más repetido: "{bigword}" 
Con un nº de: {bigcount} correos enviados.""")
print()
print(bigword, bigcount)
print()
n.close()