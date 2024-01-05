class DynamicClassCreator(type):
    def __new__(metacls, name, bases, namespace, **kwargs):
        cls = super().__new__(metacls, name, bases, namespace)
        for attribute_name, attribute_value in kwargs.items():
            setattr(cls, attribute_name, attribute_value)
        return cls

class Spell(metaclass=DynamicClassCreator, incantation="Abracadabra", potency=100):
    pass

spell = Spell()
print(f"The incantation is: {spell.incantation}") 
print(f"The spell's potency is: {spell.potency}")   
