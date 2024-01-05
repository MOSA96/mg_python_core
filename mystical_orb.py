class MysticalOrb:
    def __init__(self, color, power):
        self.color = color  
        self.power = power  

    def __str__(self):
        return f"A {self.color} orb of {self.power} power."

    def __repr__(self):
        return f"MysticalOrb('{self.color}', {self.power})"

orb_of_foresight = MysticalOrb("crimson", 5000)

print(orb_of_foresight)  
print(repr(orb_of_foresight))  