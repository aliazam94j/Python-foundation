# inheritance = allows a class to inherit attributes and methods from another class.
# from animal import Animal
# from animal import Cat
# from animal import Hawk
# from animal import Lion


# cat = Cat("Toto")
# hawk = Hawk("Birdy")
# lion = Lion("Simba")


# print(cat.name)
# cat.hunting()
# cat.Attack()
# cat.eat()
# cat.sleep()



#multi inheritance = inherit from more then one parent class

class Animal:
    def __init__(self,name):
        self.name = name
        
    def eating(self):
        print(f"{self.name} is eating")

    def sleeping(self):
        print(f"lazy {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print("this animal is fleeing")


class Predator(Animal):
    def hunt(self):
        print("this animal is hunting the prey")


class Chicken(Prey):
    pass


class Tiger(Predator):
    pass


class Bear(Predator):
    pass


class Fish(Prey,Predator):
    pass



chicken = Chicken("chik")
tiger = Tiger("Jaguar")
bear = Bear("Po")
fish = Fish("NEMO")



fish.eating()
fish.sleeping()