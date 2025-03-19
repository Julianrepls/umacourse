bolso = dict()
bolso['dinero'] = 12 #donde dinero es la key y 12 es su valor
bolso['caramelos'] = 3
bolso['papeles'] = 75
print(bolso) # esto nos arroja: {'dinero': 12, 'caramelos': 3, 'papeles': 75}

print(bolso['caramelos']) # arroja: 3
bolso['caramelos'] = bolso['caramelos'] + 2
print(bolso) # esto nos arroja: {'dinero': 12, 'caramelos': 5, 'papeles': 75}

# En las listas podíamos modificar de tal manera los elementos: 
lst = list()
lst.append(21)
lst.append(183)
print(lst) #arroja: [21,183]
lst[0] = 23 
print(lst) # esto arroja [23,183]
# Con los diccionarios lo hacemos de esta manera:
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd) #arroja: {'course': 182, 'age':21}

ddd['age'] = 23
print(ddd) #arroja: {'course': 182, 'age': 23} 

#También podemos crear diccionarios vacíos:
x = { }
print(x) #arroja: {}


#si queremos por ejemplo ver cuantas veces aparece un nombre en un diccionario
counts = dict()
names = ['sev', 'wen','quian','sev', 'wen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] +1
print(counts)

#si quiero comprobar si sev está en el diccionario:
'sev' in counts #devolvería True

if name in counts:
    x = counts[name]
else:
    x = 0
#sería lo mismo con la funcion "get()" ya que get comprueba si un valor está o no actualmente en un diccionario y si no está asume un valor por defecto.
x = counts.get(name,0)

# podemos hacer también comprobar si el nombre está en el diccionario y nos devuelve si está y su valor y sino
# nos da un valor por defecto y le sumamos 1:
counts = dict()
names = ['sev', 'wen','quian','sev', 'wen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts) # devuelve: {'sev': 2, 'wen': 2, 'quian': 1}


#podemos hacer un programa que nos cuente las palabras y despues imprimir cuantas veces aparece cada palabra
count = dict()
print('Escribe una línea')
line = input('')
words = line.split()
print('Palabras: ', words)
print('Contando...')
for word in words:
    count[word] = count.get(word, 0) +1
print('Cuentas', count)

# si escribo: bienvenidos bienvenidos a a a la grieta del del invocador invocador invocador invocador
# nos arrojaría:   Palabras:  ['bienvenidos', 'bienvenidos', 'a', 'a', 'a', 'la', 'grieta', 'del', 'del', 'invocador', 'invocador', 'invocador', 'invocador']
# Contando...
# Cuentas {'bienvenidos': 2, 'a': 3, 'la': 1, 'grieta': 1, 'del': 2, 'invocador': 4} 




# ==================== X ======================
jjj = {'chuck':1, 'fred': 42, 'jan':100}
print(list(jjj)) # ['jan', 'chuck', 'fred']
print(jjj.keys()) # ['jan', 'chuck', 'fred']
print(jjj.values()) # [100, 1, 42]
print(jjj.items()) #[('jan', 100), ('chuck', 1), ('fred', 42)] Esto nos devuelve tuplas, las tuplas son listas de pareja de valores, ejempl: ('jan', 100)


#sobre las tuplas podemos iterar como en este ejemplo:
jjj = {'chuck':1, 'fred': 42, 'jan':100}
for aaa,bbb in jjj.items():
    print(aaa,bbb)
    # jan 100
    # chuck 1
    # fred 42

#veamos otro ejemplo más:
name = input('Nombre de fichero_ ') # aquí preguntamos por el nombre del fichero
handle = open(name) # lo almacenamos en una variable

counts = dict()
for line in handle: # vamos leyendo linea a linea el fichero
    words = line.split() # extraemos las palabras para cada linea
    for word in words:
        counts[word] = counts.get(word, 0) +1  # para cada palabra de la línea vamos llevando  un control de cuantas palabras han aparecido
# aqui ya tenemos en counts cuantes veces aparece las palabras en nuestro fichero
bigcount= None
bigword = None
for word, count in counts.items(): # vamos iterando sobre los diferentes valores de nuestro diccionario counts para quedarnos con el valor máximo
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
