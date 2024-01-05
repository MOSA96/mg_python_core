def arcane_library(secret_archive):
    """Function that encapsulates."""
    def inner_sanctum(spell_name):
        return secret_archive.get(spell_name, "This spell is not in the archive")

    return inner_sanctum  

secret_spell_archive = {'Fireball': 'A blazing sphere of condensed flame.',
                        'Frostbind': 'An icy enchantment to ensnare the targeted entity.'}

arcane_keeper = arcane_library(secret_spell_archive)

print(arcane_keeper('Fireball'))  
print(arcane_keeper('Lightning Strike'))  