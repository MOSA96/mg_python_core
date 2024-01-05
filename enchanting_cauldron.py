def brew_potion(base_ingredient):
    """A high-order function that takes an ingredient and returns a potion."""
    
    def potion_strength(level):
        return f"Potion of {base_ingredient} at strength {level}"

    return potion_strength  

def enhance_potion(potion_brewing_function, additional_effect):
    """A high-order function that takes a potion brewing function and adds an additional effect."""
    def enhanced_potion(level):
        basic_potion = potion_brewing_function(level)
        return f"{basic_potion} with {additional_effect}"

    return enhanced_potion  

base_potion_brewing_function = brew_potion("Dragon's Breath") 
enchanted_potion_brewing_function = enhance_potion(base_potion_brewing_function, "Phoenix Feathers")  

print(enchanted_potion_brewing_function(5))
