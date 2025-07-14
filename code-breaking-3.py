from itertools import permutations
from itertools import product
from main import *

if __name__ == "__main__":
    # Set up plugboard
    plugboard = Plugboard()
    plugboard_pairs = ["FH", "TS", "BE", "UQ", "KD", "AL"]
    for pair in plugboard_pairs:
        plugboard.add(PlugLead(pair))

    # Rotor combinations
    rotors = ["II", "IV", "Beta", "Gamma"]
    rotor_combinations = list(permutations(rotors, 3)) # Permutations of 3 rotors out of 4 given rotors

    ring_settings = ["02", "04", "06", "08", "20", "22", "24", "26"]
    ring_setting_combinations = list(product(ring_settings, repeat=3)) # Products of 3 ring settings out of 8 possible ring settings

    reflectors = [Reflector("A"), Reflector("B"), Reflector("C")]    
    
    # Decrypte
    ciphertext = "ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY"
    crib = "THOUSANDS"

    for rotor_combination in rotor_combinations:
        for ring_setting_combination in ring_setting_combinations:
            for reflector in reflectors:
                rotor1 = Rotor(rotor_combination[0], ring_setting_combination[0], "Y")
                rotor2 = Rotor(rotor_combination[1], ring_setting_combination[1], "M")
                rotor3 = Rotor(rotor_combination[2], ring_setting_combination[2], "E")
        
                enigma = EnigmaMachine(plugboard, [rotor1, rotor2, rotor3], reflector)
                plaintext = enigma.encode(ciphertext)

                if crib in plaintext:
                    print(f"Plaintext: {plaintext}.")


    
    