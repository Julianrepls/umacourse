while True:# while true el true significa que esa condición siempre va a ser cierta entonces el bucle seria infinito mientras la condición sea cierta
    line = input("> ")
    if line == "hecho":
        break # el break lo que hace es romper el buble.
    print(line)
print("bien hecho")

while True:
    line = input("> ")
    if line [0] == "#":
        continue # lo que hace continue es que vuelve al inicio del bucle. Aqui por ejemplo si escribimos # comprueba la primera letra de lo que escribes sea una almohadilla e ignora lo demas que escribas despues de la almohadilla
    if line == "hecho":
        break
    print(line)
print("Well done") 

#bucle definido:
for i in [5,4,3,2,1]:
    print(i)
print("despegue")

#otro ejemplo de bucle definido:
friends = ["Paco", "juli", "Dani"]
for friend in friends: # en este caso Friend (sin s) toma el valor de paco primero, luego de juli y asi recorriendo la lista de friends (con s)
    print("hola ", friend)
print("hecho")

#otro ejemplo de bucle definido:
#con este código buscamos cuale es el valor mas alto
largest = 0
print("Antes", largest)
for the_num in [2,7,3,9,8]:
    if the_num > largest:
        largest = the_num
    print(largest, the_num)
print("despues", largest)

#otro ejemplocon for:
#usamos este código para encontrar un valor determintado, en este caso sería el 3
found = False
print("Antes", found)
for value in [2,7,3,9,8]:
    if value == 3 :
        found = True
        print(f"Elemento encontrado {found}, {value}")
        break
    print(found, value)
print("despues", found)

#usamos este código para buscar cual es el valor mas pequeño

smallest = None
print('antes', smallest)
for val in [7, 9, 17, 15, 5]:
    if smallest is None:                    #el "is" es casi igual que el "==" pero el is es mas fuerte
        smallest = val
    elif val < smallest:
        smallest = val
    print(smallest, val)
print('déspues', smallest)

