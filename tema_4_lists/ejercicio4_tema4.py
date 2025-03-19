print(""""
1) Vamos a escribir un programa que lea nuestro archivo mbox-short.txt y muestre la distribución por horas.
2) Extraeremos la hora de las líneas que comiencen por 'From '.
3) Una vez obtenemos el total de mensajes en cada hora, mostramos los totales ordenados por hora.
""")


f = open('mbox-short.txt')
counter = 0
d = dict()
for i in f:
    if not i.startswith('From '): continue #buscamos las líneas que solo empiecen por 'From'
    counter += 1
    # print(i, end='')
    a = i.find(":") # buscamos una primera posición hasta el primer delimitador horario ":" (tipo: string)
    b = a - 2 # hallamos la segunda posición que sería la posción "a" -2, esto nos arrojaría la hora (tipo: string)
    line = i[b:a] #aquí acotamos buscando solo las horas de cada línea
    line = line.split() # partimos las líneas en listas en las que solo aparece la hora de las líneas que empiezan por 'From'
    # print(line)
    for horas in line:
        d[horas] = d.get(horas, 0) + 1  # iteramos cada línea contando el nº de veces que aparece cada hora y agreagamos al diccionario
    # print(d)

lst = []   # creo una lista
for key, val in d.items():  # iteramos sobre nuestro diccionario(d), con la plabra clave(key) y su valor(val)
    tup = (key, val) # vamos creando nuevas tuplas de tipo clave, valor
    lst.append(tup) # agregamos las tuplas a la lista
    lst = sorted(lst) # ordenamos la lista
# print(lst)
print("Este sería el total de mensajes por hora:")
for key, val in lst: # iteramos sobre la lista ya ordenada y mostramos los key y su valor
    print(key, val) 

f.close()
