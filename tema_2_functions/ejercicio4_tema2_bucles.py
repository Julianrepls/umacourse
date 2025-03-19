print()
print("=== En este ejercicio vamos a introducir valores numéricos y compararlos para determinar el mayor y el menor ===")
print("=== Introduzca la palabra 'fin' para finalizar el programa ===")
print()
may = None
smal = None

while True:
        try:
            n = input("Introduzca un Número o la palabra fin> ")
            num_check = int(n)

            if may is None:
                may = num_check
            elif num_check > may:
                may = num_check
            if smal is None:
                smal = num_check
            elif num_check < smal:
                smal = num_check
        
        except ValueError:
            if n == "fin":
                if may == None:
                    print("No se ha introducido ningún número todavía")
                    continue
                if smal == None:
                    print("No se ha introducido ningún número todavía")
                    continue  
                else:
                    print("- FIN del programa -")
                    print()
                    print(f"El mayor es: {may}")
                    print(f"El menor es: {smal}")
            else:
                print(f"{n}, no es un número")
                continue
