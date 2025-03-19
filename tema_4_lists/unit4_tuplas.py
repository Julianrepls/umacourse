#las tuplas guardan semejanzas con las litas
#las tuplas son varios elementos que están emparejados
#al contrario de las listas, una vez creas la tupla no se puede alterar su contenido
# por ejemplo:
x = (5, 4, 3)
x[2] = 0 # esto da Error porque no puedes cambiar el valor
x.short() #esto ordenaba una lista, pero aquí nos de Error, con lo cual no se puede hacer
x.append(5) #esto también nos da Error, no se puede añadir elementos
x.reverse() #también nos da Error

names = ('Paco', 'Juli', 'Josefa')
print(names[2]) #muestra: Josefa

num = (1 ,9, 2)
print(num) # (1, 9, 2)
print(max(num)) # 9

for iter in num:
    print(iter) 
    # 1
    # 9
    # 2


#para ver que cosas podíamos hacer con la lista hacíamos:
n = list()
dir(n) # Esto nos arroja lo que podemos hacer con la lista: [append, count, extend, index, insert, pop, remove, reverse, sort]
#para ver que cosas podemos hacer con las tuplas hacemos un dir de tuplas a ver que opciones nos da
t = tuple()
dir(t) # Esto nos arroja las funciones de: [count, index]


#ejemplos tuplas:
(x,y) = (4, 'Fred')
print(y) # Fred
(a, b) = (99, 98)
print(a) # 99


#podemos ver tuplas también en los diccionarios:
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)
    # nos arroja:
    # csev 2
    # cwen 4
tups = d.items()
print(tups) # nos devuelve: dict_items([)'csev', 2)], (cwen, 4)])

# las tuplas son comparables
(0, 1, 2) < (5, 1, 2) #true
(0, 1, 2000000) < (0, 3, 4)#True
('Jones', 'Sally') < ('Jones', 'Sam') #true
('Jones', 'Sally') > ('Adams', 'Sam') #true


#Como ORDENAR tuplas:
d = {'a':10, 'b':1, 'c':22}
d.items() # Esta funcion items, te devuelve los items del diccionario

print(d) #{'a': 10, 'b': 1, 'c': 22}
dict_items([('a', 10), ('c', 22), ('b', 1)])
sorted(d.items()) # La función sorted nos ordena las tuplas
print(d) #{'a': 10, 'b': 1, 'c': 22}

x = {'a': 10, 'b': 1, 'c': 22}
t = sorted(x.items())
print(t)  # [('a', 10), ('b', 1), ('c', 22)]
for k, v in sorted(x.items()):
    print(k, v) # k=key v=valor
    # a 10
    # b 1
    # c 22


# si a lo mejor queremos ordenar por valores en lugar de por las claves como hicimos en el ejempl anterior haríamos esto:
c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append( (v, k) ) #aquí ya le damos la vuelta
print(tmp) #[(10, 'a'), (1, 'b'), (22, 'c')]
tmp = sorted(tmp, reverse=True) # reverse en esta ocasión nos ordena de mayor a menor
print(tmp)


# Veamos ahora las 10 palabras mas comunes o qu más aparecen en el fichero 'romeo.txt'
fhand = open('romeo.txt')
counts = {}
for line in fhand: # leemos línea a línea
    words = line.split() # cada línea la partimos en palabras
    for word in words:
        counts[word] = counts.get(word, 0) + 1 #contamos las palabras y con esto tenemos en counts cuantas veces aparece cada palabra

lis = [] #cramos una lista
for key, val in counts.items(): # vamos iterando por nuestro diccionario de palabras 'counts'
    newtup = (val, key) # vamos creando nuevas tuplas donde ponemos el Val:cuantas veces aparece esa palbra; y Key: la palbra en sí. Le hemos dado la vuelta a key valor
    lis.append(newtup) # esto anterior lo añadimos a la nueva lista 'lis'. Esto llegado a este punto muestra cuantas veces a parece y la palabra
lis = sorted(lis, reverse=True) # ordenamos por nº de apariciones

for val, key in lis[:10]:  # si queremos las 10 palabras que más aparece
    print(key, val)


# LISTAS COMPRENSION
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v, k) for k, v in c.items()])) #[(1, 'b'), (10, 'a'), (22, 'c')]
# esto se utiliza para crear estructura de una lista
# lo que hacemos en este ejempl es: le estamos diciendo créame una lista donde vas a añadir para cada k y v que me devuelve c.items
# me vas a crear un nuevo elemento en la lista (v, k) dando la vuelta a valor y key. Después con el sorted la ordenamos