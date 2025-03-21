class animal:
    species: None
    name: None
    sound: None
    # estas con las cosas que vamos a almacenar dentro de la clase animal

    def __init__(self, name, species, sound): #el self, funciona como un enlace

        self.name = name
        self.species = species
        self.sound = sound
        #asi es como se crea una plantilla para un animal

    def talk(self):
        print(f"{self.name} says {self.sound}")

#ahora vamos a crear una nueva clase, esto es la HERENCIA:

class bird(animal):
    
    color = None

    def __init__(self, color):
        self.name = "Bird"
        self.species = "Avian"
        self.sound = "Tweet"
        self.color = color
    # crear esta nueva clase (pájaro) nos permite heredar del perro el name, specie, sound 
    #   al llamar el "class bird(animal)" al poner animal ente parentesis heredamos todos los atribunos de animal
    #       incluso podemos agregarle otro atributo como el color



"""
VEAMOS OTRO EJEMPLO
"""

dog = animal("Dog", "canine", "Woof")
print(dog.name)
print(dog.sound)
dog.talk() #con esto estoy llamando correctamente la funcion 'talk'
print()

cow = animal("Cow", "Bo Taurus", "Muu") # así es como puedo crear un nuevo animal con la plantilla 
print(cow.sound) # de esta forma es como llamo al sonido que hace la vaca
cow.talk()
print()

polly = bird("Green") # aqui llamamos a nuestro pájaro Polly y le damos un color como bien hemos definido arriba el Color
polly.talk() # devuelve: Bird says Tweet
print(polly.color) # devuelve: greeen
print(polly.sound)

class player:
    name: None
    speed: None
    position: None
    nacionalidad: None
    skill: None

    def __init__(self, name, speed, position, nacionalidad, skill):
        self.name = name
        self.speed = speed
        self.position = position
        self.nacionalidad = nacionalidad
        self.skill = skill

    def tipo(self):
        print(f"{self.name} is a great {self.position}")

player1 = player("Mbape", "100", "delantero", "Francia", "goal killer")
print(player1.name)
player1.tipo()



"""
Veamos otro ejemplo más creando profesiones
"""

# vamos a crear 3 trabajos. 1: abogado, 2: profesor, 3: doctor 
# luego lo vamos a mostrar en pantalla usando las funciones integradas

class job:
    name = None
    salary = None
    hours = None
    
    def __init__(self, name, salary, hours):
        self.name = name
        self.salary = salary
        self.hours = hours

    def print(self):
        print("@@ JOB @@ ")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.hours:>10}")

class doctor(job): # RECUERDA: al llamar "doctor(job)"" estamos heredando el salario, horas del abogado y luego definimos y añadimos experience y speciality
    
    experience = None
    speciality = None

    def __init__(self, salary, hours, experience, speciality):
        self.name = "Doctor"
        self.salary = salary
        self.hours = hours
        self.experience = experience
        self.speciality = speciality

    def print(self):
        print("@@ JOB @@ ")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.hours:>10}") #recuerda los <15 y tal son para la alineación a la izq, derch y centro
        print(f"{self.experience:<10} {self.speciality:>21}")

class teacher(job):

    subject = None
    position = None

    def __init__(self, salary, experience, subject, position):
        self.name = "Teacher"
        self.salary = salary
        self.subjetct = subject
        self.experience = experience
        self.position = position

    def print(self):
        print("@@ JOB @@ ")
        print()
        print(f"{self.name:<10} {self.salary:^10} {self.experience:>10}") #recuerda los <15 y tal son para la alineación a la izq, derch y centro
        print(f"{self.subjetct:<10} {self.position:>21}")




lawyer = job("Lawyer", "~$100.000", "40")
lawyer.print()

doc = doctor("~$200.000", "35", "7 years", "Pediaric")
doc.print()

teach = teacher("~$50.0000", "3 years", "Maths", "Principal")
teach.print()