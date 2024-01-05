class MagicalRealm:
    def __enter__(self):
        print("You enter a magical realm.")
        return self  

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Alas, A mishap occurred! {exc_value}")
        print("You leave the realm, its magic sealed safely within.")

with MagicalRealm() as realm:
    print("You practice your spells safely.")
    raise Exception("An arcane disturbance!")