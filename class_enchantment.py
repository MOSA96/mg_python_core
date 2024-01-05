def verbose_class(cls):
    """A class decorator that augments each method."""
    class VerboseClass(cls):
        def __getattribute__(self, name):
            item = super().__getattribute__(name)
            if callable(item):
                print(f"Verbose mode: The method {name}() is being invoked.")
            return item
    
    return VerboseClass

@verbose_class
class MagicalItemRepository:
    def __init__(self):
        self.items = ['Mystic Wand', 'Enchanted Dagger', 'Elixir of Wisdom']

    def list_items(self):
        for item in self.items:
            print(f"- {item}")

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item}.")

repository = MagicalItemRepository()
repository.list_items()
repository.add_item('Invisibility Cloak')