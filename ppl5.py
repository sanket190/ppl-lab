class Animal:
    def __init__(self, name):
        print("{} is animal".format(self.name))


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)


class lion(NonWingedMammal,NonMarineMammal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        super().__init__('Lion')


    def __str__(self):
        return ("{} sounds is {}".format(self.name,self.sound))


    def speed(speed):
        print("speed of lion is {} km/h".format(speed))



class tiger(NonWingedMammal,NonMarineMammal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        super().__init__('Tiger')


    def __str__(self):
        return ("{} sounds is {}".format(self.name,self.sound))


    def speed(speed):
        print("speed of tiger is {} km/h".format(speed))


class elephant(NonWingedMammal,NonMarineMammal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        super().__init__('elephant')


    def __str__(self):
        return ("{} sounds is {}".format(self.name,self.sound))


    def speed(speed):
        print("speed of elephant is {} km/h".format(speed))


class monkey(NonWingedMammal,NonMarineMammal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        super().__init__('monkey')


    def __str__(self):
        return ("{} sounds is {}".format(self.name,self.sound))


    def speed(speed):
        print("speed of monkey is {} km/h".format(speed))


class dog(NonWingedMammal,NonMarineMammal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        super().__init__('dog')


    def __str__(self):
        return ("{} sounds is {}".format(self.name,self.sound))


    def speed(speed):
        print("speed of dog is {} km/h".format(speed))

class cat(NonWingedMammal,NonMarineMammal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        super().__init__('cat')


    def __str__(self):
        return ("{} sounds is {}".format(self.name,self.sound))


    def speed(speed):
        print("speed of cat is {} km/h".format(speed))

class rabbit(NonWingedMammal,NonMarineMammal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        super().__init__('rabbit')


    def __str__(self):
        return ("{} sounds is {}".format(self.name,self.sound))


    def speed(speed):
        print("speed of rabbit is {} km/h".format(speed))

class parrot(NonMarineMammal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        super().__init__('parrot')


    def __str__(self):
        return ("{} sounds is {}".format(self.name,self.sound))


    def speed(speed):
        print("speed of parrot is {} km/h".format(speed))

class crow(NonMarineMammal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        super().__init__('crow')


    def __str__(self):
        return ("{} sounds is {}".format(self.name,self.sound))


    def speed(speed):
        print("speed of crow is {} km/h".format(speed))

class bat(NonMarineMammal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        super().__init__('bat')


    def __str__(self):
        return ("{} sounds is {}".format(self.name,self.sound))


    def speed(speed):
        print("speed of bat is {} km/h".format(speed))


d = lion("Lion","roar")
print(d)
print(lion.speed('80'))
print(' ')

d = tiger("tiger","roar")
print(d)
print(tiger.speed('80'))
print(' ')


d = elephant("elephant","trump trump")
print(d)
print(elephant.speed('10'))
print(' ')


d = bat("bat","ultrasonics")
print(d)
print(bat.speed('120'))
print(' ')


d = cat("cat","meow meow")
print(d)
print(cat.speed('40'))
print(' ')


d = dog("dog","bow bow")
print(d)
print(dog.speed('45'))
print(' ')


d = crow("crow","crow crow")
print(d)
print(crow.speed('80'))
print(' ')


d = parrot("parrot","peo")
print(d)
print(parrot.speed('100'))
print(' ')


d = rabbit("rabbit","trio trio")
print(d)
print(rabbit.speed('80'))
print(' ')


d = monkey("monkey","oh oh aa aa")
print(d)
print(monkey.speed('55'))
print(' ')
