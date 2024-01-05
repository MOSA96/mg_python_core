class EnchantedProxy:
    def __init__(self, target):
        self._target = target

    def __getattr__(self, name):
        print(f"Proxy intercepted the retrieval of {name}!")
        return getattr(self._target, name)
        
    def __setattr__(self, name, value):
        if name == '_target':
            super().__setattr__(name, value)
        else:
            print(f"Proxy intercepted the setting of {name} to {value}!")
            setattr(self._target, name, value)

class SimpleSpellbook:
    def __init__(self):
        self.spells = []

    def add_spell(self, spell):
        self.spells.append(spell)

    def show_spells(self):
        return self.spells

my_spellbook = SimpleSpellbook()
proxy_spellbook = EnchantedProxy(my_spellbook)

proxy_spellbook.add_spell("Mystic Shield")  
print(proxy_spellbook.show_spells())        

