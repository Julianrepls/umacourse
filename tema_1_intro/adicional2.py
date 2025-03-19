#calculador de edad
from datetime import datetime, timedelta

print("=== ¿Quieres saber cuántos años tendrás en el año que introduzcas? ¡Calculémoslo! ===")

birth = datetime(1989, 12, 16)
year = int(input("Introduce el año: "))
month = int(input("Introduce el nº del mes: "))
day = int(input("Introduce el dia: "))

event = datetime(year, month, day)
#print(type(event)) >>>> datetime
difference = (event - birth)
#print(type(difference)) >>>> timedelta
anos = int(difference.days /365.25)


print(f"En el año {event.year} tienes: {anos:.2f} años. ")
