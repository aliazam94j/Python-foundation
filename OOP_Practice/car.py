
class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

    def driving(self):
        print(f"your driving the {self.color} {self.model} ")


    def stop(self):
        print(f"your stopped the {self.model}")


    def parkering(self):
        print(f"your parking the {self.model}")

    def forSALE(self):
        print(f"is the {self.color} {self.model} {self.year} for sale? = {self.for_sale}")    