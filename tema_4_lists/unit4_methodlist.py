# podemos crear listas de la siguiete forma:
z = list()
type(z)
dir(z) # esto nos va a arrojar las diferentes operaciones que podemos hacer con ellas

# 1º creamos lista:
# 2º con el 'append' vamos agregando elementos a la lista:
y = list()
y.append('book') # podemos agregar cadena de texto
y.append(99) # podemos agregar números también
print(y)

# podemos comprobar de esta manera si un elemento está en la lista:
some = [1, 9, 21, 10, 16]
9 in some # esto nos devuélve un True

# esta operación  'sort' es muy importante porque nos ordena los elementos de una lista:
friends = ['Paco', 'Juli', 'Josefa']
friends.sort()
print(friends) # esto nos devuelve: ['Josefa', 'Juli', 'Paco']

# Ahora vamos a ver 'pop', esto lo que hace es que podemos sacar un elemento de una lista y almacenarlo en una variable.
n = ['a', 'b', 'c']
f = n.pop(1) # la 'b' se queda almecenado en la variable "f"
print(n) # esto nos devuelve ['a', 'c']

# Podemos usar "del" para eleniminar un elemento:
m = ['a', 'b', 'c']
del m[1] 
print(m) # esto nos devuelve ['a', 'c']


# Si no sabemos la posición del elemento pero si su nombre podemos usar "remove":
p = ['a', 'b', 'c']
p.remove('b')
print(p) #esto nos devuelve ['a', 'c']


# Vamos a ver ahora algunas matemáticas que podríamos hacer con listas:
nums = [3, 41, 12, 9, 74, 15]
print(len(nums)) # devuelve: 6
print(max(nums)) # devuelve: 74
print(min(nums)) # devuelve:3
print(sum(nums)) # devuelve: 154
print(sum(nums)/len(nums)) # devuelve:25.6


#vamos a hacer un ejemplo de como hacer la media en una lista:
numlist = list()
while True:
    inp = input('Escribe un número: ')
    if inp =='fin': 
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist)/len(numlist)
print('La Media es:', average)


#veamos que hace " slplit() "
abc = 'with three words'
cba = abc.split() # el "split" nos hace una lista y divide el 'string' en un elemento cada vez que encuentre un espacio. En esta frase hay 3 palabras 3 espacios 
print(cba)
print(len(cba)) # devuelve 3
print(cba[0]) # esto nos devuelve "with"


abc = ['with three words']
print(abc)
for w in abc:
    print(w) # esto nos arrojaría: with three words

line = 'A lot                            espaces'
etc = line.split()
print(etc) # esto nos arroja: ['A', 'lot', 'espaces'] eliminando los espacios

lin = 'first;second;third'
thing = lin.split()
print(thing) # esto nos arroja: ['first;second;third']
print(len(thing)) # esto nos arroja: 1 porque lo considera todo el string como una sola palabra
thing = lin.split(';') # aqui de esta forma le indicamos que el separador es el punto y coma
print(thing) # Arroja: ['first', 'second', 'third']
print(len(thing)) # Arroja: 3


# vemos que podemos hacer con rstrip()
texto = "Hola mundo!!!"
texto_limpio = texto.rstrip("!")
print(texto_limpio) # esto imprime: Hola mundo


# Sobre esta línea del texto mbox-short vamos a extraer los dias(Sat, Sun..): 
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
arepa = open('mbox-short.txt')
for line in arepa:
    line = line.rstrip() #elimina los espacios en blanco (o caracteres especificados) al final de una cadena
    if not line.startswith('From'): continue
    wor = line.split()
    print(wor[2]) # esto nos arroja Sat, Fri, Fri....