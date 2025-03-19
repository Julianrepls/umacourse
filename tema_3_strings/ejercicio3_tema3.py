def password(pw):
    longitud = len(pw)
    mayuscula = False
    digito = False
    if len(pw) > 8:
       longitud = True 
    else:
        longitud = False 
    for i in range(len(pw)):
        if pw[i].isdigit():
            digito = True
        if pw[i].isupper():
            mayuscula = True
    if longitud and mayuscula and digito:
        return True
    else:
        return False
    
print("= En este ejercicio vamos a crear una contraseña segura =")
print("= Para que la contraseña sea válidad debe contener al menos: una letra Mayus, un digito y mínimo 8 caracteres =")
print()
while True: 
    try:
        pw = input("Introduce una contraseña: ")
        a = pw.find(" ")
        h1 = password(pw)
        if a != -1:
            print("Error: La contraseña NO puede contener espacios, intenta de nuevo")
            print()
        elif h1:
            print("La contraseña es VALIDA")
            print()
        else:
            print("Error: La contraseña NO es válida, intenta de nuevo")
            print()            
    except ValueError:
        pass
        
