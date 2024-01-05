class Spellbook:
    def __init__(self):
        self.spells = {}  # A dictionary to store the spells

    def __getitem__(self, spell_name):
        return self.spells.get(spell_name, "Spell not found")

    def __setitem__(self, spell_name, description):
        self.spells[spell_name] = description

my_spellbook = Spellbook()

my_spellbook['Arcane Bolt'] = 'A bolt of magical energy that seeks its target.'
my_spellbook['Healing Touch'] = 'A touch that revitalizes and mends wounds.'

# Retrieving spells
print(my_spellbook['Arcane Bolt'])    
print(my_spellbook['Invisibility'])   