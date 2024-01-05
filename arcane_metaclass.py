# arcane_metaclass.py

class ArcaneType(type):
    """A metaclass that defines behavior for the creation and initialization of new magical classes."""

    def __new__(metacls, name, bases, namespace, **kwds):
        cls = super().__new__(metacls, name, bases, namespace)
        cls.greet = lambda self: print(f"The magic of {name} has been invoked!")
        return cls

class Spellbook(metaclass=ArcaneType):
    def __init__(self, title):
        self.title = title

grimoire = Spellbook("Grimoire of the Arcane")
grimoire.greet()