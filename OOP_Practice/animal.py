class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True


    def eat(self):
        print(f"{self.name} is eating")


    def sleep(self):
        print(f"{self.name} is sleeping")

    def hunting(self):
        print(f"{self.name} is hunting")



class Cat(Animal):
    def Attack(self):
        print(f"{self.name} is attacking the prey")

class Hawk(Animal):
    pass


class Lion(Animal):
    pass