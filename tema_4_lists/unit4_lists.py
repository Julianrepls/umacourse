friends = ['paco', 'manolo', 'javi']
for i in friends:
    print('Hola: ', i)

print(friends[1])

# con las listas podemos modificar segun posición
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)

# También podemos ver cuantos elementos tiene una lista de esta forma:
x = [3, 7,21,'joe', 78]
print(len(x)) # esto devuelve 5
# en su diferencia con los strings es que los strings los haciamos asi:
greet = 'Hello Bob'
print(len(greet)) #esto devuelve 9

# podemos crear listas de esta manera:
print(list(range(4)))
# tambien podemos hacer algo muy curioso con la posición de la lista:
friends = ['Paco', 'Fran', 'Miki']
print(list(range(len(friends))))
print(len(friends))

# Otra forma de iterar en las listas con el bucle for:
friends = ['Paco', 'Fran', 'Miki']
for i in range(len(friends)):  # este range nos devolveria 0, 1, 2
    i = friends[i]
    print('Hola: ', i)

# tenemos concatenación de listas:
a = [1, 2 ,3]
b = [4, 5, 6]
c = a + b
print(c)

# como moverse con litas:
t =[9, 41, 12, 3, 74, 15]
print(t[1:3]) # nos devuelve [41,12]
print(t[:4]) # esto nos devuelve [9, 41, 12, 3]
print(t[3:]) # nos devuelve [3, 74, 15]
print(t[:]) # nos devueleve la lista completa

