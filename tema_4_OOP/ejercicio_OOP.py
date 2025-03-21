"""
En este ejemplo de Programación orientada a objetos vamos a crear unos personajes
1) Vamos a clasificarlo por nombre, vida y puntos
2) Deben tener un método para imprimir esos datos de cada personaje
3) Luego vamos a heredar esos datos para crear un jugador el cuál debe tener 3 vidas y un método al que cuando le llamemos nos diga si esta vivo o muerto
4) También del constructor personaje, vamos a crear un enemigo del cual debemos saber que tipo de enemigo es y la fuerza que tiene
5) Luego además vamos a heredar esto para crear 3 enemigos mas; 2 orcos que deben especificar su velocidad y 1 vampiro que va a dectectar si es de día/noche

"""
class character:
    name: None
    health = 100
    points = 120

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"{self.name}\tHP: {self.health}\tPoints:{self.points}")

    def setStats(self, health, points):
        self.health = health
        self.points = points

#vamos a crear la variable del jugador
class player(character):
    nickname = None
    lives = 5

    def __init__(self, nickname):
        self.name = "Player"
        self.nickname = nickname

    def print(self):
        print(f"{self.name}\tHP:{self.health}\tPoints: {self.points}\tNickname: {self.nickname}\tLives:{self.lives}")
        # Al llamarlo nos va a devolver: Player  HP:100  Points: 120     Nickname: Bocaseca Man  Lives:5
        #nota: la \t lo que hace es meter tabulaciones, recuerda la \n para salto de línea
    def isAlive(self):
        if self.lives > 0:
            print(f"{self.nickname} is already alive!")
            return True
        else:
            print(f"{self.nickname} is dead")
            return False

bocaSeca = player("Bocaseca Man")
bocaSeca.print()
print(bocaSeca.isAlive())

# a continuacion el enemigo
class enemy(character):
    type = None
    strength = None

    def __init__(self, name, type, strength):
        self.name = name
        self.type = type
        self.strength = strength
        
    def  print(self):
        print(f"{self.name}\tHP:{self.health}\tPoints: {self.points}\tType: {self.type}\tStregth:{self.strength}")
        
class orc(enemy):
    speed = None

    def __init__(self, speed):
        self.name = "Orc"
        self.type = "Orc"
        self.strength = 200
        self.speed = speed
        
    def  print(self):
        print(f"{self.name}\tHP:{self.health}\tPoints: {self.points}\tType: {self.type}\tStregth: {self.strength}\tSpeed: {self.speed}")
      
uruk = orc(250) # speed = 250
trol = orc(205)

uruk.print()
trol.print()


# por último la clase del vampiro
class vampire(enemy):
    day = True

    def __init__(self, day):
        self.name = "VampirE"
        self.type = "VAmpire"
        self.strength = 150
        self.day = day

    def print(self):
        print(f"{self.name}\tHP:{self.health}\tPoints: {self.points}\tType: {self.type}\tStregth: {self.strength}\tDay: {self.day}")

dracula = vampire(False)
dracula.print()