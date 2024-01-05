def armor_enchantment(strength='light', material='leather'):
    def decorator(spell_function):
        def protected_spell(*args, **kwargs):
            print(f"A {strength} {material} armor encases the caster.")
            return spell_function(*args, **kwargs)
        return protected_spell
    return decorator

@armor_enchantment(strength='heavy', material='mithril')
def charge_spell():
    print("The caster charges forward with enhanced vigor.")

charge_spell()
