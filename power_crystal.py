class ManaCrystal:
    def __init__(self, value=0):
        self._mana = value  

    def __get__(self, instance, owner):
        return self._mana

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Mana must be an integer value.")
        if value < 0 or value > 100:
            raise ValueError("Mana must be between 0 and 100.")
        self._mana = value

class WizardStaff:
    mana = ManaCrystal()  

    def __init__(self, name):
        self.name = name  


staff_of_elders = WizardStaff("Staff of Elders")
print(staff_of_elders.mana)  

staff_of_elders.mana = 50 
print(staff_of_elders.mana) 

try:
    staff_of_elders.mana = 5000  
except ValueError as error:
    print(error)  