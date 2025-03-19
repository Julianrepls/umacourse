#veamos cómo concatenar strings
# Para concatenar strings, simplemente se suman
n1 = "Hello"
n2 = "there"

bob = n1 + n2
print(bob)
# Esto nos arrojará Hellothere

# Si queremos concatenar un número con un string, debemos convertir el número a string
n3 = "123"
#n4 = n3 + 1 Esto nos arrojará un error
n4 = int(n3) + 1
print(n4) # esto nos arrojará 124

apple = input("escribe un numero: ")
x = apple - 10
print(x)
# Esto nos arrojará 90


fruit = "banana"
letter = fruit[1]
print(letter)
# Esto nos arrojará a
x = 3
w = fruit[x - 1]
print(w)  
# Esto nos arrojará n

zot = "abc"
print(zot[5])
# Esto nos arrojará un error

# Si queremos imprimir la longitud de un string, usamos la función len()
fruit = "banana"
print(len(fruit))
# Esto nos arrojará 6

fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
# Esto nos arrojará 0 b, 1 a, 2 n, es decir letra por letra y su posición

fruit = "banana"
for letter in fruit:
    print(letter)
# Esto nos arrojará b, a, n, a, n, a


word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count = count + 1
print(count)
# Esto nos dira cuantas veces se repite la letra "a" en la palabra banana

#lower.( ) convierte el string a minúsculas
greet = "Hello Bob"
zap = greet.lower()
print(zap)
# Esto nos arrojará "hello bob"
zat = greet.upper()
print(zat)
# Esto nos arrojará "HELLO BOB"

greet = "Hello Bob"
nstr = greet.replace("Bob", "Jane")
print(nstr)
# Esto nos arrojará "Hello Jane"
nstr = greet.replace("o", "X")
print(nstr)
# Esto nos arrojará "HellX BXb"

greet = " Hello Bob "
print(greet.lstrip())
# Esto nos arrojará "Hello Bob " borra los espacios a la izquierda
print(greet.rstrip())
# Esto nos arrojará " Hello Bob" borra los espacios a la derecha
print(greet.strip())
# Esto nos arrojará "Hello Bob" borra los espacios a ambos lados



