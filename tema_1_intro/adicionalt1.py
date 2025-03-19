
# vamos a crear una vision de futuro, pediremos al usuario que nos diga su nombre y le diremos con quien se casará, donde vivira y de que va a trabajar, así como cuantos hijos va a tener
import random

names = ["Sara", "Maria", "Nayara"]
index = random.randint(0,4)

cities = ["Nex York", "Fuengirola", "Shangai"]
nc = random.randint(0,3)

jobs = ["Fisio", "Peon de Albañil", "Manager", "Programador"]
work = random.randint(0, 4)


nHijos = random.randint(1, 10)
# nPareja = names[index]
# nCity = cities[nc]
# nTrabajo = jobs[work]

tuIde = str((input("Dime tu nombre y descubre el futuro> ")).capitalize())


print(f"{tuIde}, viviras en {cities[nc]}, estarás casado con {names[index]}, vas a tener {nHijos}, hijos y trabajaras como {jobs[work]}")

