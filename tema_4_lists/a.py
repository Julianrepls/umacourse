# # name = input('Nombre de fichero_ ') # aquí preguntamos por el nombre del fichero

# handle = open('mbox-short.txt') # En este ejemplo lo vamos a hacer con nuestro documento 'mbox-short.txt'

# counts = dict()
# for line in handle: # vamos leyendo linea a linea el fichero
#     if not line.startswith('From '):
#         continue
#     words = line.split() # extraemos las palabras para cada linea
#     for word in words:
#         counts[word] = counts.get(word, 0) +1  # para cada palabra de la línea vamos llevando  un control de cuantas palabras han aparecido
# print(counts)
# # aqui ya tenemos en counts cuantes veces aparece las palabras en nuestro fichero
# bigcount= None
# bigword = None
# for word, count in counts.items(): # vamos iterando sobre los diferentes valores de nuestro diccionario counts para quedarnos con el valor máximo
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword, bigcount)

# counts = dict()
# names = ['sev', 'wen','quian','sev', 'wen']
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

