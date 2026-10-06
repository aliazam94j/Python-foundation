# Class variables




class EnergyDrink:
    #Class variables 
    class_name = "CleanSavd"
    class_Price = 20

    def __init__(self,flavour,year,is_tasty):
        self.flavour = flavour
        self.year = year
        self.is_tasty = is_tasty
        EnergyDrink.class_Price +=1
        


energydrink1 = EnergyDrink("Pear",2024,True)
# energydrink2 = EnergyDrink("Apple",2026, True)
# energydrink3 = EnergyDrink("orange",2020,False)

print(f"the flavour {energydrink1.flavour} from {EnergyDrink.class_name} is ${EnergyDrink.class_Price}")