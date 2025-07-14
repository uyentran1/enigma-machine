from main import *
from itertools import permutations

if __name__ == "__main__":
    
    # Update the reflector's mapping list with 2 new pairs in a set of permutations of 4
    # to demonstrate the non-standard reflector
    # There are four updated mapped pairs: perm[0] and perm[1], perm[2] and perm[3], 
    # original mapped chars of perm[0] and perm[1], and original mapped chars of perm[2] and perm[3]
    def update(inlist, perm):
        updated_list = inlist.copy()
        
        # Get index of each element in the permutation
        index_char_0 = ord(perm[0]) - ORDER_OF_A
        index_char_1 = ord(perm[1]) - ORDER_OF_A
        index_char_2 = ord(perm[2]) - ORDER_OF_A
        index_char_3 = ord(perm[3]) - ORDER_OF_A

        # Map the original mapped chars of perm[0] and perm[1]
        swapped_char_0 = updated_list[index_char_0] 
        swapped_char_1 = updated_list[index_char_1] 
        
        index_swapped_char_0 = ord(swapped_char_0) - ORDER_OF_A 
        index_swapped_char_1 = ord(swapped_char_1) - ORDER_OF_A 

        updated_list[index_swapped_char_0] = swapped_char_1 
        updated_list[index_swapped_char_1] = swapped_char_0

        # Map the original mapped chars of perm[2] and perm[3]
        swapped_char_2 = updated_list[index_char_2] 
        swapped_char_3 = updated_list[index_char_3] 

        index_swapped_char_2 = ord(swapped_char_2) - ORDER_OF_A 
        index_swapped_char_3 = ord(swapped_char_3) - ORDER_OF_A 

        updated_list[index_swapped_char_2] = swapped_char_3
        updated_list[index_swapped_char_3] = swapped_char_2
        
        # Map perm[0] with perm[1], and perm[2] with perm[3] 
        updated_list[index_char_0] = perm[1]
        updated_list[index_char_1] = perm[0]
        updated_list[index_char_2] = perm[3]
        updated_list[index_char_3] = perm[2]

        return updated_list
    
    def main():    
        ciphertext = "HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX"
        cribs = ["FACEBOOK", "LINKEDIN", "INSTAGRAM", "TWITTER"]

        # Set up plugboard
        plugboard = Plugboard()
        plugboard_pairs = ["UG", "IE", "PO", "NX", "WT"]
        for pair in plugboard_pairs:
            plugboard.add(PlugLead(pair))

        # Reflector possibilities
        reflectors = [Reflector("A"), Reflector("B"), Reflector("C")]
    
        # Permutations of new pairs in the reflector
        modified_pairs = 4
        perms = list(permutations("ABCDEFGHIKLMNOPQRSTUVWXYZ", modified_pairs))

        for reflector in reflectors:
            for perm in perms:
                reflector.mapping_list = update(reflector.original_mapping_list, perm)
                
                rotor1 = Rotor("IV", "07", "L")
                rotor2 = Rotor("II", "18", "J")
                rotor3 = Rotor("V", "06", "A")

                enigma = EnigmaMachine(plugboard, [rotor1, rotor2, rotor3], reflector)
                
                plaintext = enigma.encode_code_breaking_5(ciphertext)

                match_found = False
                
                for crib in cribs:
                    if crib in plaintext:
                        print(f"Plaintext: {plaintext}.")
                        print(f"Reflector: {reflector.name}.")
                        print(f"Reflector mapping: {reflector.mapping_list}.")
                        match_found = True
                        break

                if match_found:
                    break

    main()
    

