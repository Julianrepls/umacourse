print("En este ejercicio vamos a introducir un nombre completo y mostraremos en primer lugar los apellidos seguido del nombre.")
print("Por ejemplo, si introducimos 'Perico Delos Palotes', el programa nos devolverá 'Delos Palotes, Perico'.")
print()
while True:
    name = input("Introduzca su nombre: ")
    name = name.title()
    a = name.find(" ")
    b = name.find(" ", a + 1) # esto busca el siguiente espacio, es decir buscamos el espacio desde la posición (a+1)
    if a == -1:
        print("Debes introducir un nombre completo y no olvidar los apellidos.")
        print()
    elif a != -1:
        if b == -1:
            print("Debes introducir un nombre y apellidos separado con espacios.")
            print()
        elif b != -1:
                print()
                print(f"{name[a+1:b]} {name[b+1:]}, {name[:a+1]}")
                print()
        else:
            print("Debes introducir un nombre completo con los dos apellidos.")
            print()
            continue
    else:
        print("Debes introducir un nombre completo con los dos apellidos.")
        print()
        continue