from main import *
from itertools import combinations

if __name__ == "__main__":
    ciphertext = "SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW"
    crib = "TUTOR"
    
    # Set up the plugboard
    plugboard = Plugboard()
    plugboard_pairs = ["WP", "RJ", "VF", "HN", "CG", "BS"] # Missing pairs of A_ and I_
    for pair in plugboard_pairs:
        plugboard.add(PlugLead(pair))


    complement_leads = "DEKLMOQTUXYZ" # Possible leads connecting with A and I
    
    # Connect A with each of complement leads
    for i, l in enumerate(complement_leads):
        # Reset the plugboard mapping dict by removing previous tried 4 pairs (2 pairs of A, 2 pairs of I)
        if i > 0:
            for j in range(4):
                plugboard.mapping_dict.popitem()
        
        plugboard.mapping_dict.update({"A": l, l: "A"})

        remaining_leads = complement_leads.replace(l, "") # Remaining possible leads connecting with I

        for index, lead in enumerate(remaining_leads):
            # Reset the plugboard mapping dict by removing previous tried 2 pairs of I
            if index > 0:
                for k in range(2):
                    plugboard.mapping_dict.popitem()

            plugboard.mapping_dict.update({"I": lead, lead: "I"})

            # Set up the rotors and reflector
            rotor1 = Rotor("IV", "10", "U")
            rotor2 = Rotor("III", "12", "W")
            rotor3 = Rotor("V", "24", "S")
            reflector = Reflector("A")

            enigma = EnigmaMachine(plugboard, [rotor1, rotor2, rotor3], reflector)
            plaintext = enigma.encode(ciphertext)

            if plaintext == "NOTUTORSWEREHARMEDNORIMPLICATEDOFCRIMESDURINGTHEMAKINGOFTHESEEXAMPLES":
                print(f"Plaintext: {plaintext}.")
                print(f"Plugboard pairs: {plugboard.mapping_dict}")