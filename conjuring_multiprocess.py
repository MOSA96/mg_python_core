from multiprocessing import Process, current_process
import time

def alchemical_concoction(potion_number):
    """Create alchemical potion."""
    process_name = current_process().name
    print(f"Alchemist {process_name} begins potion {potion_number}.")
    time.sleep(potion_number)  # Simulate the time taken to brew the potion.
    print(f"Alchemist {process_name} has completed potion {potion_number}.")

def cauldrons_of_creation():
    """Spell to create and manage multiple potion-brewing processes."""
    alchemists = []
    for potion_number in range(1, 4):
        alchemist = Process(target=alchemical_concoction, args=(potion_number,), name=f"Alchemist-{potion_number}")
        alchemists.append(alchemist)
        alchemist.start()
    
    for alchemist in alchemists:
        alchemist.join()  

if __name__ == "__main__":
    cauldrons_of_creation()