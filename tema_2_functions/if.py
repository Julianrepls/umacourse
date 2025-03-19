x = int(input("Introduce un nº: "))

# los if siempre se comprueban, caso distinto es el else o elif, los else o elif se comprueban solo si los if no son falsos.
if x >1:
    print("Mayor que 1")
    if x<100:
        print(f"{x} es menor que 100")
    if x>100:
        print(f"{x} es mayor que 100")
print("fin")
print()

print("----------------------------------------------")
y = float(input("Introduce un 2ndo nº: "))

if y > 1:
    print(f"{y} es mayor que 1")
elif y < 1:
    print(f"{y} es menor que 1")
elif y >50:
    print(f"{y} es mayor que 50")
elif y < 100:
    print(f"{y} es menor que 100")
else:
    print (f"{y} es mayor que 100")